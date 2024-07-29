from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    is_verified = models.BooleanField()
    verification_code = models.IntegerField()

    def __str__(self):
        return self.user_name