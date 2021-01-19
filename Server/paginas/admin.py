from __future__ import unicode_literals 

from django.contrib import admin 
from .models import Noticias,Servicio,Brochure,Vendedor,Empresa,Beneficios
from .views import ListarServicios
from . import views
from django.conf.urls import url

class NoticiaAdmin(admin.ModelAdmin): 
	ordering = ('-id',) 

	search_fields = ('titulo', 'descripcion','fuente','imagen',) 


class ServicioAdmin(admin.ModelAdmin):
	ordering = ('-id',) 

	search_fields = ('nombre', 'descripcion') 
		

class BrochureAdmin(admin.ModelAdmin):
	ordering = ('-id',) 

	search_fields = ('nombre','fecha') 


class VendedorAdmin(admin.ModelAdmin):
	ordering = ('-id',) 

	search_fields = ('nombre', 'apellido','cedula','telefono','correo') 


class EmpresaAdmin(admin.ModelAdmin):
	ordering = ('-id',) 

	search_fields = ('ruc','nombre', 'telefono','direccion','representante')


class BeneficiosAdmin(admin.ModelAdmin):
	ordering = ('-id',) 

	search_fields = ('nombre', 'descripcion')  



admin.site.register(Noticias, NoticiaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Brochure, BrochureAdmin) 
admin.site.register(Vendedor, VendedorAdmin) 
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Beneficios, BeneficiosAdmin)  