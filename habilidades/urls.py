
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^habilidades/$','habilidades.views.habilidades',name='habilidades'),
	url(r'^habilidades/(?P<pk>[\w\-]+)/$','habilidades.views.detalle',name='detalle'),
	
	url(r'^nuevahabilidad/$','habilidades.views.nuevaHabilidad',name='nuevaHabilidad'),
	url(r'^listarhabilidades/$','habilidades.views.listHabilidadesActivas',name='listarHabilidades'),
	
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