"""Segtium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path,include
from paginas import views
from django.conf import settings
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('paginas.urls')),
    #path('',views.index),
    #path('contacto/',views.contacto)
    path('home/',views.index,name='home'),
    path('somos/',views.somos, name='somos'),
    path('perfil/',views.perfil, name='perfil'),
    url(r'^hacemos/(?P<dato>\d+)',views.servicios,name='servicios'),
    #path('contactenos.html',views.contacto),
    path('noticias/',views.noticias,name='noticias'),
    path('carrito/',views.carrito,name='carrito'),
    
    #path('',views.contacto)
    url(r'', include('paginas.urls')),  
    url(r'^logout/', LogoutView.as_view(template_name='index.html'), name='logout'),
]
