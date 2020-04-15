from django.db import models


# Create your models here.
class Outlet(models.Model):
    owner_username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=15)


class Dish(models.Model):
    owner_username = models.CharField(max_length=50)
    dish_name = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    v_or_n = models.CharField(max_length=1)
    price = models.IntegerField()

