# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

# Mensajes de error
custom_error_messages = {
    'invalid_login': ('Usuario o contraseñas incorrectos'),
    'inactive': ('Su cuenta fue inhabilitada'),
    'null_field' : ('Este campo es requerido'),
    'blank_field': ('El campo esta en blanco'),
    'null_option':('Debes seleccionar una opcion'),
    'password_mismatch':('Las contraseñas no coinciden'),
    'user_exist':('Ese usuario ya esta ocupado'),
    'email_exist':('Ese email ya esta asociado a una cuenta'),
    'cedula_exist':('Esa cedula ya esta asociado a una cuenta'),
}


def validate_username(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(username = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['user_exist'],)

def validate_email(data):
	if len(str(data)) == 0:
		raise forms.ValidationError(custom_error_messages['null_field'],)
	elif str(data).isspace():
		raise forms.ValidationError(custom_error_messages['blank_field'],)
	elif data:
		try:
			user = User.objects.get(email = data)
		except User.DoesNotExist:
			return data
	raise forms.ValidationError(custom_error_messages['email_exist'],)