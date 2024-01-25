from django.db import models
from django.core.exceptions import ValidationError

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Order(models.Model):
    order_number = models.CharField(max_length=10)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title
