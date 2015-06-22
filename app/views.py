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

# [buscarTemplate] View encargada de retornar el template de busquedas
def buscarTemplate(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categoria':TodasLasCategorias})

def detalleHabilidadBuscada(request,slug,pk):
	try:
		habilidadBuscada = habilidadesModel.objects.get(slug=slug, pk=pk)
	except ObjectDoesNotExist:
		habilidadBuscada = get_object_or_404(habilidadesModel,pk=pk)

	usuario = User.objects.get(id= habilidadBuscada.usuario_id)
	perfilusuario = perfilUsuarioModel.objects.get(usuario=usuario)

	contexto = {
		'habilidad' : habilidadBuscada,
		'perfil': perfilusuario,
		'usuario': usuario,
	}

	return render(request,'busqueda.html', contexto)

#[BusquedasListView] recibe parametros de busqueda de habilidades y retorna json con resultados
class busquedasListView(ListView):
	model = habilidadesModel

	'''Se ejecuta al momento de realizar una peticion tipo GET a la url'''
	def get(self, request, *args, **kwargs):

		self.object_list = self.get_queryset()

		formato = self.request.GET.get('format', None)
		if formato == 'json':
			return self.json_to_response()

		context = self.get_context_data()
		return self.render_to_response(context)

	#Funcion de busqueda de elemento en la DB
	def get_queryset(self):
		#Parametros Recibidos
		categoriaBuscada = self.request.GET.get('categoria', None)
		fraseBuscada = self.request.GET.get('busqueda', None)
		orden = self.request.GET.get('orden', None)

		#orden = self.obtenerOrdenDeConsulta(self.request.GET.get('sort', None))

		ordenOpciones = {
			'1': 'num_solicitudes',
			'2': 'val_promedio',
		}

		q = self.querysetPorDefecto()

		#Proceso de Consulta
		if categoriaBuscada is not None and categoriaBuscada != '':
			q = q.filter(categoria=categoriaBuscada)
		if fraseBuscada is not None and fraseBuscada != '':
			q = self.filtrarPorPalabras(q, fraseBuscada)
		if orden is not None and orden != '':
			q = q.order_by('-'+ordenOpciones[orden])
		return q

#	def obtenerOrdenDeConsuta(self, criterioDeOrden):
#		if criterioDeOrden is not None:
#			#Proceso
#		else:
#			return None

	def querysetPorDefecto(self):
		#Consulta por defecto
		q = self.model.objects.filter(estado=True)
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
				'habilidad_id': habilidad.id,
				'nhabilidad': habilidad.nhabilidad,
				'slug': habilidad.slug,
				'descripcion': habilidad.descripcion,
				'habilidad_id': habilidad.id,
				'habilidad_val':habilidad.val_promedio,
				'habilidad_nsol':habilidad.num_solicitudes,
				'foto':perfilusuario.foto.name,
			})
		return JsonResponse(data, safe=False)