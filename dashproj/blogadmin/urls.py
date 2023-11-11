from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.first_page),
    path("add/", views.add_post),
    path("<int:pk>", views.detail)
]
