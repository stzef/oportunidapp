from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView



from habilidades.models import habilidadesModel, habCategoriasModel
from usuarios.models import perfilUsuarioModel


import json

# Create your views here.
def inicio(request):
	return render(request,'home.html')

# [busquedasViewTemplate] View encargada de retornar el template de busquedas
def busquedasViewTemplate(request):
	TodasLasCategorias = habCategoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categorias':TodasLasCategorias})
	#return HttpResponse(request.GET.get('estado'))



def personasListar(request):
	if request.is_ajax():
		categoria = request.GET.get('categoria',None)
		habilidades = habilidadesModel.objects.all().filter(categoria_id=categoria,estado='1')[:10]
		#data = serializers.serialize(
		#	"json",
		#	habilidadesModel.objects.all().filter(categoria_id=categoria,estado='1')[:10],
		#	fields = ('pk','nhabilidad','descripcion','val_promedio'),
		#	use_natural_foreign_keys = True,
		#)
		data = []
		for habilidad in habilidades:
			usuario = User.objects.get(id= habilidad.usuario_id)
			perfilusuario = perfilUsuarioModel.objects.get(usuario=usuario)
			item = {
				'user_id': usuario.id,
				'username': usuario.username,
				'userfirstname': usuario.first_name,
				'userlastname': usuario.last_name,
				'userphone': perfilusuario.celular1,
				'nhabilidad': habilidad.nhabilidad,
				'descripcion': habilidad.descripcion,
				'habilidad_id': habilidad.id,
				'habilidad_val':habilidad.val_promedio,
				'habilidad_nsol':habilidad.num_solicitudes,
				'foto':perfilusuario.foto.name,
			}
			data.append(item)

		return HttpResponse(
			json.dumps(data),
			content_type = "application/json"
		)

def findDetail(request,pk):
	habilidad = get_object_or_404(habilidadesModel,id=pk)
	usuario = User.objects.get(id=habilidad.usuario_id)
	perfil_usuario = perfilUsuarioModel.objects.get(usuario=usuario)
	return render(request,'FindDetail.html',{'habilidad':habilidad, 'usuario':usuario, 'perfil':perfil_usuario})



#Limpia el key 'Model' retornado por el serializador de Modelos
def cleanJsonModel(data):
	for d in data:
		del d['model']
	return data


class busquedasListView(ListView):

	model = habilidadesModel
	template_name = "busquedas_sprike.html"
	paginate_by = 1

	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset()

		formato = self.request.GET.get('format', None)

		if formato == 'json':
			return self.json_to_response()

		context = self.get_context_data()
		return self.render_to_response(context)
	#def get(self,*args, **kwargs):
	#	categoria = self.request.GET.get('categoria')
	#	if categoria:
	#		print self.kwargs
	#	else:
	#		super(busquedasListView, self).get(*args,**kwargs)

	def json_to_response(self):
		data = []
		for habilidad in self.object_list:
			data.append({
				'nhab': habilidad.nhabilidad,
				'desc': habilidad.descripcion,
				#'cat': habilidad.categoria,
			})
		return JsonResponse(data, safe=False)

	def get_queryset(self):
		queryset = self.model.objects.filter(
			descripcion__contains=self.request.GET.get('palabra','')
		).filter(
			nhabilidad__contains=self.request.GET.get('palabra','')
		).filter(
			categoria=self.request.GET.get('categoria')
		)
		return queryset


