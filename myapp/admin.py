from django.contrib import admin
from myapp.models import Customer

@admin.register(Customer)
class admin_model(admin.ModelAdmin):
    list_display =['id','name','advance','location','date','lunch','dinner','extra_meals']
    