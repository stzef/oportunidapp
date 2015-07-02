# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q

#Importaciones desde Aplicacion [Oportunidad]
from habilidades.models import habilidadesModel, habCategoriasModel
from usuarios.models import perfilUsuarioModel

#Importaciones desde Python
import json


class detalleHabilidadBuscada(DetailView):
	model = habilidadesModel
	context_object_name = 'habilidad'
	template_name = 'busqueda_detalle.html'


	def getRecomendados(self, habilidad):
		recomendados = habilidadesModel.objects.filter(categoria=habilidad.categoria).exclude(id=habilidad.id).order_by('-val_promedio')[:3]
		return recomendados


	def get_context_data(self, **kwargs):
		context = super(detalleHabilidadBuscada, self).get_context_data(**kwargs)
		recomendados = self.getRecomendados(context['object'])
		context['recomendados'] = recomendados
		return context

class busquedasListView(ListView):

	model = habilidadesModel
	paginate_by = 4
	template_name = 'busqueda.html'
	context_object_name = 'habilidades'
	ordering = '-val_promedio'

	ordenList = [
		('','-val_promedio','Mas valoradas'),
		('PRECIO_DESC','-precio','Mayor precio'),
		('PRECIO','precio','Menor precio'),
	]


	def get_template_names(self):
		inicio = self.request.GET.get('inicio')
		if inicio == 'true':
			return 'buscares.html'
		else:
			return self.template_name


	def get_elemento_busqueda(self, indice):
		i = 0
		for a,b,c in self.ordenList:
			if a == indice:	
				return self.ordenList[i]
			i += 1


	def get_ordering(self):
		orden = self.request.GET.get('orden')
		if orden is not None:
			item = self.get_elemento_busqueda(orden)
			return item [1]
		else:
			return self.ordering


	def get_orden_actual(self):
		orden = self.request.GET.get('orden')
		if orden is not None:
			item = self.get_elemento_busqueda(orden)
			return item
		else:
			return self.ordenList[0]

	def query_por_palabra(self, queryset, busqueda):

		#proceso
		return queryset

	def get_queryset(self):
		categoria = habCategoriasModel.objects.get(slug=self.kwargs['slug'])
		queryset = self.model.objects.filter(estado=True,categoria=categoria)

		busqueda = self.request.GET.get('q')
		if busqueda is not None:
			queryset = self.query_por_palabra(queryset, busqueda)

		ordering = self.get_ordering()

		if ordering:
			queryset = queryset.order_by(ordering)

		return queryset


	def get_context_data(self, **kwargs):

		context = super(busquedasListView, self).get_context_data(**kwargs)
		categoria = habCategoriasModel.objects.get(slug=self.kwargs['slug'])
		ordenItem = self.get_orden_actual()
		busqueda = self.request.GET.get('q')

		if busqueda is not None:
			busqueda = busqueda.replace(' ','+')

		context['categoria'] 	= categoria
		context['ordenList'] 	= self.ordenList
		context['ordenActual']  = ordenItem[2]
		context['orden'] 		= ordenItem[0]
		context['busqueda']		= busqueda
		context['page'] 		= self.request.GET.get('page')

		return context


def buscarView(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categorias':TodasLasCategorias})