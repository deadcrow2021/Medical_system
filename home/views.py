from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .models import User
# from .forms import LoginForm

@login_required
def home_page(request):
    # user = "admin"
    user = "doctor"
    # user = "pat"
    return render(request, 'home/home.html', { "user": user })

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    else:
        return render(request, 'home/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')