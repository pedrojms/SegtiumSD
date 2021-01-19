from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    #path('',views.index),
    path('contacto/',views.contacto,name='contact'),
    url(r'^noticias/$', views.MostrarNoticias, name="listar_noticias"),
    path('rservicios/',views.ListarServicios,name='r-servicios'),
    path('rempresa/',views.ListarEmpresa,name='r-empresa'),
    path('rvendedor/',views.ListarVendedor,name='r-vendedor'),
    url(r'^$', views.main_base_view, name='main_base'), 
    url(r'^login/$', views.login, name='login'),
    url(r'^reportes/$', views.reportes, name='reportes'),

	url(r'^(?P<dato>\d+)/actualizar$', views.editItem, name='actualizar-model'),
	url(r'^(?P<dato>\d+)', views.deleteItem, name='borrar-model'), 
	url(r'^agregar', views.add, name='agregar-model'),
]