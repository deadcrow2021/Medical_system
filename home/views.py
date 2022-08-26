from django.shortcuts import render
from .models import User
from .forms import LoginForm

def home_page(request):
    # user = "admin"
    user = "doctor"
    # user = "pat"
    return render(request, 'home/index.html', { "user": user })

def login_page(request):
    form = LoginForm()
    
    data = {
        "user": "anonimus",
        "form": form
    }
    return render(request, 'home/login.html', data)