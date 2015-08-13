from django.shortcuts import render
from django.http import JsonResponse


from respuestas.models import respuestasModel
from preguntas.models import preguntasModel
from app.utilidades import get_or_none




def crearRespuesta(request):
	if request.is_ajax():
		pregunta_id = request.POST['pregunta']
		respuesta   = request.POST['respuesta']
		pregunta = get_or_none(preguntasModel, id=pregunta_id)

		nuevaRespuesta = respuestasModel(respuesta=respuesta)
		nuevaRespuesta.save()

		if pregunta is not None:
			pregunta.respuesta = nuevaRespuesta

		mensaje = ''


		return JsonResponse(
			{
				'mensaje': mensaje,
			},
			safe = False,

		)
