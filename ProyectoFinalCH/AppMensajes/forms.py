from django import forms

class Formulario_mensaje(forms.Form):
    
    cuerpo = forms.CharField(max_length = 5000)
    receptor = forms.CharField(max_length = 50)
    imagen = forms.ImageField()