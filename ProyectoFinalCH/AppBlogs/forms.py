from django import forms

class Formulario_blog(forms.Form):
    titulo = forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo = forms.CharField(max_length = 3000)
    imagen = forms.ImageField()