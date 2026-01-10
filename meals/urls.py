
from django.urls import path
from meals.views import home
urlpatterns = [
    
    path('', home, name='home'),
]
