from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Category', unique=True, primary_key=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Name of product', unique=False, primary_key=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='User',
                             on_delete=models.CASCADE)
    price = models.DecimalField(
        verbose_name='Price', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
