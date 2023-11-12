from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *

# Create your views here.

def first_page(request):
    output = BlogPost.objects.filter(status='published')
    return render(request, "blog-page.html", {"blogs": output})

def add_post(request):
    return render(request, "blog-create.html")

def detail(request, pk):
    blogs = get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog-detail.html", {
        "blogdetail": blogs
    })
