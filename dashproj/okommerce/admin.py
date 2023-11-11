from django.contrib import admin
from .models import *

# Register your models here.

class ProductLists(admin.ModelAdmin):
    list_display = ['name', 'regular_price', 'sales_price', 'created_at', 'updated_at']

class AddressLists(admin.ModelAdmin):
    list_display = ['address_title', 'city_or_county', 'state_or_province', 'country']

admin.site.register(Product, ProductLists)
admin.site.register(Address, AddressLists)