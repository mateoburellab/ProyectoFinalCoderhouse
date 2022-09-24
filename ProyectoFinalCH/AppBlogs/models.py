from django.db import models
from datetime import datetime, date

# Create your models here.

class Blog(models.Model):
    id_blog = models.IntegerField()
    titulo = models.CharField(max_length = 50)
    subtitulo =  models.CharField(max_length = 50)
    cuerpo = models.CharField(max_length = 3000)
    autor = models.CharField(max_length = 30)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    fecha_posteo = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)