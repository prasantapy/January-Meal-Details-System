from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from meals.models import Meal
from django.http import JsonResponse

# Only superusers can access admin panel
def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def admin_dashboard(request):
    search_query = request.GET.get("search", "")

    meals = Meal.objects.all()
    if search_query:
        meals = meals.filter(user__username__icontains=search_query)

    # Prepare totals per user
    user_totals = {}
    for meal in meals:
        if meal.user.username not in user_totals:
            user_totals[meal.user.username] = {"lunch":0, "dinner":0}
        if meal.lunch:
            user_totals[meal.user.username]["lunch"] += 1
        if meal.dinner:
            user_totals[meal.user.username]["dinner"] += 1

    context = {
        'meals': meals,
        'user_totals': user_totals,
        'search_query': search_query
    }
    return render(request, 'adminpanel/admin_dashboard.html', context)


@login_required
@user_passes_test(superuser_required)
def admin_toggle_meal(request):
    if request.method == "POST" and request.is_ajax():
        date_str = request.POST.get("date")
        user_id = request.POST.get("user_id")
        meal_type = request.POST.get("meal_type")
        value = request.POST.get("value") == "true"

        meal = Meal.objects.get(user_id=user_id, date=date_str)

        if meal_type == "lunch":
            meal.lunch = value
        elif meal_type == "dinner":
            meal.dinner = value
        meal.save()

        # Return updated totals
        total_lunch = Meal.objects.filter(user_id=user_id, lunch=True).count()
        total_dinner = Meal.objects.filter(user_id=user_id, dinner=True).count()

        return JsonResponse({
            "status": "success",
            "total_lunch": total_lunch,
            "total_dinner": total_dinner
        })

    return JsonResponse({"status": "fail"})
