from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

# Create your views here.

def shop(request):
    carousels = MarketingCampaign.objects.all()
    products = Product.objects.all()
    return render(request, 'shop.html', {'carousels': carousels, 'products': products})

def single_product(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'single-product.html', {'products':products})