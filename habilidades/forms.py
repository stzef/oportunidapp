# -*- encoding: utf-8 -*-
from django import forms
from models import habilidadesModel

class nuevaHabilidadForm(forms.ModelForm):
	class Meta:
		model = habilidadesModel
		fields = ['categoria','nhabilidad','descripcion','precio']
		widgets = {
			'categoria':forms.Select(attrs={'class':'form-control'}),
			'nhabilidad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cual es tu habilidad'}),
			'descripcion': forms.Textarea(attrs={'rows': 2, 'class':'form-control','placeholder':'Describe tu habilidad'}),
			'precio': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
		}
		labels = {
			'categoria': ('Categoria'),
			'nhabilidad': ('Habilidad'),
		}