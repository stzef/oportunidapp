from django.conf.urls import patterns, include, url
from views import loginView, registroView

urlpatterns = patterns('',
    # Examples:
    #url(r'^emailvalidate/','usuarios.views.validarEmail'),
    #url(r'^api/', include(router.urls, namespace='api')),
    url(r'^registro/',registroView.as_view(),name='registro'),
    url(r'^ingresar/',loginView.as_view(),name='ingresar'),
)