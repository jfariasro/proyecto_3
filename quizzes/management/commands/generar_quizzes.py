from django.core.management.base import BaseCommand
from quizzes.models import Quiz, Pregunta, Opcion

class Command(BaseCommand):
    help = 'Genera 10 quizzes de ejemplo con diferentes temáticas'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Quiz.objects.all().delete()
        
        # Quiz 1: Cultura General
        quiz1 = Quiz.objects.create(
            titulo="Quiz de Cultura General",
            descripcion="Pon a prueba tus conocimientos generales con este quiz interactivo.",
            activo=True
        )
        
        # Preguntas Quiz 1
        pregunta1 = Pregunta.objects.create(quiz=quiz1, texto="¿Cuál es la capital de Francia?")
        Opcion.objects.create(pregunta=pregunta1, texto="París", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta1, texto="Madrid", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta1, texto="Roma", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta1, texto="Berlín", es_correcta=False)
        
        pregunta2 = Pregunta.objects.create(quiz=quiz1, texto="¿Quién pintó la Mona Lisa?")
        Opcion.objects.create(pregunta=pregunta2, texto="Leonardo da Vinci", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta2, texto="Pablo Picasso", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta2, texto="Vincent van Gogh", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta2, texto="Miguel Ángel", es_correcta=False)
        
        pregunta3 = Pregunta.objects.create(quiz=quiz1, texto="¿Cuál es el planeta más grande del sistema solar?")
        Opcion.objects.create(pregunta=pregunta3, texto="Júpiter", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta3, texto="Saturno", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta3, texto="Tierra", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta3, texto="Marte", es_correcta=False)
        
        # Quiz 2: Ciencias
        quiz2 = Quiz.objects.create(
            titulo="Quiz de Ciencias",
            descripcion="Desafía tus conocimientos científicos con preguntas de física, química y biología.",
            activo=True
        )
        
        pregunta4 = Pregunta.objects.create(quiz=quiz2, texto="¿Cuál es la fórmula química del agua?")
        Opcion.objects.create(pregunta=pregunta4, texto="H2O", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta4, texto="CO2", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta4, texto="O2", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta4, texto="H2SO4", es_correcta=False)
        
        pregunta5 = Pregunta.objects.create(quiz=quiz2, texto="¿Cuántos cromosomas tiene un ser humano normal?")
        Opcion.objects.create(pregunta=pregunta5, texto="46", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta5, texto="44", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta5, texto="48", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta5, texto="50", es_correcta=False)
        
        # Quiz 3: Historia
        quiz3 = Quiz.objects.create(
            titulo="Quiz de Historia Mundial",
            descripcion="Viaja a través del tiempo con preguntas sobre eventos históricos importantes.",
            activo=True
        )
        
        pregunta6 = Pregunta.objects.create(quiz=quiz3, texto="¿En qué año terminó la Segunda Guerra Mundial?")
        Opcion.objects.create(pregunta=pregunta6, texto="1945", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta6, texto="1944", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta6, texto="1946", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta6, texto="1943", es_correcta=False)
        
        pregunta7 = Pregunta.objects.create(quiz=quiz3, texto="¿Quién fue el primer emperador romano?")
        Opcion.objects.create(pregunta=pregunta7, texto="Augusto", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta7, texto="Julio César", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta7, texto="Nerón", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta7, texto="Marco Aurelio", es_correcta=False)
        
        # Quiz 4: Geografía
        quiz4 = Quiz.objects.create(
            titulo="Quiz de Geografía",
            descripcion="Explora el mundo con preguntas sobre países, capitales y geografía física.",
            activo=True
        )
        
        pregunta8 = Pregunta.objects.create(quiz=quiz4, texto="¿Cuál es el río más largo del mundo?")
        Opcion.objects.create(pregunta=pregunta8, texto="Río Nilo", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta8, texto="Río Amazonas", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta8, texto="Río Yangtsé", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta8, texto="Río Misisipi", es_correcta=False)
        
        pregunta9 = Pregunta.objects.create(quiz=quiz4, texto="¿En qué continente se encuentra el desierto del Sahara?")
        Opcion.objects.create(pregunta=pregunta9, texto="África", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta9, texto="Asia", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta9, texto="América", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta9, texto="Australia", es_correcta=False)
        
        # Quiz 5: Deportes
        quiz5 = Quiz.objects.create(
            titulo="Quiz de Deportes",
            descripcion="Demuestra tus conocimientos sobre deportes y atletas famosos.",
            activo=True
        )
        
        pregunta10 = Pregunta.objects.create(quiz=quiz5, texto="¿Cada cuántos años se celebran los Juegos Olímpicos de verano?")
        Opcion.objects.create(pregunta=pregunta10, texto="4 años", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta10, texto="2 años", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta10, texto="5 años", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta10, texto="3 años", es_correcta=False)
        
        pregunta11 = Pregunta.objects.create(quiz=quiz5, texto="¿En qué deporte destaca Lionel Messi?")
        Opcion.objects.create(pregunta=pregunta11, texto="Fútbol", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta11, texto="Baloncesto", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta11, texto="Tenis", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta11, texto="Golf", es_correcta=False)
        
        # Quiz 6: Tecnología
        quiz6 = Quiz.objects.create(
            titulo="Quiz de Tecnología",
            descripcion="Ponte a prueba con preguntas sobre tecnología, programación e innovación.",
            activo=True
        )
        
        pregunta12 = Pregunta.objects.create(quiz=quiz6, texto="¿Quién fundó Microsoft?")
        Opcion.objects.create(pregunta=pregunta12, texto="Bill Gates", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta12, texto="Steve Jobs", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta12, texto="Mark Zuckerberg", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta12, texto="Elon Musk", es_correcta=False)
        
        pregunta13 = Pregunta.objects.create(quiz=quiz6, texto="¿Qué significa HTML?")
        Opcion.objects.create(pregunta=pregunta13, texto="HyperText Markup Language", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta13, texto="High Tech Modern Language", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta13, texto="Hyper Transfer Markup Language", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta13, texto="Home Tool Markup Language", es_correcta=False)
        
        # Quiz 7: Matemáticas
        quiz7 = Quiz.objects.create(
            titulo="Quiz de Matemáticas",
            descripcion="Desafía tu mente con problemas matemáticos y conceptos numéricos.",
            activo=True
        )
        
        pregunta14 = Pregunta.objects.create(quiz=quiz7, texto="¿Cuál es el valor de π (pi) aproximadamente?")
        Opcion.objects.create(pregunta=pregunta14, texto="3.14159", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta14, texto="3.15159", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta14, texto="3.12159", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta14, texto="3.16159", es_correcta=False)
        
        pregunta15 = Pregunta.objects.create(quiz=quiz7, texto="¿Cuánto es 2² + 3²?")
        Opcion.objects.create(pregunta=pregunta15, texto="13", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta15, texto="11", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta15, texto="12", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta15, texto="14", es_correcta=False)
        
        # Quiz 8: Literatura
        quiz8 = Quiz.objects.create(
            titulo="Quiz de Literatura",
            descripcion="Explora el mundo de los libros, autores y obras literarias famosas.",
            activo=True
        )
        
        pregunta16 = Pregunta.objects.create(quiz=quiz8, texto="¿Quién escribió 'Cien años de soledad'?")
        Opcion.objects.create(pregunta=pregunta16, texto="Gabriel García Márquez", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta16, texto="Mario Vargas Llosa", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta16, texto="Julio Cortázar", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta16, texto="Octavio Paz", es_correcta=False)
        
        pregunta17 = Pregunta.objects.create(quiz=quiz8, texto="¿En qué año se publicó 'Don Quijote de la Mancha'?")
        Opcion.objects.create(pregunta=pregunta17, texto="1605", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta17, texto="1600", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta17, texto="1610", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta17, texto="1615", es_correcta=False)
        
        # Quiz 9: Música
        quiz9 = Quiz.objects.create(
            titulo="Quiz de Música",
            descripcion="Pon a prueba tus conocimientos sobre música, artistas e instrumentos.",
            activo=True
        )
        
        pregunta18 = Pregunta.objects.create(quiz=quiz9, texto="¿Cuántas cuerdas tiene una guitarra española clásica?")
        Opcion.objects.create(pregunta=pregunta18, texto="6", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta18, texto="4", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta18, texto="8", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta18, texto="12", es_correcta=False)
        
        pregunta19 = Pregunta.objects.create(quiz=quiz9, texto="¿Qué compositor escribió 'La Novena Sinfonía'?")
        Opcion.objects.create(pregunta=pregunta19, texto="Ludwig van Beethoven", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta19, texto="Wolfgang Amadeus Mozart", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta19, texto="Johann Sebastian Bach", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta19, texto="Franz Schubert", es_correcta=False)
        
        # Quiz 10: Cine
        quiz10 = Quiz.objects.create(
            titulo="Quiz de Cine",
            descripcion="Demuestra tus conocimientos sobre películas, directores y la industria cinematográfica.",
            activo=True
        )
        
        pregunta20 = Pregunta.objects.create(quiz=quiz10, texto="¿Qué película ganó el Oscar a Mejor Película en 1994?")
        Opcion.objects.create(pregunta=pregunta20, texto="Forrest Gump", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta20, texto="Pulp Fiction", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta20, texto="El Rey León", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta20, texto="Entrevista con el Vampiro", es_correcta=False)
        
        pregunta21 = Pregunta.objects.create(quiz=quiz10, texto="¿Quién dirigió la película 'Jaws' (Tiburón)?")
        Opcion.objects.create(pregunta=pregunta21, texto="Steven Spielberg", es_correcta=True)
        Opcion.objects.create(pregunta=pregunta21, texto="George Lucas", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta21, texto="Martin Scorsese", es_correcta=False)
        Opcion.objects.create(pregunta=pregunta21, texto="Francis Ford Coppola", es_correcta=False)
        
        self.stdout.write(
            self.style.SUCCESS('¡10 quizzes de ejemplo generados exitosamente!')
        )
