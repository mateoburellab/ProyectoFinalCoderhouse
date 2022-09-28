from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    
    cuerpo = models.CharField(max_length = 3000)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
    emisor = models.ForeignKey(User, on_delete = models.CASCADE)
    receptor = models.CharField(max_length = 3000)
    fecha_envio = models.DateTimeField(null=True, auto_now_add=False, auto_now=False, blank=True)