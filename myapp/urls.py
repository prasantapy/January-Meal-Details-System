from django.urls import path
from myapp.views import home,create_data,show_data,update_data,delete_data
urlpatterns = [
    path('',home,name='home'),
    path('create/',create_data,name='create'),
    path('read/',show_data,name='show'),
    path('update/<int:id>',update_data,name='update'),
    path('delete/<int:id>',delete_data,name='delete'),
    
    
]
