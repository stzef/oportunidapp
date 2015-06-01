from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from views import *
from usuarios import views


urlpatterns = patterns('',
	url(r'^perfil/$','usuarios.views.profileView',name='profile'),
	url(r'^perfil/edit/$','usuarios.views.EditProfile',name='edit-profile'),
	url(r'^perfil/edit-password/$','usuarios.views.EditPassword', name='edit-password'),
	url(r'^perfil/profile-update/$','usuarios.views.UpdateProfile',name='update-profile'),
	url(r'^perfil/password-update/$','usuarios.views.UpdatePass',name='update-password'),
	url(r'^perfil/foto-usuario/$','usuarios.views.cambiarFotoPerfil',name='fotoPerfil'),
	url(r'^registro/',registroView.as_view(),name='signup'),
	url(r'^ingresar/',loginView.as_view(),name='login'),
	url(r'^salir/','usuarios.views.logoutView',name='logout'),
)