# -*- encoding: utf-8 -*-
#importaciones dede Django
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#importaciones desde Aplicacion
from habilidades.models import habilidadesModel
from preguntas.models import preguntasModel
from usuarios.models import perfilUsuarioModel
#importaciones desde python


#View encargada de registrar una pregunta a un ofertante
#request en AJAX response en JSON
@csrf_exempt
def preguntanueva(request):
	if request.is_ajax():
		# recibe parametros
		habilidadPreguntada = habilidadesModel.objects.get(pk=request.POST['habilidad'])
		descripcionPregunta = request.POST['pregunta']
		solicitante = perfilUsuarioModel.objects.get(pk=request.user.id)

		# crear pregunta
		pregunta = preguntasModel(
			pregunta = descripcionPregunta,
			habilidad = habilidadPreguntada,
			ofertante = habilidadPreguntada.usuario,
			solicitante = solicitante,
		)

		# guardar pregunta
		pregunta.save()
		# enviar email de notificacion
		pregunta.enviar_pregunta_email()

		# respuesta
		return JsonResponse(
			{
				'estado': 1,
				'pregunta': pregunta.pregunta,
				'mensaje': 'Listo hemos enviado tu pregunta, te avisaremos con un email cuando respondan.',
			},
			safe= False,
		)
