# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User

#Importaciones desde Aplicacion [Oportunidad]
from habilidades.models import habilidadesModel
from usuarios.models import perfilUsuarioModel
from necesito.models import teNecesitoModel
from necesito.forms import teNecesitoForm

# Create your views here.
@login_required()
def necesito(request):
	necesitos = teNecesitoModel.objects.filter(usuarioRequerido=request.user.id).order_by('-fecha')
	contexto = {
		'necesito' : necesitos,
	}
	return render(request,'necesito.html', contexto)

@login_required()	
def teNecesito(request, usuarioSolicitado, habilidadSlug):
	usuario = get_object_or_404(User, username=usuarioSolicitado)
	perfil = perfilUsuarioModel.objects.get(usuario = usuario)
	habilidadSolicitada = get_object_or_404(habilidadesModel, slug=habilidadSlug, usuario=perfil)

	context = {
		'usuario' : usuario,
		'habilidad' : habilidadSolicitada,
		'perfil': perfil,
	}

	return render(request,'te_necesito.html', context)

def crearMensajeSolicitud(request):
	if request.method == "POST":
		form = teNecesitoForm(request.POST or None)
		respuesta = {}
		if form.is_valid():
			form.save()
			respuesta['estado'] = 1
			respuesta['mensaje'] = 'El mensaje ha sido enviado'
		else:
			respuesta['estado'] = 0
			respuesta['mensaje'] = 'Lo sentimos en este momento no se puede enviar el mensaje'

		return JsonResponse(respuesta, safe=False)
