from django.conf.urls import patterns, include, url
from app.views import busquedasListView


urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^buscar/$', 'app.views.busquedasViewTemplate',name='buscar'),
    url(r'^buscar/(?P<pk>[\w\-]+)/$', 'app.views.findDetail',name='findDetail'),
	url(r'^resultados/$', busquedasListView.as_view(),name='resultados'),
)
