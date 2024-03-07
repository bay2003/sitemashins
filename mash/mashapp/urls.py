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
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form'),
    path('create/', views.create, name='create'),
    path('create/<int:post_id>/', views.view_post, name='view_post'),
    path('resume/', views.resume_view, name='resume'),
    path('tag-list/', views.TagListView.as_view(), name='tag_list'),
    path('tag-detail/<int:pk>/', views.TagDetailView.as_view(), name='tag_detail'),
    path('tag-create/', views.TagCreateView.as_view(), name='tag_create'),
    path('tag-update/<int:pk>/', views.TagUpdateView.as_view(), name='tag_update'),
    path('tag-delete/<int:pk>/', views.TagDeleteView.as_view(), name='tag_delete'),
    ]

