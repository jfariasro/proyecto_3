from django.contrib import admin
from .models import Quiz, Pregunta, Opcion, Participacion, Respuesta

admin.site.register(Quiz)
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Participacion)
admin.site.register(Respuesta)
