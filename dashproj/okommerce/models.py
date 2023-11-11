from django.db import models
from .countries import COUNTRY_CHOICE

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField
    is_sold = models.BooleanField(default=False)
    regular_price = models.DecimalField(max_digits=10,decimal_places=2)
    sales_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    address_title = models.CharField(max_length=255)
    address = models.TextField()
    city_or_county = models.CharField(max_length=255)
    state_or_province = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICE, default='Thailand')
    postal_code = models.IntegerField()

    class Meta:
        verbose_name_plural = "Addresses"