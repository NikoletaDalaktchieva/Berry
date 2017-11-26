from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^$', views.programs, name='programs'),
 	url(r'^(?P<program_id>[0-9]+)/$', views.info, name='info'),
    #url(r'^direction/', views.direction, name='direction'),
]