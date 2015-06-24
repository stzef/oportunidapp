from habilidades.views import habilidadesListView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#url(r'^habilidades/$','habilidades.views.habilidadesViewTemplate',name='habilidades'),
	url(r'^habilidades/$',habilidadesListView.as_view(),name='habilidades'),
	url(r'^habilidades/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','habilidades.views.detalle',name='detalle'),
	url(r'^nuevahabilidad/$','habilidades.views.crearNuevaHabilidad',name='nuevaHabilidad'),
	
	
	url(r'^fotohabilidad/$','habilidades.views.cambiarFotoHabilidad',name='fotoHabilidad'),
	url(r'^desactivarhabilidad/$','habilidades.views.desactivarHabilidad',name='desactivarHabilidad'),
	url(r'^activarhabilidad/$','habilidades.views.activarHabilidad',name='activarHabilidad'),
	url(r'^editarhabilidad/$','habilidades.views.editarHabilidad',name='editarHabilidad'),
	url(r'^habilidades-activas/$','habilidades.views.listarHabilidadesActivas',name='habilidadesActivas'),
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