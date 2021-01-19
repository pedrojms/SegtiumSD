from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class ServicioViewset(viewsets.ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServiciosSerializer

class NoticiasViewset(viewsets.ModelViewSet):
	queryset = models.Noticias.objects.all()
	serializer_class = serializers.NoticiasSerializer

class VentasViewset(viewsets.ModelViewSet):
	queryset = models.Ventas.objects.all()
	serializer_class = serializers.VentasSerializer