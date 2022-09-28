from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppMensajes.models import Mensaje
from AppMensajes.forms import Formulario_mensaje
from django.contrib.auth.models import User
import datetime
from AppRegistro.views import obtener_avatar

# Create your views here.

@login_required
def form_mensaje(request):
    if (request.method == "POST"):
        formulario = Formulario_mensaje(request.POST, request.FILES)
        if (formulario.is_valid()):
            info = formulario.cleaned_data
            receptor_info = info.get("receptor")
            receptor1 = User.objects.filter(username = receptor_info)
            if (len(receptor1) == 0):
                return (render(request, "inicio.html", {"mensaje": "Usuario receptor no encontrado"}))
            else:
                emisor1 = request.user
                cuerpo = info.get("cuerpo")
                imagen = info.get("imagen")
                fecha_envio = datetime.datetime.today()
                mensaje = Mensaje(cuerpo = cuerpo, emisor = emisor1, receptor = receptor_info, imagen = imagen, fecha_envio = fecha_envio)
                mensaje.save()
                return (render(request, "inicio.html", {"mensaje": "Mensaje Enviado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Formulario no válido"}))
    else:
        formulario = Formulario_mensaje()
    return (render(request, "form_mensaje.html", {"form": formulario, "imagen": obtener_avatar(request)}))

@login_required    
def mensajes_recibidos(request):
        mensajes = Mensaje.objects.filter(receptor = request.user.username)
        if (len(mensajes) != 0):
            return render(request, "mensajes_recibidos.html", {"aviso": "Viendo todos los mensajes recibidos", "mensajes": mensajes})
        else:
            return render(request, "mensajes_recibidos.html", {"aviso": "No tienes mensajes"})

@login_required    
def mensajes_enviados(request):
        mensajes = Mensaje.objects.filter(emisor = request.user)
        if (len(mensajes) != 0):
            return render(request, "mensajes_enviados.html", {"aviso": "Viendo todos los mensajes enviados", "mensajes": mensajes})
        else:
            return render(request, "mensajes_enviados.html", {"aviso": "No enviaste ningún mensaje"})
    
def mensajes(request):
    return (render(request, "mensajes.html", {"imagen": obtener_avatar(request)}))