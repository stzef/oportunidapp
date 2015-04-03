from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class perfilUsuarioModel(models.Model):

	GENERO_OPCIONES = (
		('M','Masculino'),
		('F','Femenino'),
		('O','Otro'),
	)
	usuario = models.OneToOneField(User,primary_key=True)
	cedula = models.IntegerField(max_length=20,blank=True,null=True)
	genero = models.CharField(max_length=15,choices=GENERO_OPCIONES,default='Masculino')
	fnacimiento = models.DateField(blank=True,null=True)
	celular1 = models.IntegerField(max_length=15,blank=True,null=True)
	celular2 = models.IntegerField(max_length=15,blank=True,null=True)
	celular3 = models.IntegerField(max_length=15,blank=True,null=True)

	def __str__(self):
		return u'%s' % (self.usuario)
