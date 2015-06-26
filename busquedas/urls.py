from django.conf.urls import patterns, include, url
from busquedas.views import *

urlpatterns = patterns('',
	url(r'^buscar/$', busquedasListView.as_view(),name='buscar'),
	url(r'^buscar/(?P<slug>[\w\-]+)/$',detalleHabilidadBuscada.as_view(), name='busqueda'),
    url(r'^buscar_/$', 'busquedas.views.buscarPrincipal',name='buscar_'),

	#url(r'^buscar/$', 'busquedas.views.buscarTemplate',name='buscar'),
	#url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
)
