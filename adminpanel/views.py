from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from meals.models import MealRecord, Payment
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .decorators import admin_only
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate
from meals.models import MealRecord, Customer
from django.contrib import messages
from django.shortcuts import render, redirect




# ---------------------------
# Admin Meals List
# ---------------------------
@admin_only
def admin_meals(request):
    meals_list = MealRecord.objects.select_related('customer').order_by('-date')
    paginator = Paginator(meals_list, 10)
    page_number = request.GET.get('page')
    meals = paginator.get_page(page_number)
    return render(request, 'adminpanel/admin_meals.html', {'meals': meals})


# ---------------------------
# Admin Update Meal
# ---------------------------
@admin_only
def admin_update_meal(request, meal_id):
    meal = get_object_or_404(MealRecord, id=meal_id)

    if request.method == 'POST':
        meal.date = request.POST.get('date')
        meal.lunch = 'lunch' in request.POST
        meal.dinner = 'dinner' in request.POST
        meal.extra_meals = request.POST.get('extra_meals')

        try:
            meal.save()
            messages.success(request, "Meal record updated successfully.")
            return redirect('admin_meals')

        except IntegrityError:
            messages.error(
                request,
                "This customer already has a meal record for this date."
            )

    return render(request, 'adminpanel/admin_update.html', {'meal': meal})


# ---------------------------
# Admin Delete Meal
# ---------------------------
@admin_only
def admin_delete_meal(request, meal_id):
    meal = get_object_or_404(MealRecord, id=meal_id)
    meal.delete()
    messages.success(request, "Meal record deleted successfully.")
    return redirect('admin_meals')


# ---------------------------
# Admin Payments List
# ---------------------------
@admin_only
def admin_payments(request):
    payments_list = Payment.objects.select_related('customer').order_by('-date')
    paginator = Paginator(payments_list, 10)
    page_number = request.GET.get('page')
    payments = paginator.get_page(page_number)
    return render(request, 'adminpanel/admin_payments.html', {'payments': payments})


# ---------------------------
# Admin Delete Payment
# ---------------------------
@admin_only
def admin_delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    messages.success(request, "Payment record deleted successfully.")
    return redirect('admin_payments')


# ---------------------------
# Admin Login
# ---------------------------
class AdminLoginView(LoginView):
    template_name = 'adminpanel/admin_login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Allow only staff/superuser to login"""
        user = form.get_user()
        if not user.is_staff:
            messages.error(self.request, "You do not have permission to access the admin panel.")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin_meals')


@admin_only
def admin_add_meal(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        location = request.POST.get('location')
        date = request.POST.get('date')
        lunch = 'lunch' in request.POST
        dinner = 'dinner' in request.POST
        extra_meals = request.POST.get('extra_meals')

        customer, created = Customer.objects.get_or_create(
            name=customer_name,
            defaults={'location': location}
        )
        if not created:
            customer.location = location
            customer.save()

        try:
            MealRecord.objects.create(
                customer=customer,
                date=date,
                lunch=lunch,
                dinner=dinner,
                extra_meals=extra_meals
            )
            messages.success(request, "Meal added successfully!")
            return redirect('admin_meals')
        except IntegrityError:
            messages.error(request, "Meal record for this customer and date already exists.")

    return render(request, 'adminpanel/admin_add_meal.html')
