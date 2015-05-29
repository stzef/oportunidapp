from django.shortcuts import render, redirect, render_to_response 
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from models import perfilUsuarioModel
from django.views.generic import FormView
from forms import loginForm,registroForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from forms import *
import json
from django.views.generic.edit import UpdateView
from django.template import RequestContext

# Create your views here.
#def inicio(request):
#	return render(request,'home.html')

#@login_required(login_url='/ingresar')
#def perfilView(request):
#	return redirect('/')


def logoutView(request):
	logout(request)
	return redirect('/')

def profileView(request):
	profile = perfilUsuarioModel.objects.get(usuario_id = request.user.id)
	return render(request,'profile.html',{'profile': profile})

def loginEmail(request):
	form = emailLoginForm(request.POST or None)
	if form.is_valid():
		login(request,form.get_user())
	return render(request, 'loginEmail.html',{'form':form})

class registroView(FormView):
	form_class = registroForm
	template_name = 'signup.html'
	success_url = '/'
	
	def form_valid(self,form):
		form.save()
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		#return HttpResponse(self.get_context_data(form=form))
		return self.render_to_response(self.get_context_data(form=form))

class loginView(FormView):
	form_class = loginForm
	template_name = 'login.html'
	success_url = '/habilidades/'

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(loginView, self).form_valid(form)

def EditProfile(request):
	pk = request.user.id
	queryset = perfilUsuarioModel.objects.get(usuario_id = pk)
	queryset2 = User.objects.get(id = pk)
	form = profileForm(instance = queryset)
	form_2 = userForm(instance = queryset2)
	return render_to_response('UpdateProfile.html', {'form':form, 'form_2':form_2}, context_instance=RequestContext(request))

def UpdateProfile(request):
	response = {}
	if request.POST:
		form = profileForm(request.POST)
		form_2 = userForm(request.POST)
		pk = request.user.id
		profile = perfilUsuarioModel.objects.get(usuario_id = pk)
		user = User.objects.get(id = pk)
		response['response'] = pk
		if form.is_valid() and form_2.is_valid():
			form = profileForm(request.POST, instance = profile)
			form_2 = userForm(request.POST, instance = user)
			form.save()
			form_2.save()
			response['response'] = "Exito al Actualizar tus Datos"
		else:
			response['response'] = form_2.errors
	else:
		response['response'] = 'Error al Actualizar'
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def EditPassword(request):
	form = passForm()
	return render(request, 'UpdatePass.html', {'form':form})

def UpdatePass(request):
	json_response = {}
	user =  User.objects.get(id = request.user.id)
	form = passForm(request.POST)
	if request.POST:
		if form.is_valid():
			user.set_password(request.POST['password_new'])
			user.save()
			json_response['message'] = 'Exito al Actualizar'
			json_response['type'] = 'success'
		else:
			json_response['message'] = 'Error al Actualizar'
			json_response['type'] = 'danger'
	else:
		json_response['message'] = 'Error al Actualizar'
		json_response['type'] = 'danger'
	return HttpResponse(json.dumps(json_response), content_type = 'application/json')
