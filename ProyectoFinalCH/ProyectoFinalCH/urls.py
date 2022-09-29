"""ProyectoFinalCH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppBlogs.views import blog, about_me, inicio, pages, form_blog, busqueda_blog, mis_blogs, editar_blog
from AppRegistro.views import register, login_request, editar_perfil, editar_avatar
from AppMensajes.views import form_mensaje, mensajes, mensajes_recibidos, mensajes_enviados
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', about_me, name='about_me'),
    path('', inicio, name='inicio'),
    path('pages/', pages, name='pages'),
    path('form_blog/', form_blog, name='form_blog'),
    path('busqueda_blog/', busqueda_blog, name='busqueda_blog'),
    path('blog/', blog, name='blog'),
    path('register/', register, name = 'register'),
    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = 'logout'),
    path('editar_perfil/', editar_perfil, name = 'editar_perfil'),
    path('editar_avatar/', editar_avatar, name = 'editar_avatar'),
    path('editar_blog/', editar_blog, name = 'editar_blog'),
    path('mis_blogs/', mis_blogs, name = 'mis_blogs'),
    path('mensajes/', mensajes, name = 'mensajes'),
    path('form_mensaje/', form_mensaje, name = 'form_mensaje'),
    path('mensajes_recibidos/', mensajes_recibidos, name = 'mensajes_recibidos'),
    path('mensajes_enviados/', mensajes_enviados, name = 'mensajes_enviados'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
