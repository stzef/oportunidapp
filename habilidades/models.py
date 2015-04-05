from django.db import models
from usuarios.models import perfilUsuarioModel

class habCategoriasModel(models.Model):
	categoria = models.CharField(max_length=30,blank=False,null=False)

	def __str__(self):
		return u'%s' % (self.categoria)

class habilidadesModel(models.Model):
	ESTADO_OPCIONES = (
		('1','Activo'),
		('2','Inactivo'),
		('3','Eliminado'),
	)

	id_usuario = models.ForeignKey(perfilUsuarioModel)
	id_categoria = models.ForeignKey(habCategoriasModel)
	nhabilidad = models.CharField(max_length=30,blank=False,null=False)
	descripcion = models.CharField(max_length=250,blank=False,null=False)
	#foto = models.ImageField(upload_to="/")
	val_promedio = models.IntegerField(blank=True,null=True)
	num_solicitudes = models.IntegerField(blank=True,null=True)
	estado = models.CharField(choices=ESTADO_OPCIONES,max_length=1,blank=False,null=False,default='Activo')
	precio = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)

	def __str__(self):
		return u'%s' % (self.nhabilidad)
