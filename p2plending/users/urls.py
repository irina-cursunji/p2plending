from django.urls import path

from .views import user_detail_view
from .views import user_redirect_view
from .views import user_update_view
from . import views
app_name = "users"


urlpatterns = [
    path('users/<uuid:pk>/', views.UserDetailView.as_view(), name='detail'),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
]
