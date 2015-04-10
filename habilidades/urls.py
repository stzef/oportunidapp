from django.conf.urls import patterns, include, url
from views import habilidadesViewSet


from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'habilidades', habilidadesViewSet, 'habilidades')

urlpatterns = patterns('',
	url(r'^api/', include(router.urls, namespace='api')),
	#url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
	#url(r'^habilidad/',habilidadesViewSet.as_view({'get': 'list'}),name='createhab'),
	url(r'^perfil/habilidades','habilidades.views.habilidades',name='habilidades'),
)