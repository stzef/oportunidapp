from django.db import models
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

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

	def enviar_pregunta_email(self):

		#datos para renderizar el template de email
		contextoDeTemplateParaEmail = {
			'solicitante' : self.solicitante.usuario.get_full_name(),
			'pregunta' : self.pregunta,
		}

		template = render_to_string('pregunta_email_template.html', contextoDeTemplateParaEmail)

		#creando mensaje
		msg = EmailMessage(
			subject = 'Oportunidapp (pregunta)',
			from_email = 'sistematizaref <sistematizaref@gmail.com>',
			to = [self.ofertante.usuario.email]
		)

		msg.template_name = 'Bienvenida'
		msg.template_content = {
			'std_content00' : template,
		}

		msg.send()

	def __str__(self):
		return u'%s' % (self.pregunta)

	def __unicode__(self):
		return u'%s' % (self.categoria)


