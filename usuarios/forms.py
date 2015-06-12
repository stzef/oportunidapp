# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from models import perfilUsuarioModel
from django.core.exceptions import ValidationError

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

	name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Nombres', 'class':'form-control col-md-11'}),)
	lastname = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Apellidos', 'class':'form-control col-md-11'}),)
	username = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Usuario', 'class':'form-control col-md-11'}),)
	email = forms.EmailField(max_length=30,required=True,widget=forms.TextInput(attrs={'type': 'email', 'required': 'required', 'placeholder':'Email', 'class':'form-control col-md-11'}),)
	password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder':'Contraseña', 'class':'form-control col-md-11'}),)
	password_confirm = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder':'Confirma tu contraseña', 'class':'form-control col-md-11'}),)
	fnacimiento = forms.DateField(required=False,widget=forms.TextInput(attrs={'type': 'date', 'required': 'required', 'placeholder':'Fecha de nacimiento', 'class':'form-control col-md-11'}),)
	genero  = forms.ChoiceField(choices=(('M','Masculino'),('F', 'Femenino'),('O','Otro'),),required=True,widget=forms.Select(attrs={'class':'form-control col-md-11'}),)
	celular = forms.IntegerField(required=False,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Numero Celular', 'class':'form-control col-md-11'}),)
	#Validaciones
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('Usuario en uso. Ingresa otro')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('Email en uso. Ingresa otro')
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

class userForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name']

	#username = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Usuario', 'class':'form-control col-md-11'}),)
	first_name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Nombres', 'class':'form-control col-md-11'}),)
	last_name = forms.CharField(max_length=20,required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Apellidos', 'class':'form-control col-md-11'}),)

	def clean_username(self):
		username = self.cleaned_data.get('username')
		"""
		id = self.cleaned_data.get('id')
		if User.objects.exclude(pk = self.instance.pk).filter(username = username).exists():
			raise forms.ValidationError('Usuario en uso. Ingresa otro')
		"""
		return username

class profileForm(forms.ModelForm):
	class Meta:
		model = perfilUsuarioModel
		fields = ['cedula', 'genero', 'fnacimiento', 'celular1']

	cedula = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Cedula', 'class':'form-control col-md-11'}),)
	genero  = forms.ChoiceField(choices=(('M','Masculino'),('F', 'Femenino'),('O','Otro'),),required=True,widget=forms.Select(attrs={'class':'form-control col-md-11'}),)
	fnacimiento = forms.DateField(required=True,widget=forms.TextInput(attrs={'type': 'date', 'required': 'required', 'placeholder':'Fecha de nacimiento', 'class':'form-control col-md-11'}),)
	celular1 = forms.IntegerField(required=True,widget=forms.TextInput(attrs={'required': 'required', 'placeholder':'Numero Celular', 'class':'form-control col-md-11'}),)

class passForm(forms.Form):

	#password_old = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder':'Ingresa tu contraseña actual', 'class':'form-control col-md-11'}),)
	password_new = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder':'Ingresa tu contraseña nueva', 'class':'form-control col-md-11'}),)
	password_confirm = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput(attrs={'required': 'required', 'placeholder':'Confirma tu contraseña', 'class':'form-control col-md-11'}),)