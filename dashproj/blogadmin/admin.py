from django.contrib import admin
from .models import *

# Register your models here.
class ShowBlogPost(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_at', 'updated_at']

admin.site.register(BlogPost, ShowBlogPost)

class ShowBlogCategories(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(BlogCategory, ShowBlogCategories)