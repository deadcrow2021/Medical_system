from django.shortcuts import render
from home.models import CustomUser

def admin_page(request):
    all_users = CustomUser.objects.exclude(groups="a")
    return render(request, 'administration/admin_page.html', {'users':all_users})