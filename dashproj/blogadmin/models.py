from django.db import models

# Create your models here.

STATUS_CHOICE = (
    ('draft', 'Draft'),
    ('published', 'Published')
)

class BlogCategory(models.Model):
    category = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Blog categories"

    def __str__(self):
        return self.category

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=255, choices=STATUS_CHOICE, default=1)
    category = models.ForeignKey(BlogCategory, related_name='title', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title