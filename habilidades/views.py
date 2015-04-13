# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from serializers import habilidadesSerializer
from models import habilidadesModel
from forms import nuevaHabilidadForm
from permissions import IsOwnerOrReadOnly
from usuarios.models import perfilUsuarioModel

import json




@login_required()
def habilidades(request):
	user = request.user
	return render(request,'habilidades.html',{'user':user,'form': nuevaHabilidadForm})

def nuevaHabilidad(request):	
	if request.method == 'POST':
		form = nuevaHabilidadForm(request.POST)
		if form.is_valid():
			habilidad = form.save(commit=False)
			usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
			habilidad.usuario = usuario
			habilidad.save()
			return HttpResponse(
				json.dumps({'status':1,'message':'Habilidad agregada +'}),
				content_type="application/json"
			)

		else:
			#data_error = json.loads(form.errors.as_json())
			return HttpResponse(
				json.dumps({"massage":"Revisa que toda la información este bien"}),
				content_type="application/json"
			)











#from rest_framework.permissions import IsAuthenticated
#from rest_framework import viewsets


"""class habilidadesViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,) 
	def create(self, request):
		queryset = habilidades.objects.all()
		#return Response(request.data['nombre_habilidad'])
class habilidadesViewSet(viewsets.ModelViewSet):
	permission_classes = ( IsAuthenticated, IsOwnerOrReadOnly,)
	queryset = habilidadesModel.objects.all()
	serializer_class = habilidadesSerializer

	def perform_create(self, serializer):
		usuario = perfilUsuarioModel.objects.get(usuario_id=self.request.user)
		serializer.save(id_usuario=usuario)

	def list(self,request):
		queryset = habilidadesModel.objects.get(id=17)
		serializer = habilidadesSerializer
		return HttpResponse(serializer.data)

"""

