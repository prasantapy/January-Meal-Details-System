from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from meals.models import MealRecord

@login_required(login_url='admin_login')
def customer_meals(request):
    """
    Show logged-in customer their meal records
    """
    customer = request.user.customer
    meals = customer.meals.all().order_by('-date')

    # Summary
    total_lunch = meals.filter(lunch=True).count()
    total_dinner = meals.filter(dinner=True).count()
    total_extra = meals.exclude(extra_meals__isnull=True).exclude(extra_meals__exact='').count()

    # Optional: date search
    query_date = request.GET.get('date')
    if query_date:
        meals = meals.filter(date=query_date)

    context = {
        'meals': meals,
        'total_lunch': total_lunch,
        'total_dinner': total_dinner,
        'total_extra': total_extra,
        'query_date': query_date or '',
    }
    return render(request, 'customer/my_meals.html', context)
