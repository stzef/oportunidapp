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

#def buscarTemplate(request):
#	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
#	return render(request,'buscar.html',{'categoria':TodasLasCategorias})

class detalleHabilidadBuscada(DetailView):
	model = habilidadesModel
	context_object_name = 'habilidad'
	template_name = 'busqueda.html'

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
	paginate_by = 2
	template_name = 'buscar.html'
	context_object_name = 'habilidades'

	def get_template_names(self):
		inicio = self.request.GET.get('inicio')
		if inicio == 'true':
			return 'buscares.html'
		else:
			return self.template_name

	def get_queryset(self):
		return self.model.objects.filter(estado=True)

	def get_context_data(self, **kwargs):
		context = super(busquedasListView, self).get_context_data(**kwargs)
		context['categorias'] = habCategoriasModel.objects.all()
		context['queryString'] = self.request.META['QUERY_STRING'] 
		return context
		
def buscarPrincipal(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscarP.html',{'categoria':TodasLasCategorias})