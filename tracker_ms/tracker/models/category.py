from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=[('i', 'Income'), ('e', 'Expense')])

    def __str__(self):
        return f"{self.name} ({'Income' if self.type == 'i' else 'Expense'})"