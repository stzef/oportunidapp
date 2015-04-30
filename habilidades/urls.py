from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^habilidad/','habilidades.views.habilidades',name='habilidades'),
	url(r'^habilidades/detalle/','habilidades.views.detalle',name='detalle'),
	url(r'^habilidades/nueva/','habilidades.views.nuevaHabilidad',name='nuevaHabilidad'),
	url(r'^habilidades/list/','habilidades.views.listHabilidadesActivas',name='listarHabilidades'),
)







#from views import habilidadesViewSet
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'habilidades', habilidadesViewSet, 'habilidades')
#url(r'^api/', include(router.urls, namespace='api')),
#url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#url(r'^habilidad/',habilidadesViewSet.as_view({'get': 'list'}),name='createhab'),