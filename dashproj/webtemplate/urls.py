from django.urls import path
from django.contrib.auth import views as authviews
from . import views
from .forms import SignInForm

urlpatterns = [
    path('', views.home),
    path('signin/', authviews.LoginView.as_view(template_name='signin.html', authentication_form=SignInForm), name='login'),
    path('signup/', views.signup)
]
