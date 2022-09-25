from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class Formulario_blog(forms.Form):
    titulo = forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo = forms.CharField(max_length = 3000)
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}