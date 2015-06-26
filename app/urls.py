from django.conf.urls import patterns, include, url
from app.views import busquedasListView,detalleHabilidadBuscada

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^404/$', 'app.views.view_404',name='404'),
    url(r'^500/$', 'app.views.view_500',name='500'),
    url(r'^buscar/$', 'app.views.buscarTemplate',name='buscar'),
    url(r'^buscar_/$', 'app.views.buscarPrincipal',name='buscar_'),
    url(r'^buscar/(?P<slug>[\w\-]+)/$',detalleHabilidadBuscada.as_view(), name='busqueda'),
	url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
	#url(r'^resultados/detalle/$', 'app.views.resultadosDetalle',name='resultados-detalle'),

)
