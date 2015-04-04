# -*- encoding: utf-8 -*-
from django import forms
from validations import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from models import perfilUsuarioModel

class loginForm(AuthenticationForm):
	username = forms.CharField(error_messages={'required': 'Ingresa tu Usuario, '},widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'nombre de usuario','autofocus':''}))
	password = forms.CharField(error_messages={'required': 'Ingresa tu Contraseña'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))
	

class registroForm(forms.Form):
	name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Nombres'}),)
	lastname = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Apellidos'}),)
	username = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Usuario'}),)
	email = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}),)
	password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}),)
	fnacimiento = forms.DateField(required=False,widget=forms.TextInput(attrs={'placeholder':'Fecha de nacimiento'}),)
	genero  = forms.ChoiceField(choices=(('M','Masculino'),('F', 'Femenino'),('O','Otro'),),required=True,widget=forms.Select(),)
	celular = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder':'Numero Celular'}),)
	#Validaciones
	def clean_username(self):
		username = self.cleaned_data.get('username')
		validate_username(username)
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		validate_email(email)
		return email

	def save(self):
		username = self.cleaned_data.get("username")
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")
		name = self.cleaned_data.get("name")
		lastname = self.cleaned_data.get("lastname")
		fnacimiento = self.cleaned_data.get("fnacimiento")
		genero = self.cleaned_data.get("genero")
		celular = self.cleaned_data.get("celular")

		user = User.objects.create_user(username, email, password)
		user.first_name = name
		user.last_name = lastname
		user.save()

		perfil = perfilUsuarioModel(usuario= user,fnacimiento=fnacimiento,genero=genero,celular1=celular)
		perfil.save()