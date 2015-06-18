# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User


from habilidades.models import habilidadesModel
from usuarios.models import perfilUsuarioModel
from necesito.models import teNecesitoModel

# Create your views here.
def necesito(request):
	return render(request,'necesito.html')

#@login_required()	
def teNecesito(request, usuarioSolicitado, habilidadSlug):
	usuario = get_object_or_404(User, username=usuarioSolicitado)
	perfil = perfilUsuarioModel.objects.get(usuario = usuario)
	habilidadSolicitada = get_object_or_404(habilidadesModel, slug=habilidadSlug, usuario=perfil)

	context = {
		'usuario' : usuario,
		'habilidad' : habilidadSolicitada,
	}

	return render(request,'te_necesito.html', context)

def crearMensajeSolicitud(request):
	if request.method == "POST":
		usuarioSolicitante = perfilUsuarioModel.objects.get(usuario=request.user.id)
		usuarioRequerido = perfilUsuarioModel.objects.get(usuario=request.POST['usuarioRequerido'])
		habilidadSolicitada = habilidadesModel.objects.get(id=request.POST['habilidadSolicitada'])
		mensaje = request.POST['mensaje']

		necesitoSolicitud = teNecesitoModel(
			usuarioSolicitante = usuarioSolicitante,
			usuarioRequerido = usuarioRequerido,
			habilidadSolicitada = habilidadSolicitada,
			mensaje = mensaje,
		)

		necesitoSolicitud.save()

		return HttpResponse(necesitoSolicitud)

