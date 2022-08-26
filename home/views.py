from django.shortcuts import render

def home_page(request):
    # user = "admin"
    user = "doctor"
    # user = "pat"
    return render(request, 'home/index.html', { "user": user })

def login_page(request):
    user="anonimus"
    return render(request, 'home/login.html', { "user": user })