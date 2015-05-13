from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^Te-necesito/$','necesito.views.necesito',name='necesito'),

)


