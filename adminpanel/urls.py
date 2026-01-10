from django.urls import path
from django.contrib.auth.views import LogoutView
from adminpanel.views import (
    admin_meals,
    admin_update_meal,
    admin_delete_meal,
    admin_payments,
    AdminLoginView,
    admin_add_meal
)

urlpatterns = [
    path('admin_add_meal/', admin_add_meal, name='admin_add_meal'),
    path('admin_meals/', admin_meals, name='admin_meals'),
    path('admin_update/<int:meal_id>/', admin_update_meal, name='admin_update_meal'),
    path('admin_delete_meal/<int:meal_id>/', admin_delete_meal, name='admin_delete_meal'),
    path('admin_payments/', admin_payments, name='admin_payments'),
    path('login/', AdminLoginView.as_view(), name='admin_login'),
    path('logout/', LogoutView.as_view(next_page='admin_login'), name='admin_logout'),
    


]

