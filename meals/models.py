from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class MealRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='meals')
    date = models.DateField()
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    extra_meals = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('customer', 'date')

    def __str__(self):
        return f"{self.customer.name} - {self.date}"


class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - ₹{self.amount}"
