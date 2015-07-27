from django.shortcuts import render
from django.views.generic import TemplateView

#Importaciones de otras librerias
from braces.views import LoginRequiredMixin


class miCuentaView(LoginRequiredMixin, TemplateView):
	template_name = 'mi_cuenta.html'
	login_required = True






def inicio(request):
	return render(request,'home.html')

def view_404(request):
	return render(request,'404.html')

def view_500(request):
	return render(request,'500.html')

