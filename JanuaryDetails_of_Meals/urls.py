from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('django-admin/', admin.site.urls), 
    path('', include('adminpanel.urls')),  # all adminpanel URLs prefixed
    path('', include('customer.urls')),
    path('',include('meals.urls')),

]

    
