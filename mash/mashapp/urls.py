from django.urls import path
from . import views
from .models import Project

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form')
    ]
