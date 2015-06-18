# -*- encoding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User


from habilidades.models import habilidadesModel
from necesito.forms import teNecesitoForm
from usuarios.models import perfilUsuarioModel

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
	return HttpResponse(request)
