from django.contrib import admin
from .models import Customer, MealRecord, Payment

# ---------- Customer ----------
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name', 'location')


# ---------- MealRecord ----------
@admin.register(MealRecord)
class MealRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date', 'lunch', 'dinner', 'extra_meals')
    list_filter = ('date',)
    search_fields = ('customer__name',)


# ---------- Payment ----------
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'amount', 'date')
    list_filter = ('date',)
    search_fields = ('customer__name',)
