from django.db import models
from django.contrib.auth.models import AbstractUser


class Smartphone(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ram = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.model}'


class CustomUser(AbstractUser):
    phone_num = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.username}'
    
