from django.conf.urls import patterns, include, url
from busquedas.views import *

urlpatterns = patterns('',

	url(r'^buscar/$', 'busquedas.views.buscarView',name='buscar'),
	url(r'^(?P<slug>[\w\-]+)/$', busquedasListView.as_view(),name='busqueda'),
	url(r'^buscar/(?P<slug>[\w\-]+)/$',detalleHabilidadBuscada.as_view(), name='detallebusqueda'),

	#url(r'^buscar/$', 'busquedas.views.buscarTemplate',name='buscar'),
	#url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
)
