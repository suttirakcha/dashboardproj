from django.contrib import admin
from .models import *

# Register your models here.
class ShowBlogPost(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_at', 'updated_at']

class ShowBlogCategories(admin.ModelAdmin):
    list_display = ['category']

admin.site.register(BlogCategory, ShowBlogCategories)
admin.site.register(BlogPost, ShowBlogPost)