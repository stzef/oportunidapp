
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^habilidades/$','habilidades.views.habilidadesViewTemplate',name='habilidades'),
	url(r'^habilidades/(?P<pk>[\w\-]+)/$','habilidades.views.detalle',name='detalle'),
	url(r'^desactivarhabilidad/$','habilidades.views.desactivarHabilidad',name='desactivarHabilidad'),

	url(r'^nuevahabilidad/$','habilidades.views.crearNuevaHabilidad',name='nuevaHabilidad'),

	#Listar Habilidades Activas
	url(r'^habilidades-activas/$','habilidades.views.listarHabilidadesActivas',name='habilidadesActivas'),

	#Listar Habilidades No Activas
	url(r'^habilidades-no-activas/$','habilidades.views.listarHabilidadesNoActivas',name='habilidadesNoActivas'),


	url(r'^categoriaslistar/$','habilidades.views.categoriasListar',name='categoriasListar'),
	url(r'^personaslistar$','app.views.personasListar',name='personasListar'),

)







#from views import habilidadesViewSet
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'habilidades', habilidadesViewSet, 'habilidades')
#url(r'^api/', include(router.urls, namespace='api')),
#url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#url(r'^habilidad/',habilidadesViewSet.as_view({'get': 'list'}),name='createhab'),