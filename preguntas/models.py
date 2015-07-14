from django.db import models
from usuarios.models import perfilUsuarioModel
from habilidades.models import habilidadesModel

class preguntasModel(models.Model):

	pregunta = models.CharField(max_length=1000,null=False,blank=False)
	fecha = models.DateTimeField(auto_now=True,null=False,blank=False)
	estado = models.BooleanField(default=True)
	habilidad = models.ForeignKey(habilidadesModel)
	ofertante = models.ForeignKey(perfilUsuarioModel)
	solicitante = models.ForeignKey(perfilUsuarioModel)

	def __str__(self):
		return u'%s' % (self.pregunta)
