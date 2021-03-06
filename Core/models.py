from django.db import models
from django.contrib.auth.models import Permission, User


# Create your models here.


'''
class Pharmacy(models.Model):
    owner = models.ForeignKey(User, unique=True)
    name = models.CharField(max_length=64)
    def __str__(self):
        return self.name

'''


class CoreMedicine(models.Model):
    barcode = models.CharField(blank=False, max_length=32)
    comerical_name = models.CharField(blank=False, max_length=200)
    arabic_name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    type = models.CharField(blank=False, max_length=40)
    generic_name = models.CharField(max_length=100)
    price = models.FloatField(blank=False, default=0.0)
    med_unit_price = models.FloatField(blank=False, default=0.0)
    small_unit_price = models.FloatField(blank=False, default=0.0)
    med_unit = models.IntegerField(blank=False, max_length=11)
    small_unit = models.IntegerField(blank=False, max_length=11)
    licence = models.CharField(max_length=100)
    storage_temp = models.IntegerField(max_length=3)
    expiration = models.DateTimeField(blank=False)


class Pharmacy(models.Model):
    name = models.CharField(max_length=100, blank=False)
    branch = models.CharField(max_length=100)
    auth_user_email = models.ForeignKey(User, on_delete=models.CASCADE)


class Clients(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, blank=False, null=False)
    discount_perc = models.IntegerField(max_length=3, blank=False, default=0)
    sales = models.ForeignKey('Sales.SalesInvoice', on_delete=models.CASCADE, blank=False)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, blank=False)
    # have to add foreign keys


class Employees(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    user_name = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    address = models.CharField(max_length=200, blank=False)
    date_joined = models.DateTimeField(blank=False)
    email = models.CharField(blank=False, max_length=100)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)


class Branches(models.Model):
    branch_name = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=15, blank=False)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)





