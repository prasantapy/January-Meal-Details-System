from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from meals.models import Meal

@login_required
def my_meals(request):
    user = request.user
    search_query = request.GET.get("search", "")

    meals = Meal.objects.filter(user=user)
    if search_query:
        meals = meals.filter(user__username__icontains=search_query)

    total_lunch = meals.filter(lunch=True).count()
    total_dinner = meals.filter(dinner=True).count()

    context = {
        'meals': meals,
        'total_lunch': total_lunch,
        'total_dinner': total_dinner,
        'search_query': search_query,
    }
    return render(request, 'customer/my_meals.html', context)
