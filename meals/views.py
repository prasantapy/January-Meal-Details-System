from django.shortcuts import render, redirect
from meals.models import MealRecord, Customer
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    meals = MealRecord.objects.all().order_by('-date')  # default: show all
    query_name = request.GET.get('name', '')
    query_date = request.GET.get('date', '')

    # Filter if search applied
    if query_name:
        meals = meals.filter(customer__name__icontains=query_name)
    if query_date:
        meals = meals.filter(date=query_date)

    # Login handling
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin_meals')  # full modify access
            else:
                messages.info(request, "You cannot modify records.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'meals/home.html', {
        'meals': meals,
        'query_name': query_name,
        'query_date': query_date,
    })
