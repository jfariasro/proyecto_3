from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import os
from quizzes.utils import procesar_archivo_quiz


class Command(BaseCommand):
    help = 'Procesa un archivo de texto para crear un quiz'

    def add_arguments(self, parser):
        parser.add_argument('archivo', type=str, help='Ruta al archivo de texto del quiz')
        parser.add_argument('--titulo', type=str, help='Título del quiz (opcional)')
        parser.add_argument('--descripcion', type=str, default='', help='Descripción del quiz (opcional)')
        parser.add_argument('--tiempo', type=int, default=0, help='Tiempo límite en minutos (opcional)')

    def handle(self, *args, **options):
        archivo_path = options['archivo']
        
        if not os.path.exists(archivo_path):
            self.stdout.write(
                self.style.ERROR(f'El archivo {archivo_path} no existe.')
            )
            return
        
        if not archivo_path.endswith('.txt'):
            self.stdout.write(
                self.style.ERROR('Solo se permiten archivos .txt')
            )
            return
        
        try:
            with open(archivo_path, 'r', encoding='utf-8') as f:
                contenido = f.read()
            
            # Crear un objeto de archivo simulado
            archivo_simulado = ContentFile(contenido.encode('utf-8'))
            archivo_simulado.name = os.path.basename(archivo_path)
            
            # Usar título del archivo si no se proporciona
            titulo = options.get('titulo') or os.path.splitext(os.path.basename(archivo_path))[0]
            descripcion = options.get('descripcion', '')
            tiempo_limite = options.get('tiempo', 0)
            
            self.stdout.write(f'Procesando archivo: {archivo_path}')
            self.stdout.write(f'Título: {titulo}')
            
            # Procesar el archivo
            quiz, error = procesar_archivo_quiz(archivo_simulado, titulo, descripcion, tiempo_limite)
            
            if quiz:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Quiz "{quiz.titulo}" creado exitosamente!\n'
                        f'   - ID: {quiz.id}\n'
                        f'   - Preguntas: {quiz.preguntas.count()}\n'
                        f'   - Fecha: {quiz.fecha_creacion}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error al procesar el archivo: {error}')
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error inesperado: {str(e)}')
            )
