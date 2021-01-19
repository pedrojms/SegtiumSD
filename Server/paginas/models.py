from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Oficina(models.Model): 

	ciudad = models.CharField(max_length=250) 
	telefono = models.CharField(max_length=250)  
	direccion = models.CharField(max_length=500)  


class Vendedor(models.Model):

	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250) 
	cedula=models.CharField(max_length=250) 
	telefono=models.CharField(max_length=250) 
	correo=models.EmailField() 
	oficina_id=models.ForeignKey(Oficina, null=True, blank=True, on_delete=models.CASCADE)

class Servicio(models.Model):

	nombre=models.CharField(max_length=250) 
	descripcion=models.TextField()

class Beneficios(models.Model):
	nombre=models.CharField(max_length=250) 
	descripcion=models.TextField()
	servicio_id=models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)

class Brochure(models.Model):
	nombre=models.CharField(max_length=250)
	fecha=models.DateField()
	servicio_id=models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)


class Empresa(models.Model):
	ruc=models.CharField(max_length=250)
	nombre=models.CharField(max_length=250)
	telefono=models.CharField(max_length=250)
	direccion=models.TextField()
	representante=models.CharField(max_length=250)

class Usuario(models.Model):
	nombre=models.CharField(max_length=250)
	apellido=models.CharField(max_length=250)
	correo=models.EmailField()
	contrasena=models.CharField(max_length=250)

class Solicitud(models.Model):
	detalle=models.TextField()
	fecha=models.DateField()
	ciudad=models.CharField(max_length=250)
	usuario=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Contrato(models.Model):
	fecha=models.DateField()
	precio=models.FloatField()
	usuario=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	empresa=models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
	vendedor=models.ForeignKey(Vendedor, null=True, blank=True, on_delete=models.CASCADE)
	servicio=models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)

class Noticias(models.Model):
	titulo=models.CharField(max_length=250)
	descripcion=models.TextField()
	fuente=models.CharField(max_length=250)
	fecha=models.DateField()
	imagen=models.CharField(max_length=250)


