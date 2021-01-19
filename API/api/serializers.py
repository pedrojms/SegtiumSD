from rest_framework import serializers
from . import models

class ServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Servicio
        fields = ("id",'nombre','descripcion','preciobase')


class NoticiasSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Noticias
		fields=("id","titulo","descripcion","fuente","fecha")


class VentasSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Ventas
		fields=("nombre","totalventas")