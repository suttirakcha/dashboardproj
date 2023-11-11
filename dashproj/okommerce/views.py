from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def shop(request):
    return render(request, 'shop.html')
