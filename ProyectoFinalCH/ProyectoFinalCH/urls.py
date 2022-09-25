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
from AppBlogs.views import about_me, inicio, pages, form_blog, busqueda_blog, blog, register, login_request, editar_perfil
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about_me, name='about_me'),
    path('inicio/', inicio, name='inicio'),
    path('pages/', pages, name='pages'),
    path('form_blog/', form_blog, name='form_blog'),
    path('busqueda_blog/', busqueda_blog, name='busqueda_blog'),
    path('blog/', blog, name='blog'),
    path('register/', register, name = 'register'),
    path('login/', login_request, name = 'login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name = 'logout'),
    path('editar_perfil/', editar_perfil, name = 'editar_perfil'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
