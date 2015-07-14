from django.db import models

from preguntas.models import preguntasModel

class respuestasModel(models.Model):
	respuesta = models.CharField(max_length=1000)
	fechas = models.DateTimeField(auto_now=True)
	pregunta = models.ForeignKey(preguntasModel)


	def __str__(self):
		return u'%s' % (self.respuesta)