from django.db import models

from habilidades.models import habilidadesModel
from usuarios.models import perfilUsuarioModel

# Create your models here.
class teNecesitoModel(models.Model):
	usuarioSolicitante = models.ForeignKey(perfilUsuarioModel, related_name='solicitante')
	usuarioRequerido = models.ForeignKey(perfilUsuarioModel, related_name='requerido')
	habilidadSolicitada = models.ForeignKey(habilidadesModel)
	mensaje = models.CharField(max_length=200)
	fecha = models.DateTimeField(auto_now=True,null=False,blank=True)

