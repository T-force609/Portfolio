from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='custom_admin_login'),
    path('dashboard/', views.dashboard, name='custom_admin_dashboard'),
]