import re
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppBlogs.forms import Formulario_blog, UserRegisterForm, UserEditForm, AvatarForm
from AppBlogs.models import Blog, Avatar
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def about_me(request):
    return (render(request, "about_me.html", {"request_user": request.user, "imagen": obtener_avatar(request)}))

def inicio(request):
    return (render(request, "inicio.html", {"imagen": obtener_avatar(request)}))

def pages(request):
    blogs = Blog.objects.all()
    #diccionario = {"blogs": blogs}
    #plantilla = loader.get_template("pages.html")
    #documento = plantilla.render(diccionario)
    #return HttpResponse(documento)
    return (render(request, "pages.html", {"blogs": blogs, "imagen": obtener_avatar(request)}))

@login_required
def form_blog(request):
    if (request.method == "POST"):
        formulario = Formulario_blog(request.POST, request.FILES)
        if (formulario.is_valid()):

            info = formulario.cleaned_data
            id_blog = len(Blog.objects.all()) + 1
            titulo = info.get("titulo")
            subtitulo = info.get("subtitulo")
            cuerpo = info.get("cuerpo")
            imagen = info.get("imagen")
            fecha_posteo = datetime.datetime.today()
            autor = request.user

            blog = Blog(id_blog = id_blog, titulo = titulo, subtitulo = subtitulo, cuerpo = cuerpo, autor = autor, imagen = imagen, fecha_posteo = fecha_posteo)
            blog.save()

            return (render(request, "inicio.html", {"mensaje": "Blog creado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_blog()
        return (render(request, "formulario_blog.html", {"formulario": formulario, "imagen": obtener_avatar(request)}))

def busqueda_blog(request):
    return (render(request, "busqueda_blog.html", {"imagen": obtener_avatar(request)}))

def blog(request):
    if request.GET["id_blog"]:
        id_blog = request.GET["id_blog"]
        blog = Blog.objects.get(id_blog__icontains = id_blog)
        condicion = False
        if (blog.autor == request.user.username):
            condicion = True
        else:
            condicion = False

        return render(request, "blog.html", {"blog": blog, "id_blog": id_blog, "condicion": condicion, "imagen": obtener_avatar(request)})

    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

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

@login_required
def mis_blogs(request):
    lista_blogs = Blog.objects.filter(autor = request.user)
    mensaje = ""
    if (len(lista_blogs) == 0):
        mensaje = "No tienes ningún blog todavía"
    else:
        mensaje = "Viendo todos tus blogs"

    return (render(request, 'mis_blogs.html', {"lista_blogs": lista_blogs, "mensaje": mensaje, "imagen": obtener_avatar(request)}))

# FUNCIÓN, NO VISTA
def obtener_avatar(request):
    if (request.user.is_authenticated):
        lista = Avatar.objects.filter(user = request.user)
        if (len(lista) != 0):
            imagen = lista[0].imagen.url
        else:
            imagen = None
        return imagen