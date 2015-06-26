from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q

from habilidades.models import habilidadesModel, habCategoriasModel
from usuarios.models import perfilUsuarioModel

import json

# Create your views here.
def inicio(request):
	return render(request,'home.html')

def view_404(request):
	return render(request,'404.html')

def view_500(request):
	return render(request,'500.html')

# [buscarTemplate] View encargada de retornar el template de busquedas
def buscarTemplate(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categoria':TodasLasCategorias})

def buscarPrincipal(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscarP.html',{'categoria':TodasLasCategorias})

class detalleHabilidadBuscada(DetailView):
	model = habilidadesModel
	context_object_name = 'habilidad'
	template_name = 'busqueda.html'

	def getRecomendados(self, habilidad):
		recomendados = habilidadesModel.objects.filter(categoria=habilidad.categoria).exclude(id=habilidad.id)[:5]
		return recomendados

	def get_context_data(self, **kwargs):
		context = super(detalleHabilidadBuscada, self).get_context_data(**kwargs)
		recomendados = self.getRecomendados(context['object'])
		context['recomendados'] = recomendados
		return context

class busquedasListView(ListView):
	model = habilidadesModel
	paginador = 10

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()
		formato = self.request.GET.get('format', None)
		if formato == 'json':
			return self.json_to_response()
		context = self.get_context_data()
		return self.render_to_response(context)


	def get_queryset(self):
		categoriaBuscada = self.request.GET.get('categoria', None)
		fraseBuscada = self.request.GET.get('busqueda', None)
		orden = self.request.GET.get('orden', None)
		page = self.request.GET.get('page', None)
		limitePrimero = (int(page)-1)*self.paginador
		limiteUltimo = int(page)*self.paginador

		ordenOpciones = {
			'1': 'num_solicitudes',
			'2': 'val_promedio',
		}

		q = self.querysetPorDefecto()

		if categoriaBuscada is not None and categoriaBuscada != '':
			q = q.filter(categoria=categoriaBuscada)
		if fraseBuscada is not None and fraseBuscada != '':
			q = self.filtrarPorPalabras(q, fraseBuscada)
		if orden is not None and orden != '':
			q = q.order_by('-'+ordenOpciones[orden])
		return q[limitePrimero:limiteUltimo]

	def querysetPorDefecto(self):
		q = self.model.objects.filter(estado=True)
		return q

	def filtrarPorPalabras(self, q, fraseBuscada):
		dicFraseBuscada = fraseBuscada.split()
		for palabra in dicFraseBuscada:
			q = q.filter(
				Q(nhabilidad__contains=palabra) | Q(descripcion__contains=palabra)
			)
		return q

	def json_to_response(self):
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
				'foto':habilidad.foto.name,
			})
		return JsonResponse(data, safe=False)