from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from serializers import habilidadesSerializer
from models import habilidadesModel
from forms import createHabForm
from permissions import IsOwnerOrReadOnly
from usuarios.models import perfilUsuarioModel

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


"""class habilidadesViewSet(viewsets.ViewSet):
	permission_classes = (IsAuthenticated,) 
	def create(self, request):
		queryset = habilidades.objects.all()
		#return Response(request.data['nombre_habilidad'])
"""

@login_required()
def habilidades(request):
	user = request.user
	return render(request,'habilidades.html',{'user':user})


class habilidadesViewSet(viewsets.ModelViewSet):
	permission_classes = ( IsAuthenticated, IsOwnerOrReadOnly,)
	queryset = habilidadesModel.objects.all()
	serializer_class = habilidadesSerializer

	def perform_create(self, serializer):
		usuario = perfilUsuarioModel.objects.get(usuario_id=self.request.user)
		serializer.save(id_usuario=usuario)


def createHab(request):	
	if request.method == 'POST':
		form = createHabForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = createHabForm()

	#user = User.objects.get(username=request.user.get_username())

	return render(request,'createHab.html')#,{'user':user})