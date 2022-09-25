from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppBlogs.forms import Formulario_blog, UserRegisterForm
from AppBlogs.models import Blog
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def about_me(request):

    diccionario = {}
    plantilla = loader.get_template("about_me.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def inicio(request):
    diccionario = {}
    plantilla = loader.get_template("inicio.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def pages(request):
    blogs = Blog.objects.all()
    diccionario = {"blogs": blogs}
    plantilla = loader.get_template("pages.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

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

            blog = Blog(id_blog = id_blog, titulo = titulo, subtitulo = subtitulo, cuerpo = cuerpo, imagen = imagen, fecha_posteo = fecha_posteo)
            blog.save()

            return (render(request, "inicio.html", {"mensaje": "Blog creado"}))
        else:
            return (render(request, "inicio.html", {"mensaje": "Error"}))
        
    else:
        formulario = Formulario_blog()
        return (render(request, "formulario_blog.html", {"formulario": formulario}))

def busqueda_blog(request):
    return (render(request, "busqueda_blog.html"))

def blog(request):
    if request.GET["id_blog"]:
        id_blog = request.GET["id_blog"]
        blog = Blog.objects.get(id_blog__icontains = id_blog)

        return render(request, "blog.html", {"blog": blog, "id_blog": id_blog})

    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"inicio.html", {"mensaje":f"Usuario Creado {username} :)"})
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
                return render(request, 'inicio.html', {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, 'login.html', {"form": form, "mensaje": 'Usuario o contraseña incorrectos'})
        else:
                return render(request, 'login.html', {"form": form, "mensaje": 'Usuario o contraseña incorrectos'})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {"form": form})