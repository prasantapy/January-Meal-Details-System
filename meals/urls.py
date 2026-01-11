from django.urls import path
from . import views

urlpatterns = [
    # Login / Logout
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    # Present Table
    path("present-table/", views.present_table, name="present_table"),

    # AJAX auto-save toggle
    path("toggle-meal/", views.toggle_meal, name="toggle_meal"),
]
