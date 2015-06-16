from django.conf.urls import patterns, include, url
from app.views import busquedasListView


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^buscar/$', 'app.views.buscarTemplate',name='buscar'),
	url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
	url(r'^resultados/detalle/$', 'app.views.resultadosDetalle',name='resultados-detalle'),
)
