from django.shortcuts import render, redirect
from myapp.models import Customer, MealRecord


def create_data(request):
    if request.method == 'POST':
        customer = Customer.objects.create(
            name=request.POST.get('name'),
            location=request.POST.get('location')
        )

        MealRecord.objects.create(
            customer=customer,
            date=request.POST.get('date'),
            lunch=bool(request.POST.get('lunch')),
            dinner=bool(request.POST.get('dinner')),
            extra_meals=request.POST.get('extra_meals')
        )

        return redirect('show')

    return render(request, 'create.html')
def show_data(request):
    meals = MealRecord.objects.select_related('customer')
    return render(request, 'show.html', {'meals': meals})

def update_data(request, id):
    meal = MealRecord.objects.get(id=id)

    if request.method == 'POST':
        meal.lunch = bool(request.POST.get('lunch'))
        meal.dinner = bool(request.POST.get('dinner'))
        meal.extra_meals = request.POST.get('extra_meals')
        meal.save()
        return redirect('show')

    return render(request, 'update.html', {'meal': meal})
def delete_data(request, id):
    MealRecord.objects.filter(id=id).delete()
    return redirect('show')
def home(request):
    return render(request,'home.html')