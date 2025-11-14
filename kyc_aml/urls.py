from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='kyc_index'),
    path('/submit', views.submit, name='kyc_submit'),
    path('success', views.success, name='kyc_success')
]