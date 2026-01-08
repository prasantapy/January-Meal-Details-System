from django.urls import path
from myapp.views import create_data,show_data,home,Update_data,Delete_data

urlpatterns = [
    path('',home),
    path('create/',create_data,name='create'),
    path('read/',show_data,name='show'),
    path('update/<int:id>',Update_data,name='update'),
    path('delete/<int:id>',Delete_data,name='delete'),
    
    
]
