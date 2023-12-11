from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.

def shop(request):
    carousels = MarketingCampaign.objects.all()
    return render(request, 'shop.html', {'carousels': carousels})
