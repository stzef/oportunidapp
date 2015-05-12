# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404


from serializers import habilidadesSerializer
from models import habilidadesModel, habCategoriasModel
from forms import nuevaHabilidadForm
from usuarios.models import perfilUsuarioModel


from app.views import cleanJsonModel
import json


#Servir Template
@login_required()
def habilidades(request):
	user = request.user
	#habilidades = habilidadesModel.objects.filter(usuario_id=user.id).order_by('-fecha_creacion')
	return render(request,'habilidades.html',{'user':user,'form': nuevaHabilidadForm,'habilidades':habilidades})

@login_required
def detalle(request,pk):
	habilidad = get_object_or_404(habilidadesModel,id=pk)
	return render(request,'detalle.html',{'habilidad': habilidad})

#Crear nueva Habilidad request POST return JSON
@login_required()
def nuevaHabilidad(request):	
	if request.method == 'POST':
		form = nuevaHabilidadForm(request.POST, request.FILES)
		if form.is_valid():
			response_data = {}
			habilidad = form.save(commit=False)
			usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
			habilidad.usuario = usuario
			habilidad.save()

			response_data['pk'] = habilidad.pk
			return HttpResponse(
				#json.dumps({'status':1,'message':'Habilidad agregada +'}),
				json.dumps(response_data),
				content_type="application/json"
			)

		else:
			data_error = json.loads(form.errors.as_json())
			return HttpResponse(
				json.dumps(data_error),
				content_type="application/json"
			)

#Listar Habilidades activas del usuario request POST return JSON
@login_required()
def listHabilidadesActivas(request):
	if request.method == 'GET':
		data = serializers.serialize(
			"json",
			habilidadesModel.objects.all().filter(usuario_id=request.user.id).order_by('-fecha_creacion'),
			fields = ('pk','categoria','nhabilidad','foto','descripcion','val_promedio','num_solicitudes','precio'),
			use_natural_foreign_keys=True,
		)

		data_response = cleanJsonModel(json.loads(data))

		return HttpResponse(
			json.dumps(data_response),
			content_type = "application/json"
		)


#Listar Categorias
def categoriasListar(request):
	if request.method == "GET":
		data = serializers.serialize(
			"json",
			habCategoriasModel.objects.all().order_by('categoria'),
			fields = ('pk','categoria'),
		)

		data_response = cleanJsonModel(json.loads(data))

		return HttpResponse(
			json.dumps(data_response),
			content_type = "application/json"
		)






#from rest_framework.permissions import IsAuthenticated
#from rest_framework import viewsets
#from permissions import IsOwnerOrReadOnly


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

