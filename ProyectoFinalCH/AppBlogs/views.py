from ast import For
import re
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic import UpdateView
from AppBlogs.forms import Formulario_blog, Formulario_editar_blog
from AppBlogs.models import Blog
from AppRegistro.views import obtener_avatar
import datetime

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

def blog(request):
    if request.GET["id_blog"]:
        id_blog = request.GET["id_blog"]
        blog = Blog.objects.get(id_blog__icontains = id_blog)
        condicion = False
        if (blog.autor == request.user):
            condicion = True
        else:
            condicion = False

        return render(request, "blog.html", {"blog": blog, "id_blog": id_blog, "condicion": condicion, "imagen": obtener_avatar(request)})

    else:
        respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)

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
        return (render(request, "formulario_blog.html", {"form": formulario, "imagen": obtener_avatar(request)}))

def busqueda_blog(request):
    return (render(request, "busqueda_blog.html", {"imagen": obtener_avatar(request)}))

@login_required
def editar_blog(request):
    context = {}

    user = request.user
    blog_post = Blog.objects.get(id_blog = 1)
    if request.POST:
        form = Formulario_editar_blog(request.POST or None, request.FILES or None, instance = blog_post)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.save()
            context['success_message'] = 'Editado correctamente'
            blog_post = obj
    form = Formulario_editar_blog(
        initial = {
            "titulo": blog_post.titulo,
            "subtitulo": blog_post.subtitulo,
            "cuerpo": blog_post.cuerpo,
            "imagen": blog_post.imagen
        }
    )

    context['form'] = form
    return render(request, "editar_blog.html", context)

#class editar_blog(UpdateView):
    model = Blog
    template_name = "editar_blog.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']

@login_required
def mis_blogs(request):
    lista_blogs = Blog.objects.filter(autor = request.user)
    mensaje = ""
    if (len(lista_blogs) == 0):
        mensaje = "No tienes ningún blog todavía"
    else:
        mensaje = "Viendo todos tus blogs"

    return (render(request, 'mis_blogs.html', {"lista_blogs": lista_blogs, "mensaje": mensaje, "imagen": obtener_avatar(request)}))

