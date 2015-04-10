# -*- encoding: utf-8 -*-
from django import forms
from models import habilidadesModel

class createHabForm(forms.ModelForm):
	class Meta:
		model = habilidadesModel
		fields = ['id_categoria','nhabilidad','descripcion','precio']