from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^buscar/$', 'app.views.busquedasViewTemplate',name='buscar'),
    url(r'^Buscar/(?P<pk>[\w\-]+)/$', 'app.views.findDetail',name='findDetail'),
)
