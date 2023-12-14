from rest_framework.serializers import ModelSerializer
from .models import *

class BlogSerializer(ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'category', 'status')