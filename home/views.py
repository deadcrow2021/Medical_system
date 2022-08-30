from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_page(request):
    role = request.user._wrapped.groups
    return render(request, 'home/home.html', {"role": role })
