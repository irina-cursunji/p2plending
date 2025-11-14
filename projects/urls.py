# projects/urls.py

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('<uuid:pk>/', views.project_detail, name='project_detail'),  # Updated to use UUID
    path('create/', views.create_project, name='create_project'),
    path('confirmation/', views.project_confirmation, name='project_confirmation'),
]
