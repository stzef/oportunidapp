from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^Buscar/', 'app.views.find',name='find'),
    url(r'^Buscar-category/', 'app.views.FindDetail',name='FindDetail'),
)
