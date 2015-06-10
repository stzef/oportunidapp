from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.db.models import Q

from habilidades.models import habilidadesModel, habCategoriasModel
from usuarios.models import perfilUsuarioModel

import json

# Create your views here.
def inicio(request):
	return render(request,'home.html')

# [busquedasViewTemplate] View encargada de retornar el template de busquedas
def busquedasViewTemplate(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categoria':TodasLasCategorias})
	#return HttpResponse(request.GET.get('estado'))

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
				'foto':perfilusuario.foto.name,
			}
			data.append(item)

		return HttpResponse(
			json.dumps(data),
			content_type = "application/json"
		)

def findDetail(request,pk):
	habilidad = get_object_or_404(habilidadesModel,id=pk)
	usuario = User.objects.get(id=habilidad.usuario_id)
	perfil_usuario = perfilUsuarioModel.objects.get(usuario=usuario)
	return render(request,'FindDetail.html',{'habilidad':habilidad, 'usuario':usuario, 'perfil':perfil_usuario})



#Limpia el key 'Model' retornado por el serializador de Modelos
def cleanJsonModel(data):
	for d in data:
		del d['model']
	return data


class busquedasListView(ListView):

	model = habilidadesModel
	template_name = "busquedas_sprike.html"
	paginate_by = 1

	def get(self, request, *args, **kwargs):

		self.object_list = self.get_queryset()
		formato = self.request.GET.get('format', None)
		if formato == 'json':
			return self.json_to_response()
		context = self.get_context_data()

		return self.render_to_response(context)

	def get_queryset(self):

		#Parametros Recibidos
		categoriaBuscada = self.request.GET.get('categoria', None)
		fraseBuscada = self.request.GET.get('busqueda', None)
		orden = self.request.GET.get('orden', None)

		#orden = self.obtenerOrdenDeConsulta(self.request.GET.get('sort', None))

		#Consulta por defecto
		q = self.querysetPorDefecto()

		#Proceso de Consulta
		if categoriaBuscada is not None and categoriaBuscada != '':
			q = self.model.objects.filter(categoria=categoriaBuscada)
		if fraseBuscada is not None:
			q = self.filtrarPorPalabras(q, fraseBuscada)
		if orden is not None:
			q = q.order_by('-'+orden)

		return q

#	def obtenerOrdenDeConsuta(self, criterioDeOrden):
#		if criterioDeOrden is not None:
#			#Proceso
#		else:
#			return None

	def querysetPorDefecto(self):
		#Consulta por defecto
		q = self.model.objects.all()
		return q

	def filtrarPorPalabras(self, q, fraseBuscada):
		#Recorre la frase a buscar palabra a palabra y filtra
		dicFraseBuscada = fraseBuscada.split()
		for palabra in dicFraseBuscada:
			q = q.filter(
				Q(nhabilidad__contains=palabra) | Q(descripcion__contains=palabra)
			)
		return q

	def json_to_response(self):
		#Respuesta en Json Format
		data = []
		for habilidad in self.object_list:
			usuario = User.objects.get(id= habilidad.usuario_id)
			perfilusuario = perfilUsuarioModel.objects.get(usuario=usuario)
			data.append({
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
				'foto':perfilusuario.foto.name,
			})
		return JsonResponse(data, safe=False)

