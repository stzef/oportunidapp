from django.conf.urls import patterns, include, url
from views import loginView, registroView


urlpatterns = patterns('',
    url(r'^registro/',registroView.as_view(),name='registro'),
    url(r'^ingresar/',loginView.as_view(),name='ingresar'),
)