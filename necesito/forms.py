# -*- encoding: utf-8 -*-
from django import forms
from necesito.models import teNecesitoModel

class teNecesitoForm(forms.ModelForm):

	class Meta:
		model = teNecesitoModel
		exclude = ['fecha']
		#widgets = {
		#	'usuarioSolicitante' : forms.HiddenInput(),
		#	'usuarioRequerido' : forms.HiddenInput(),
		#	'habilidadSolicitada' : forms.HiddenInput(),
		#	'mensaje' : forms.TextInput(attrs={'required':''})
		#}
	def __init__(self, *args, **kwargs):
		print kwargs.get('usuarioSolicitante')
		self.usuarioSolicitante = kwargs.get('usuarioSolicitante')
		super(teNecesitoForm, self).__init__(*args, **kwargs)
