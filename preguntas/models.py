from django.db import models


from usuarios.models import perfilUsuarioModel
from habilidades.models import habilidadesModel
from respuestas.models import respuestasModel


class preguntasModel(models.Model):

	pregunta = models.CharField(max_length=1000,null=False,blank=False)
	fecha = models.DateTimeField(auto_now=True,null=False,blank=False)
	estado = models.BooleanField(default=True,null=False,blank=False)
	habilidad = models.ForeignKey(habilidadesModel)
	respuesta = models.ForeignKey(respuestasModel,null=True,blank=True)
	ofertante = models.ForeignKey(perfilUsuarioModel, related_name='ofertante')
	solicitante = models.ForeignKey(perfilUsuarioModel, related_name='solicitante')


	def __str__(self):
		return u'%s' % (self.pregunta)

	def __unicode__(self):
		return u'%s' % (self.categoria)