from .models import Empresa,Vendedor, Servicio,Beneficios,Noticias,Usuario
import requests,json

def ListadoEmpresa():
	model=Empresa.objects.raw('SELECT * FROM reporteempresa()')
	return model

def ListadoVendedor():
	model=Vendedor.objects.raw('SELECT * FROM reportevendedor()')
	return model

def ListadoServicio():
	model=Servicio.objects.raw('SELECT * FROM reporteservicios()')
	
	return model

def ServiciosCon(entidad):
	model=Servicio.objects.raw("SELECT ps.id, ps.nombre, ps.descripcion FROM paginas_servicio ps WHERE ps.nombre='"+entidad+"'")
	return model


def BeneficiosCon(entidad):
	model=Beneficios.objects.raw("SELECT pb.id ,pb.descripcion FROM paginas_servicio ps ,paginas_beneficios pb WHERE ps.id=pb.servicio_id_id and ps.nombre='"+entidad+"'")
	return model


def ListarNoticias(entidad):
	response = requests.get('http://db:8005/'+entidad+'/')
	data = response.json()
	return data

def ElemInd(entidad,dato):
	response = requests.get('http://db:8005/'+entidad+'/'+dato+'/')
	data = response.json()
	return data

def Edit(dato,registro):
	response=requests.put('http://db:8005/noticias/'+dato+"/",registro)
	return response

def Add(registro):
	response=requests.post('http://db:8005/noticias/',registro)
	return response

def Delete(dato):
	response=requests.delete('http://db:8005/noticias/'+dato+"/")
	return response

def InfoPerfil(correo):
  model=Usuario.objects.raw("SELECT pu.id,pu.nombre,pu.apellido,pu.correo FROM paginas_usuario pu WHERE pu.correo='"+correo+"'")
  return model
