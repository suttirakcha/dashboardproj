from django.db import models
from .countries import COUNTRY_CHOICE
from django.core.exceptions import ValidationError

# Create your models here.

PROMOTION_TYPE_CHOICE = (
    ('Discount', 'Discount'),
    ('Coupon', 'Coupon')
)

class ProductCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Product categories"

    def __str__(self):
        return self.category

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField
    is_sold = models.BooleanField(default=False)
    amount = models.IntegerField()
    product_category = models.ForeignKey(ProductCategory, related_name='product_name', on_delete=models.CASCADE)
    regular_price = models.DecimalField(max_digits=10,decimal_places=2)
    sales_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

    def clean(self):
        if self.sales_price and self.sales_price > self.regular_price:
            raise ValidationError('Sales price cannot be greater than regular price')

class Address(models.Model):
    address_title = models.CharField(max_length=255)
    address = models.TextField()
    city_or_county = models.CharField(max_length=255)
    state_or_province = models.CharField(max_length=255)
    country = models.CharField(max_length=255, choices=COUNTRY_CHOICE, default='Thailand')
    postal_code = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address_title

class Promotion(models.Model):
    promotion_name = models.CharField(max_length=255)