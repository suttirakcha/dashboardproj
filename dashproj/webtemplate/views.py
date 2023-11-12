from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/signin/')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})