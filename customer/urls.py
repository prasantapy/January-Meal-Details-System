
from django.urls import path
from .views import customer_meals

urlpatterns = [
    path('my-meals/', customer_meals, name='my_meals'),
]
