from django.conf.urls import patterns, include, url
from views import loginView, registroView


urlpatterns = patterns('',
	#url(r'^perfil/','usuarios.views.profileView',name='perfil'),
	url(r'^registro/',registroView.as_view(),name='signup'),
	url(r'^ingresar/',loginView.as_view(),name='login'),
	url(r'^salir/','usuarios.views.logoutView',name='logout'),
)