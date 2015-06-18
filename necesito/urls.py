from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^mensajes/$','necesito.views.necesito',name='necesito'),
	url(r'^te-necesito/(?P<usuarioSolicitado>[\w\-]+)/(?P<habilidadSlug>[\w\-]+)/$','necesito.views.teNecesito',name='tenecesito'),
	url(r'^solicitud/$','necesito.views.crearMensajeSolicitud',name='solicitud'),
)


