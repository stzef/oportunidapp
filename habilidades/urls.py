
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^habilidades/$','habilidades.views.habilidadesViewTemplate',name='habilidades'),
	#url(r'^habilidades/(?P<pk>[\w\-]+)/$','habilidades.views.detalle',name='detalle'),

	url(r'^habilidades/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','habilidades.views.detalle',name='detalle'),


	url(r'^fotohabilidad/$','habilidades.views.cambiarFotoHabilidad',name='fotoHabilidad'),
	url(r'^desactivarhabilidad/$','habilidades.views.desactivarHabilidad',name='desactivarHabilidad'),
	url(r'^activarhabilidad/$','habilidades.views.activarHabilidad',name='activarHabilidad'),

	#Crear Habilidad
	url(r'^nuevahabilidad/$','habilidades.views.crearNuevaHabilidad',name='nuevaHabilidad'),

	#Editar Habilidad
	url(r'^editarhabilidad/$','habilidades.views.editarHabilidad',name='editarHabilidad'),

	#Listar Habilidades Activas
	url(r'^habilidades-activas/$','habilidades.views.listarHabilidadesActivas',name='habilidadesActivas'),

	#Listar Habilidades No Activas
	url(r'^habilidades-no-activas/$','habilidades.views.listarHabilidadesNoActivas',name='habilidadesNoActivas'),
	url(r'^categoriaslistar/$','habilidades.views.categoriasListar',name='categoriasListar'),

)







#from views import habilidadesViewSet
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'habilidades', habilidadesViewSet, 'habilidades')
#url(r'^api/', include(router.urls, namespace='api')),
#url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#url(r'^habilidad/',habilidadesViewSet.as_view({'get': 'list'}),name='createhab'),