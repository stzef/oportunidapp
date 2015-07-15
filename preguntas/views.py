# -*- encoding: utf-8 -*-
#importaciones dede Django
from django.shortcuts import render


#importaciones desde Aplicacion
from habilidades.models import habilidadesModel

#importaciones desde python



#View encargada de registrar una pregunta a un ofertante
#request en AJAX response en JSON
def hacerPregunta(request):
	if request.is_ajax():
		habilidadPreguntada = habilidadesModel.objects.get(pk=request.POST['habilidad'])
		descripcionPregunta = request.POST['pregunta']

