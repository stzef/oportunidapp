from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^perfil/habilidades','habilidades.views.habilidades',name='habilidades'),
	url(r'^habilidades/nueva','habilidades.views.nuevaHabilidad',name='nuevaHabilidad')
)







#from views import habilidadesViewSet
#from rest_framework import routers
#router = routers.DefaultRouter()
#router.register(r'habilidades', habilidadesViewSet, 'habilidades')
#url(r'^api/', include(router.urls, namespace='api')),
#url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
#url(r'^habilidad/',habilidadesViewSet.as_view({'get': 'list'}),name='createhab'),