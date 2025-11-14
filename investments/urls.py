from django.urls import path
from . import views

app_name = 'investments'

urlpatterns = [
    path('invest/<int:pk>/', views.invest_in_project, name='invest_in_project'),
    path('details/<int:pk>/', views.investment_details, name='investment_details'),
    path('my-investments/', views.user_investments, name='user_investments'),
]
