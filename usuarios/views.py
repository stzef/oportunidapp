from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from models import perfilUsuarioModel
from django.views.generic import FormView
from forms import loginForm,registroForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponseRedirect#, JsonResponse

# Create your views here.

def inicio(request):
	return render(request,'home.html')

class registroView(FormView):
	form_class = registroForm
	template_name = 'registro.html'
	success_url = '/'

	def form_valid(self,form):
		form.save()
		return HttpResponseRedirect(self.get_success_url())

class loginView(FormView):
	form_class = loginForm
	template_name = 'ingresar.html'
	success_url = '/'

	def form_valid(self, form):
		login(self.request, form.user_cache)
		return super(loginView, self).form_valid(form)

