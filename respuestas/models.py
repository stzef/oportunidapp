from django.db import models
from django.core.mail import EmailMessage

#from preguntas.models import preguntasModel

class respuestasModel(models.Model):

	#pregunta = models.OneToOneField(preguntasModel)
	respuesta = models.CharField(max_length=1000)
	fecha = models.DateTimeField(auto_now=True)


	def enviar_respuesta_email(self, usuario):
		msg = EmailMessage(
			subject = 'Oportunidapp (pregunta)',
			from_email = 'sistematizaref <sistematizaref@gmail.com>',
			to = [usuario.email]
		)
		msg.template_name = 'Bienvenida'
		msg.template_content = {
			'std_content00' : '<h2> Mensaje para enviar respuesta</h2>',
		}
		msg.send()


	def __str__(self):
		return u'%s' % (self.respuesta)

	def __unicode__(self):
		return u'%s' % (self.respuesta)


