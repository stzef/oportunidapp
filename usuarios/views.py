from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from models import perfilUsuarioModel
from django.views.generic import FormView
from forms import loginForm,registroForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from forms import emailLoginForm

# Create your views here.
#def inicio(request):
#	return render(request,'home.html')

#@login_required(login_url='/ingresar')
#def perfilView(request):
#	return render(request,'profile.html')


def logoutView(request):
	logout(request)
	return redirect('/')

def profileView(request):
	return render (request,'profile.html')

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

class loginView(FormView):
	form_class = loginForm
	template_name = 'login.html'
	success_url = '/habilidad/'

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(loginView, self).form_valid(form)

