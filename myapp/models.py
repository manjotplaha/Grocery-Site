from django.db import models
from django.db import models

import datetime

from django.contrib.auth.models import User

from django.utils import timezone
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(default='Description')
    interested = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

    def topup(self):
        self.stock += 50
        return self.save()
# class Client(User):
#     CITY_CHOICES = [
#         ('San Francisco', 'San'),
#         ('Chicago', 'Chicago'),
#         ('New York', 'New York')
#     ]
#     shipping_address = models.Charfield(max_length=200,null=True,blank=True)
#     city = models.CharField(max_length=10, choices=CITY_CHOICES)
class Client(User):
    CITY_CHOICES = [
    ('WD', 'Windsor'),
    ('TO', 'Toronto'),
    ('CH', 'Chatham'),
    ('WL', 'WATERLOO'),]
    # fullname = models.CharField(max_length=50)
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city=models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta:
        ordering = ['id']

class OrderItem(models.Model):
    STATUS = [
        (0,'Canacelled Order'),
        (1, 'Placed Order'),
        (2, 'Shipped Order'),
        (3, 'Delivered Order'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.PositiveIntegerField(choices=STATUS, default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.item.name} by  {self.client.get_full_name()} {self.quantity} units where status is {self.get_status_display()}"

    class Meta:
        ordering = ['id']

    def total_price(self):
        return self.quantity*self.item.price

class TeamMembers(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null = True, blank = True)
    rollNum = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['id']
