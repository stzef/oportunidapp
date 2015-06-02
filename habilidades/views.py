# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404


#Importaciones desde Aplicacion [Oportunidad]
from serializers import habilidadesSerializer
from models import habilidadesModel, habCategoriasModel
from forms import nuevaHabilidadForm
from usuarios.models import perfilUsuarioModel
from app.views import cleanJsonModel


#Importaciones desde Python
import json


#[habilidadesViewTemplate] View enacargada de retornar el template de habilidades
@login_required()
def habilidadesViewTemplate(request):
	user = request.user
	contexto = {
		'user':user,
		'form': nuevaHabilidadForm,
	}
	return render(request,'habilidades.html',contexto)


#[crearNuevaHabilidad] View (funcion) encargada de recibir datos para crear nueva habilidad de un usuario
""" Pendiente datos de respuesta al frontend con estado y mensage de aceptacion o negacion"""
@login_required()
def crearNuevaHabilidad(request):	
	if request.method == "POST":
		form = nuevaHabilidadForm(request.POST)
		if form.is_valid():
			response_data = {}

			habilidadNueva = form.save(commit=False)
			usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
			habilidadNueva.usuario = usuario
			habilidadNueva.save()

			response_data['pk'] = habilidadNueva.pk

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)

		else:
			data_error = json.loads(form.errors.as_json())
			return HttpResponse(
				json.dumps(data_error),
				content_type="application/json"
			)

#[detalleHabilidadView] View encargada de retornar template del detalle de una habilidad
@login_required()
def detalle(request,pk):
	habilidadBuscada = get_object_or_404(habilidadesModel,id=pk)
	templateRespuesta = 'no_permitido.html'
	form = nuevaHabilidadForm(instance=habilidadBuscada)

	if habilidadBuscada.usuario_id == request.user.id:
		templateRespuesta = 'detalle.html'
		contexto = {
			'habilidad': habilidadBuscada,
			'form' : form,
		}
		return render(request,templateRespuesta, contexto)
	return render(request,templateRespuesta)

#[editarHabilidad] View encargada editar una habilidad
@login_required()
def editarHabilidad(request):
	if request.method == "POST":
		form = nuevaHabilidadForm(request.POST or None)
		if form.is_valid():
			habilidadParaEditar = habilidadesModel.objects.get(id=request.POST['id'])
			response_data = {}
			if habilidadParaEditar.usuario_id == request.user.id:
				habilidadParaEditar.nhabilidad = request.POST['nhabilidad']
				habilidadParaEditar.descripcion = request.POST['descripcion']
				habilidadParaEditar.precio = request.POST['precio']
				habilidadParaEditar.save(update_fields=['nhabilidad','descripcion','precio'])

				response_data['message'] = 'Edición exitosa'
				return HttpResponse(
					json.dumps(response_data),
					content_type="application/json"
				)
			else:
				return render(request,'no_permitido.html')
		else:
			response_data['message'] = 'error formulario'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)


#[desactivarHabilidad] View encargada desactivar una habilidad
@login_required()
def desactivarHabilidad(request):
	if request.is_ajax() and request.method == "POST":
		habilidad_id = request.POST['habilidad_id']
		habilidadPorDesactivar = get_object_or_404 (habilidadesModel,id = habilidad_id)
		if habilidadPorDesactivar.usuario_id == request.user.id:
			response_data = {}
			habilidadPorDesactivar.estado = False
			habilidadPorDesactivar.save(update_fields=["estado"])

			response_data['message'] = 'Habilidad activada'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)


		else:
			return render(request,'no_permitido.html')
	else:
		return render(request,'no_permitido.html')

@login_required()
def activarHabilidad(request):
	if request.is_ajax() and request.method == "POST":
		habilidad_id = request.POST['habilidad_id']
		habilidadPorActivar = get_object_or_404 (habilidadesModel,id = habilidad_id)
		if habilidadPorActivar.usuario_id == request.user.id:
			response_data = {}
			habilidadPorActivar.estado = True
			habilidadPorActivar.save(update_fields=["estado"])

			response_data['message'] = 'Habilidad activada'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)

		else:
			return render(request,'no_permitido.html')
	else:
		return render(request,'no_permitido.html')

#Listar Habilidades activas del usuario request POST return JSON
@login_required()
def listarHabilidadesActivas(request):
	if request.method == 'GET':
		data = serializers.serialize(
			"json",
			habilidadesModel.objects.all().filter(usuario_id=request.user.id,estado=True).order_by('-fecha_creacion'),
			fields = ('pk','categoria','nhabilidad','foto','descripcion','val_promedio','num_solicitudes','precio'),
			use_natural_foreign_keys=True,
		)

		data_response = cleanJsonModel(json.loads(data))

		return HttpResponse(
			json.dumps(data_response),
			content_type = "application/json"
		)

#Listar Habilidades No Activas del usuario request POST return JSON
@login_required()
def listarHabilidadesNoActivas(request):
	if request.method == 'GET':
		data = serializers.serialize(
			"json",
			habilidadesModel.objects.all().filter(usuario_id=request.user.id,estado=False).order_by('-fecha_creacion'),
			fields = ('pk','categoria','nhabilidad','foto','descripcion','val_promedio','num_solicitudes','precio'),
			use_natural_foreign_keys = True,
		)
		data_response = cleanJsonModel(json.loads(data))
		return HttpResponse(
			json.dumps(data_response),
			content_type = "application/json"
		)

@csrf_exempt
@login_required
def cambiarFotoHabilidad(request):
	habilidad = habilidadesModel.objects.get(id=request.POST['habilidad'])
	foto = request.FILES['foto']

	foto.name = habilidad.nhabilidad.replace(' ','_')+str(habilidad.id)
	#Metodo borrar imagen anterior

	if habilidad.usuario_id == request.user.id:
		habilidad.foto = foto
		habilidad.save(update_fields=["foto"])

	response_data = {}
	response_data['message'] = 'OK !!!!'
	
	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
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