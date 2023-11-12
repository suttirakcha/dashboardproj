from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.first_page),
    path("<int:pk>", views.detail)
]
