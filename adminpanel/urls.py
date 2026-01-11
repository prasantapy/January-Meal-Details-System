from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-toggle-meal/', views.admin_toggle_meal, name='admin_toggle_meal'),
]
