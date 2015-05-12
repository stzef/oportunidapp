from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User

from habilidades.models import habilidadesModel, habCategoriasModel
from usuarios.models import perfilUsuarioModel


from django.http import HttpResponse
import json

# Create your views here.
def inicio(request):
	return render(request,'home.html')

def find(request):
	categorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'find.html',{'categorias':categorias})

def personasListar(request):
	if request.is_ajax():
		categoria = request.GET.get('categoria',None)
		habilidades = habilidadesModel.objects.all().filter(categoria_id=categoria,estado='1')[:10]
		#data = serializers.serialize(
		#	"json",
		#	habilidadesModel.objects.all().filter(categoria_id=categoria,estado='1')[:10],
		#	fields = ('pk','nhabilidad','descripcion','val_promedio'),
		#	use_natural_foreign_keys = True,
		#)
		data = []
		for habilidad in habilidades:
			usuario = User.objects.get(id= habilidad.usuario_id)
			perfilusuario = perfilUsuarioModel.objects.get(usuario=usuario)
			item = {
				'user_id': usuario.id,
				'username': usuario.username,
				'userfirstname': usuario.first_name,
				'userlastname': usuario.last_name,
				'userphone': perfilusuario.celular1,
				'nhabilidad': habilidad.nhabilidad,
				'descripcion': habilidad.descripcion,
				'habilidad_id': habilidad.id,
				'habilidad_val':habilidad.val_promedio,
				'habilidad_nsol':habilidad.num_solicitudes,
			}
			data.append(item)

		return HttpResponse(
			json.dumps(data),
			content_type = "application/json"
		)

#Limpia el key 'Model' retornado por el serializador de Modelos
def cleanJsonModel(data):
	for d in data:
		del d['model']
	return data

def FindDetail(request):
	return render(request,'FindDetail.html')