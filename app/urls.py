from django.conf.urls import patterns, include, url
from app.views import busquedasListView, detalleHabilidadBuscada


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^buscar/$', 'app.views.buscarTemplate',name='buscar'),
    url(r'^buscar/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','app.views.detalleHabilidadBuscada', name='busqueda'),
	url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
	#url(r'^resultados/detalle/$', 'app.views.resultadosDetalle',name='resultados-detalle'),
)
