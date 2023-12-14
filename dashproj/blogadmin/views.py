from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from .serializers import BlogSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

def first_page(request):
    output = BlogPost.objects.filter(status='published')
    total_post = BlogPost.objects.count()
    return render(request, "blog-page.html", {"blogs": output})

def detail(request, pk):
    blogs = get_object_or_404(BlogPost, pk=pk)
    return render(request, "blog-detail.html", {
        "blogdetail": blogs
    })

class BlogView(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer