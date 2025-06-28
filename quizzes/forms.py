from django import forms
from .models import Quiz, Pregunta, Opcion

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['titulo', 'descripcion', 'activo', 'tiempo_limite']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título del quiz'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción del quiz'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tiempo_limite': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tiempo en minutos (0 = sin límite)'}),
        }

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto']
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Texto de la pregunta'}),
        }

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['texto', 'es_correcta']
        widgets = {
            'texto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Texto de la opción'}),
            'es_correcta': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UploadQuizForm(forms.Form):
    archivo = forms.FileField(
        label='Archivo del Quiz',
        help_text='Selecciona un archivo .txt con el formato del quiz',
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': '.txt'
        })
    )
    titulo_quiz = forms.CharField(
        max_length=200,
        label='Título del Quiz',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Título para el quiz'
        })
    )
    descripcion_quiz = forms.CharField(
        required=False,
        label='Descripción del Quiz',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Descripción opcional del quiz'
        })
        
    )
    tiempo_limite = forms.IntegerField(
        initial=0,
        label='Tiempo límite (minutos)',
        help_text='0 = sin límite de tiempo',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'min': '0'
        })
    )
