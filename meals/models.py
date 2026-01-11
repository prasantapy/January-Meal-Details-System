from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'date')  # Prevent duplicate meals per user/day
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date}"

    @property
    def total_lunch(self):
        return Meal.objects.filter(user=self.user, lunch=True).count()

    @property
    def total_dinner(self):
        return Meal.objects.filter(user=self.user, dinner=True).count()
