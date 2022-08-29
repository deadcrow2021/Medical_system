from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home_page(request):
    role = request.user.groups.all()[0].name
    return render(request, 'home/home.html', {"role": role })
