from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^preguntanueva/$','preguntas.views.preguntanueva',name='preguntanueva'),
)
