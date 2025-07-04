from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Max
from datetime import timedelta
import json
from .models import Quiz, Participacion, Respuesta, Pregunta, Opcion
from .forms import QuizForm, PreguntaForm, OpcionForm, UploadQuizForm
from .utils import procesar_archivo_quiz, generar_archivo_ejemplo
from django.core.paginator import Paginator

def quiz_list(request):
    quizzes = Quiz.objects.filter(activo=True).order_by('-fecha_creacion')
    
    # Configurar paginación
    paginator = Paginator(quizzes, 6)  # 6 quizzes por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quizzes/quiz_list.html', {'page_obj': page_obj})

@login_required
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    preguntas = quiz.preguntas.all()
    
    # Verificar si el usuario ya participó
    participacion_existente = Participacion.objects.filter(usuario=request.user, quiz=quiz).first()
    
    return render(request, 'quizzes/quiz_detail.html', {
        'quiz': quiz, 
        'preguntas': preguntas,
        'participacion_existente': participacion_existente
    })

@login_required
@csrf_exempt
def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        data = json.loads(request.body)
        
        # Crear o actualizar participación
        participacion, created = Participacion.objects.get_or_create(
            usuario=request.user,
            quiz=quiz,
            defaults={'puntaje': 0, 'completado': False}
        )
        
        # Calcular puntaje
        puntaje = 0
        total_preguntas = quiz.preguntas.count()
        
        # Limpiar respuestas anteriores
        participacion.respuestas.all().delete()
        
        for pregunta_id, opcion_id in data['respuestas'].items():
            pregunta = quiz.preguntas.get(id=pregunta_id)
            opcion = pregunta.opciones.get(id=opcion_id)
            
            Respuesta.objects.create(
                participacion=participacion,
                pregunta=pregunta,
                opcion=opcion
            )
            
            if opcion.es_correcta:
                puntaje += 1
        
        # Actualizar participación
        participacion.puntaje = puntaje
        participacion.completado = True
        if 'tiempo_total' in data:
            participacion.tiempo_total = timedelta(seconds=data['tiempo_total'])
        participacion.save()
        
        porcentaje = round((puntaje / total_preguntas) * 100) if total_preguntas > 0 else 0
        
        return JsonResponse({
            'success': True,
            'puntaje': puntaje,
            'total': total_preguntas,
            'porcentaje': porcentaje,
            'redirect_url': f'/quiz/results/{participacion.id}/'
        })
    
    return JsonResponse({'success': False})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    participaciones = Participacion.objects.filter(usuario=request.user, completado=True).order_by('-fecha')
    
    # Configurar paginación
    paginator = Paginator(participaciones, 8)  # 8 participaciones por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    stats = {
        'total_quizzes': participaciones.count(),
        'promedio_puntaje': participaciones.aggregate(Avg('puntaje'))['puntaje__avg'] or 0,
        'mejor_puntaje': participaciones.aggregate(Max('puntaje'))['puntaje__max'] or 0,
    }
    return render(request, 'quizzes/profile.html', {'page_obj': page_obj, 'stats': stats})

@login_required
def leaderboard(request):
    # Top 10 usuarios por promedio de puntaje
    from django.db.models import Avg, Count
    top_users_data = Participacion.objects.filter(completado=True).values(
        'usuario__username', 'usuario__first_name', 'usuario__last_name'
    ).annotate(
        promedio_puntaje=Avg('puntaje'),
        total_quizzes=Count('id')
    ).order_by('-promedio_puntaje')[:10]
    
    # Calcular el ancho de progreso para cada usuario
    top_users = []
    for user_data in top_users_data:
        user_data['progreso_width'] = min(user_data['promedio_puntaje'] * 10, 100)
        top_users.append(user_data)
    
    return render(request, 'quizzes/leaderboard.html', {'top_users': top_users})

def is_staff_user(user):
    return user.is_authenticated and user.is_staff

# Vistas de administración
@user_passes_test(is_staff_user)
def admin_dashboard(request):
    stats = {
        'total_quizzes': Quiz.objects.count(),
        'total_preguntas': Pregunta.objects.count(),
        'total_participaciones': Participacion.objects.filter(completado=True).count(),
        'total_usuarios': User.objects.count(),
    }
    recent_participaciones = Participacion.objects.filter(completado=True).order_by('-fecha')[:5]
    return render(request, 'quizzes/admin/dashboard.html', {
        'stats': stats,
        'recent_participaciones': recent_participaciones
    })

@user_passes_test(is_staff_user)
def admin_quiz_list(request):
    quizzes = Quiz.objects.all().order_by('-fecha_creacion')
    
    # Configurar paginación
    paginator = Paginator(quizzes, 10)  # 10 quizzes por página en admin
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quizzes/admin/quiz_list.html', {'page_obj': page_obj})

@user_passes_test(is_staff_user)
def admin_quiz_create(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save()
            messages.success(request, f'Quiz "{quiz.titulo}" creado exitosamente.')
            return redirect('admin_quiz_edit', quiz_id=quiz.id)
    else:
        form = QuizForm()
    return render(request, 'quizzes/admin/quiz_form.html', {'form': form, 'title': 'Crear Quiz'})

@user_passes_test(is_staff_user)
def admin_quiz_edit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)
        if form.is_valid():
            form.save()
            messages.success(request, f'Quiz "{quiz.titulo}" actualizado exitosamente.')
            return redirect('admin_quiz_list')
    else:
        form = QuizForm(instance=quiz)
    
    preguntas = quiz.preguntas.all()
    return render(request, 'quizzes/admin/quiz_edit.html', {
        'form': form, 
        'quiz': quiz, 
        'preguntas': preguntas,
        'title': f'Editar Quiz: {quiz.titulo}'
    })

@user_passes_test(is_staff_user)
def admin_quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        titulo = quiz.titulo
        quiz.delete()
        messages.success(request, f'Quiz "{titulo}" eliminado exitosamente.')
        return redirect('admin_quiz_list')
    return render(request, 'quizzes/admin/quiz_delete.html', {'quiz': quiz})

@user_passes_test(is_staff_user)
def admin_pregunta_create(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.quiz = quiz
            pregunta.save()
            messages.success(request, 'Pregunta creada exitosamente.')
            return redirect('admin_pregunta_edit', pregunta_id=pregunta.id)
    else:
        form = PreguntaForm()
    return render(request, 'quizzes/admin/pregunta_form.html', {
        'form': form, 
        'quiz': quiz,
        'title': f'Crear Pregunta para: {quiz.titulo}'
    })

@user_passes_test(is_staff_user)
def admin_pregunta_edit(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    if request.method == 'POST':
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pregunta actualizada exitosamente.')
            return redirect('admin_quiz_edit', quiz_id=pregunta.quiz.id)
    else:
        form = PreguntaForm(instance=pregunta)
    
    opciones = pregunta.opciones.all()
    return render(request, 'quizzes/admin/pregunta_edit.html', {
        'form': form,
        'pregunta': pregunta,
        'opciones': opciones,
        'title': f'Editar Pregunta'
    })

@user_passes_test(is_staff_user)
def admin_pregunta_delete(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    quiz_id = pregunta.quiz.id
    if request.method == 'POST':
        pregunta.delete()
        messages.success(request, 'Pregunta eliminada exitosamente.')
        return redirect('admin_quiz_edit', quiz_id=quiz_id)
    return render(request, 'quizzes/admin/pregunta_delete.html', {'pregunta': pregunta})

@user_passes_test(is_staff_user)
def admin_opcion_create(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    if request.method == 'POST':
        form = OpcionForm(request.POST)
        if form.is_valid():
            opcion = form.save(commit=False)
            opcion.pregunta = pregunta
            opcion.save()
            messages.success(request, 'Opción creada exitosamente.')
            return redirect('admin_pregunta_edit', pregunta_id=pregunta.id)
    else:
        form = OpcionForm()
    return render(request, 'quizzes/admin/opcion_form.html', {
        'form': form,
        'pregunta': pregunta,
        'title': f'Crear Opción'
    })

@user_passes_test(is_staff_user)
def admin_opcion_edit(request, opcion_id):
    opcion = get_object_or_404(Opcion, id=opcion_id)
    pregunta = opcion.pregunta
    if request.method == 'POST':
        form = OpcionForm(request.POST, instance=opcion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opción actualizada exitosamente.')
            return redirect('admin_pregunta_edit', pregunta_id=pregunta.id)
    else:
        form = OpcionForm(instance=opcion)
    return render(request, 'quizzes/admin/opcion_form.html', {
        'form': form,
        'opcion': opcion,
        'pregunta': pregunta,
        'title': f'Editar Opción'
    })

@user_passes_test(is_staff_user)
def admin_opcion_delete(request, opcion_id):
    opcion = get_object_or_404(Opcion, id=opcion_id)
    pregunta_id = opcion.pregunta.id
    if request.method == 'POST':
        opcion.delete()
        messages.success(request, 'Opción eliminada exitosamente.')
        return redirect('admin_pregunta_edit', pregunta_id=pregunta_id)
    return render(request, 'quizzes/admin/opcion_delete.html', {'opcion': opcion})

@user_passes_test(is_staff_user)
def admin_participaciones(request):
    participaciones = Participacion.objects.filter(completado=True).order_by('-fecha')
    
    # Configurar paginación
    paginator = Paginator(participaciones, 15)  # 15 participaciones por página en admin
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'quizzes/admin/participaciones.html', {'page_obj': page_obj})

@user_passes_test(is_staff_user)
def upload_quiz(request):
    """Vista para subir un archivo de quiz"""
    if request.method == 'POST':
        form = UploadQuizForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            titulo = form.cleaned_data['titulo_quiz']
            descripcion = form.cleaned_data['descripcion_quiz']
            tiempo_limite = form.cleaned_data['tiempo_limite']
            
            # Validar tamaño del archivo (máximo 2MB)
            if archivo.size > 2 * 1024 * 1024:
                messages.error(request, 'El archivo es demasiado grande. Máximo 2MB permitido.')
                return render(request, 'quizzes/admin/upload_quiz.html', {'form': form})
            
            # Validar extensión del archivo
            if not archivo.name.endswith('.txt'):
                messages.error(request, 'Solo se permiten archivos .txt')
                return render(request, 'quizzes/admin/upload_quiz.html', {'form': form})
            
            # Procesar el archivo
            quiz, error = procesar_archivo_quiz(archivo, titulo, descripcion, tiempo_limite)
            
            if quiz:
                messages.success(request, f'Quiz "{quiz.titulo}" creado exitosamente desde el archivo. Se crearon {quiz.preguntas.count()} preguntas.')
                return redirect('admin_quiz_edit', quiz_id=quiz.id)
            else:
                messages.error(request, f'Error al procesar el archivo: {error}')
    else:
        form = UploadQuizForm()
    
    return render(request, 'quizzes/admin/upload_quiz.html', {'form': form})

@user_passes_test(is_staff_user)
def download_example_quiz(request):
    """Vista para descargar un archivo de ejemplo"""
    from django.http import HttpResponse
    
    contenido = generar_archivo_ejemplo()
    response = HttpResponse(contenido, content_type='text/plain; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="ejemplo_quiz.txt"'
    return response

@login_required
def quiz_results(request, participacion_id):
    """Vista para mostrar los resultados detallados de un quiz completado"""
    participacion = get_object_or_404(Participacion, id=participacion_id, usuario=request.user, completado=True)
    
    # Obtener todas las preguntas del quiz con las respuestas del usuario
    preguntas_con_respuestas = []
    
    for pregunta in participacion.quiz.preguntas.all():
        # Buscar la respuesta del usuario para esta pregunta
        respuesta_usuario = participacion.respuestas.filter(pregunta=pregunta).first()
        
        # Obtener la opción correcta
        opcion_correcta = pregunta.opciones.filter(es_correcta=True).first()
        
        # Determinar si la respuesta fue correcta
        es_correcta = False
        if respuesta_usuario and opcion_correcta:
            es_correcta = respuesta_usuario.opcion.id == opcion_correcta.id
        
        preguntas_con_respuestas.append({
            'pregunta': pregunta,
            'opciones': pregunta.opciones.all(),
            'respuesta_usuario': respuesta_usuario.opcion if respuesta_usuario else None,
            'opcion_correcta': opcion_correcta,
            'es_correcta': es_correcta
        })
    
    # Calcular estadísticas
    total_preguntas = len(preguntas_con_respuestas)
    respuestas_correctas = sum(1 for item in preguntas_con_respuestas if item['es_correcta'])
    respuestas_incorrectas = total_preguntas - respuestas_correctas
    porcentaje = round((respuestas_correctas / total_preguntas) * 100) if total_preguntas > 0 else 0
    
    contexto = {
        'participacion': participacion,
        'preguntas_con_respuestas': preguntas_con_respuestas,
        'total_preguntas': total_preguntas,
        'respuestas_correctas': respuestas_correctas,
        'respuestas_incorrectas': respuestas_incorrectas,
        'porcentaje': porcentaje
    }
    
    return render(request, 'quizzes/quiz_results.html', contexto)
