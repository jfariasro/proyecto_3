"""
Utilidades para procesar archivos de quiz
"""
from .models import Quiz, Pregunta, Opcion
from django.db import transaction


def procesar_archivo_quiz(archivo, titulo, descripcion="", tiempo_limite=0):
    """
    Procesa un archivo de texto y crea un quiz con sus preguntas y opciones.
    
    Formato esperado del archivo:
    Titulo del Quiz: [título opcional, se usa el del formulario si no se especifica]
    Descripcion: [descripción opcional]
    
    Pregunta: ¿Cuál es la capital de Francia?
    A) Londres
    B) Madrid
    C) París *
    D) Berlín
    
    Pregunta: ¿Cuánto es 2 + 2?
    A) 3
    B) 4 *
    C) 5
    D) 6
    
    * indica la respuesta correcta
    """
    
    try:
        # Leer el contenido del archivo
        contenido = archivo.read().decode('utf-8')
        lineas = contenido.strip().split('\n')
        
        quiz_data = {
            'titulo': titulo,
            'descripcion': descripcion,
            'tiempo_limite': tiempo_limite,
            'activo': True
        }
        
        preguntas_data = []
        pregunta_actual = None
        opciones_actuales = []
        
        i = 0
        while i < len(lineas):
            linea = lineas[i].strip()
            
            # Saltar líneas vacías
            if not linea:
                i += 1
                continue
            
            # Buscar título del quiz en el archivo (opcional)
            if linea.startswith('Titulo del Quiz:') and not quiz_data.get('titulo_from_file'):
                quiz_data['titulo'] = linea.replace('Titulo del Quiz:', '').strip() or titulo
                quiz_data['titulo_from_file'] = True
            
            # Buscar descripción en el archivo (opcional)
            elif linea.startswith('Descripcion:') and not quiz_data.get('descripcion_from_file'):
                quiz_data['descripcion'] = linea.replace('Descripcion:', '').strip() or descripcion
                quiz_data['descripcion_from_file'] = True
            
            # Nueva pregunta
            elif linea.startswith('Pregunta:'):
                # Guardar pregunta anterior si existe
                if pregunta_actual and opciones_actuales:
                    preguntas_data.append({
                        'texto': pregunta_actual,
                        'opciones': opciones_actuales.copy()
                    })
                
                # Iniciar nueva pregunta
                pregunta_actual = linea.replace('Pregunta:', '').strip()
                opciones_actuales = []
            
            # Opciones de respuesta
            elif linea and pregunta_actual and any(linea.startswith(prefix) for prefix in ['A)', 'B)', 'C)', 'D)', 'E)', 'F)']):
                es_correcta = linea.endswith(' *')
                texto_opcion = linea
                
                # Remover el asterisco si existe
                if es_correcta:
                    texto_opcion = linea[:-2].strip()
                
                opciones_actuales.append({
                    'texto': texto_opcion,
                    'es_correcta': es_correcta
                })
            
            i += 1
        
        # Agregar la última pregunta
        if pregunta_actual and opciones_actuales:
            preguntas_data.append({
                'texto': pregunta_actual,
                'opciones': opciones_actuales.copy()
            })
        
        # Validar que hay preguntas
        if not preguntas_data:
            raise ValueError("No se encontraron preguntas válidas en el archivo")
        
        # Crear el quiz y las preguntas en una transacción
        with transaction.atomic():
            # Crear el quiz
            quiz = Quiz.objects.create(
                titulo=quiz_data['titulo'],
                descripcion=quiz_data['descripcion'],
                tiempo_limite=quiz_data['tiempo_limite'],
                activo=quiz_data['activo']
            )
            
            # Crear preguntas y opciones
            for pregunta_data in preguntas_data:
                # Validar que la pregunta tenga al menos una respuesta correcta
                tiene_correcta = any(opt['es_correcta'] for opt in pregunta_data['opciones'])
                if not tiene_correcta:
                    raise ValueError(f"La pregunta '{pregunta_data['texto']}' no tiene ninguna respuesta marcada como correcta")
                
                # Crear pregunta
                pregunta = Pregunta.objects.create(
                    quiz=quiz,
                    texto=pregunta_data['texto']
                )
                
                # Crear opciones
                for opcion_data in pregunta_data['opciones']:
                    Opcion.objects.create(
                        pregunta=pregunta,
                        texto=opcion_data['texto'],
                        es_correcta=opcion_data['es_correcta']
                    )
        
        return quiz, None
        
    except UnicodeDecodeError:
        return None, "Error al leer el archivo. Asegúrate de que sea un archivo de texto válido."
    except Exception as e:
        return None, f"Error al procesar el archivo: {str(e)}"


def generar_archivo_ejemplo():
    """
    Genera un ejemplo de archivo de quiz para que el usuario sepa el formato
    """
    contenido_ejemplo = """Titulo del Quiz: Quiz de Ejemplo
Descripcion: Este es un quiz de ejemplo para mostrar el formato

Pregunta: ¿Cuál es la capital de Francia?
A) Londres
B) Madrid
C) París *
D) Berlín

Pregunta: ¿Cuánto es 2 + 2?
A) 3
B) 4 *
C) 5
D) 6

Pregunta: ¿Cuál es el planeta más grande del sistema solar?
A) Tierra
B) Marte
C) Júpiter *
D) Saturno

Pregunta: ¿En qué año llegó el hombre a la Luna?
A) 1967
B) 1968
C) 1969 *
D) 1970
"""
    return contenido_ejemplo
