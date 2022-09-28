from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlogs.models import Blog

class Formulario_blog(forms.Form):
    titulo = forms.CharField(max_length = 50)
    subtitulo = forms.CharField(max_length = 50)
    cuerpo = forms.CharField(max_length = 3000)
    imagen = forms.ImageField()

class Formulario_editar_blog(forms.Form):

    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.titulo = self.cleaned_data['titulo']
        blog_post.subtitulo = self.cleaned_data['subtitulo']
        blog_post.cuerpo = self.cleaned_data['cuerpo']
        
        if self.cleaned_data['imagen']:
            blog_post.imagen = self.cleaned_data['imagen']
        
        if commit:
            blog_post.save()
        return blog_post