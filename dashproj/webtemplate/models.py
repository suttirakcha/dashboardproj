from django.db import models

# Create your models here.

class Topbar(models.Model):
    text = models.CharField(max_length=255)
    enable_topbar = models.BooleanField(default=False)