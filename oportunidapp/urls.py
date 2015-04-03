from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'usuarios.views.inicio',name='inicio'),
    url(r'^', include('usuarios.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
