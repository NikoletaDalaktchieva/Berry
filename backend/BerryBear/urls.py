from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^direction/', views.direction, name='direction'),
    url(r'^programs_name/', views.get_programs_name, name='names'),
    url(r'^program_info/', views.get_program_info, name='information'),
    url(r'^update_program_info/', views.update_program_info, name='update'),
    url(r'^run/', views.run, name='run'),
    url(r'^add/', views.add, name='add'),
    url(r'^delete/', views.delete, name='delete'),

]