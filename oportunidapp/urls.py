from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'app.views.inicio',name='inicio'),
    url(r'^', include('usuarios.urls')),
    url(r'^', include('habilidades.urls')),
    url(r'^', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
