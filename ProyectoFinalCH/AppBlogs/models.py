from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):
    id_blog = models.IntegerField(null=True)
    titulo = models.CharField(max_length = 50)
    subtitulo =  models.CharField(max_length = 50)
    cuerpo = RichTextField(blank=True, null=True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    fecha_posteo = models.DateTimeField(null=True, auto_now_add=False, auto_now=False, blank=True)

#class Avatar(models.Model):
#    user = models.ForeignKey(User, on_delete = models.CASCADE)
#    imagen = models.ImageField(upload_to="avatares", null = True, blank = True)
