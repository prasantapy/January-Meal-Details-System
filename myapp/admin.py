from django.contrib import admin
from myapp.models import Customer,MealRecord,Payment

@admin.register(Customer)

class admin_Customer(admin.ModelAdmin):
    list_display =['id','name','location']
@admin.register(MealRecord)
class admin_MealRecord(admin.ModelAdmin):
    list_display =['date','lunch','dinner','extra_meals']

@admin.register(Payment)
class admin_Payment(admin.ModelAdmin):
    list_display =['amount','date']