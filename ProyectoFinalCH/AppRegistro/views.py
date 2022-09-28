from ast import For
import re
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import UpdateView
from AppRegistro.forms import UserRegisterForm, UserEditForm, AvatarForm
from AppRegistro.models import Avatar
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"inicio.html", {"mensaje":f"Usuario Creado {username} :)", "imagen": obtener_avatar(request)})
    else:    
        form = UserRegisterForm()
    return render(request,"register.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu = request.POST["username"]
            clave = request.POST["password"]

            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'inicio.html')
            else:
                return render(request, 'login.html', {"form": form, "mensaje": 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'login.html', {"form": form, "mensaje": 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form, "imagen": obtener_avatar(request)})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance = usuario)
        if form.is_valid():
            #info = form.cleaned_data
            #usuario.email = info["email"]
            #usuario.password1 = info["password1"]
            #usuario.password2 = info["password2"]
            #usuario.save()
            form.save()
            return render(request, 'inicio.html', {"mensaje": f"Perfil de {usuario} editado"})
    else:
        form = UserEditForm(instance = usuario)
    return render(request, 'editar_perfil.html', {"form": form, "usuario": usuario, "imagen": obtener_avatar(request)})

@login_required
def editar_avatar(request):
    if (request.method == 'POST'):
        formulario = AvatarForm(request.POST, request.FILES)
        if (formulario.is_valid()):
            avatar_viejo = Avatar.objects.filter(user = request.user)
            if (len(avatar_viejo) > 0):
                avatar_viejo.delete()
            avatar = Avatar(user = request.user, imagen = formulario.cleaned_data['imagen'])
            avatar.save()
            return (render(request, 'inicio.html', {"usuario": request.user, "mensaje": "Avatar agregado exitosamente", "imagen": obtener_avatar(request)}))
    else:
        formulario = AvatarForm()
    return (render(request, "editar_avatar.html", {"form": formulario, "usuario": request.user, "imagen": obtener_avatar(request)}))

# FUNCIÓN, NO VISTA
def obtener_avatar(request):
    if (request.user.is_authenticated):
        lista = Avatar.objects.filter(user = request.user)
        if (len(lista) != 0):
            imagen = lista[0].imagen.url
        else:
            imagen = None
        return imagen