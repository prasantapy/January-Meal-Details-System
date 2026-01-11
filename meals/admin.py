from django.contrib import admin
from .models import Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'lunch', 'dinner')
    list_filter = ('date', 'lunch', 'dinner')
    search_fields = ('user__username',)
