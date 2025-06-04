from django.db import models

class Quiz(models.Model):
    """Representa un quiz educativo."""
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    """Representa una pregunta dentro de un quiz."""
    quiz = models.ForeignKey(Quiz, related_name='preguntas', on_delete=models.CASCADE)
    texto = models.CharField(max_length=500)

    def __str__(self):
        return self.texto

class Opcion(models.Model):
    """Representa una opción de respuesta para una pregunta."""
    pregunta = models.ForeignKey(Pregunta, related_name='opciones', on_delete=models.CASCADE)
    texto = models.CharField(max_length=300)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto

class Participacion(models.Model):
    """Registro de la participación de un usuario en un quiz."""
    usuario = models.CharField(max_length=150)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    puntaje = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.usuario} - {self.quiz.titulo} ({self.puntaje})"

class Respuesta(models.Model):
    """Respuesta de un usuario a una pregunta en un quiz."""
    participacion = models.ForeignKey(Participacion, related_name='respuestas', on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.participacion.usuario} - {self.pregunta.texto}"
