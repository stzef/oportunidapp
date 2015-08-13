from django.db import models

class respuestasModel(models.Model):
	respuesta = models.CharField(max_length=1000)
	fecha = models.DateTimeField(auto_now=True)

	def __str__(self):
		return u'%s' % (self.respuesta)

	def __unicode__(self):
		return u'%s' % (self.respuesta)