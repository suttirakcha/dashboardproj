from django.contrib import admin
from .models import *

# Register your models here.

class TopBarAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = Topbar.objects.all().count()
        if count == 0:
            return True

        return False

admin.site.register(Topbar, TopBarAdmin)