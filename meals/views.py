from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import JsonResponse
from .models import Meal
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils import timezone

# ---------- LOGIN VIEW ----------
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("present_table")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "meals/login.html")


# ---------- LOGOUT VIEW ----------
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")


# ---------- PRESENT TABLE VIEW ----------
@login_required
def present_table(request):
    user = request.user
    search_query = request.GET.get("search", "")

    # Partial name search (case-insensitive)
    meals = Meal.objects.filter(user=user)
    if search_query:
        meals = meals.filter(user__username__icontains=search_query)

    # Calculate totals
    total_lunch = Meal.objects.filter(user=user, lunch=True).count()
    total_dinner = Meal.objects.filter(user=user, dinner=True).count()

    context = {
        "meals": meals,
        "total_lunch": total_lunch,
        "total_dinner": total_dinner,
        "search_query": search_query,
    }
    return render(request, "meals/present_table.html", context)


# ---------- AJAX AUTO-SAVE VIEW ----------
@login_required
def toggle_meal(request):
    if request.method == "POST" and request.is_ajax():
        user = request.user
        date_str = request.POST.get("date")
        meal_type = request.POST.get("meal_type")
        value = request.POST.get("value") == "true"  # checkbox True/False

        # Parse date
        date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()

        # Get or create meal entry
        meal, created = Meal.objects.get_or_create(user=user, date=date)

        # Update meal type
        if meal_type == "lunch":
            meal.lunch = value
        elif meal_type == "dinner":
            meal.dinner = value
        meal.save()

        # Return updated totals
        return JsonResponse({
            "total_lunch": Meal.objects.filter(user=user, lunch=True).count(),
            "total_dinner": Meal.objects.filter(user=user, dinner=True).count(),
            "status": "success"
        })
    return JsonResponse({"status": "fail"})
