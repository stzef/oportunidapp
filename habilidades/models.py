from django.db import models
from usuarios.models import perfilUsuarioModel


class habCategoriasModelManager(models.Manager):
	def get_by_natural_key(self, categoria):
		return self.get(categoria=categoria)

class habCategoriasModel(models.Model):
	categoria = models.CharField(max_length=30,blank=False,null=False)
	objects = habCategoriasModelManager()
	def __str__(self):
		return u'%s' % (self.categoria)

	def natural_key(self):
		return (self.categoria)

class habilidadesModel(models.Model):
	#ESTADO_OPCIONES = (
	#	('1','Activo'),
	#	('2','Inactivo'),
	#	('3','Eliminado'),
	#)
	usuario = models.ForeignKey(perfilUsuarioModel)
	categoria = models.ForeignKey(habCategoriasModel)
	nhabilidad = models.CharField(max_length=30,blank=False,null=False)
	descripcion = models.CharField(max_length=250,blank=False,null=False)
	foto = models.ImageField(upload_to="habilidades/img/",blank=True,null=True, default="habilidades/img/no_image.png")
	val_promedio = models.IntegerField(blank=True,null=True)
	num_solicitudes = models.IntegerField(blank=True,null=True,default=0)
	estado = models.BooleanField(default=True)
	#estado = models.CharField(choices=ESTADO_OPCIONES,max_length=1,blank=False,null=False,default='1')
	precio = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
	fecha_creacion =  models.DateTimeField(auto_now=True,null=False,blank=True)

	def __str__(self):
		return u'%s' % (self.nhabilidad)
