# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from models import perfilUsuarioModel

class loginForm(AuthenticationForm):
	username = forms.CharField(error_messages={'required': 'Ingresa tu Usuario, '},widget=forms.TextInput(attrs={'class':'form-control ','placeholder':'nombre de usuario','autofocus':''}))
	password = forms.CharField(error_messages={'required': 'Ingresa tu Contraseña'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))
	
class emailLoginForm(forms.Form):
	email = forms.EmailField(error_messages={'required': 'Ingresa tu email'})
	password = forms.CharField(error_messages={'required': 'Ingresa tu Contraseña'},widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(emailLoginForm, self).__init__(*args, **kwargs)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		self.user_cache = authenticate(email=email, password=password)

		if self.user_cache is None:
			raise forms.ValidationError('Email no asociado a un usuario ')
		elif not self.user_cache.is_active:
			raise forms.ValidationError('Usuario actualmente inactivo')

		return self.cleaned_data

	def get_user(self):
		return self.user_cache

class registroForm(forms.Form):
	name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Nombres', 'class':'form-control '}),)
	lastname = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Apellidos', 'class':'form-control '}),)
	username = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'placeholder':'Usuario', 'class':'form-control '}),)
	email = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control '}),)
	password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class':'form-control '}),)
	fnacimiento = forms.DateField(required=False,widget=forms.TextInput(attrs={'placeholder':'Fecha de nacimiento', 'class':'form-control '}),)
	genero  = forms.ChoiceField(choices=(('M','Masculino'),('F', 'Femenino'),('O','Otro'),),required=True,widget=forms.Select(attrs={'class':'form-control '}),)
	celular = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'placeholder':'Numero Celular', 'class':'form-control '}),)
	#Validaciones
	def clean_username(self):
		username = self.cleaned_data.get('username')
		#validate_username(username)
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		#validate_email(email)
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