from django.db import models
from .category import Category

class FinancialEntry(models.Model):
    user_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)