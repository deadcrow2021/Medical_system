from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render


@login_required
def home_page(request):
    return render(request, 'home/home.html')


def account(request, user_id):
    user: User = User.objects.get(id=user_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == 'doctor':
        user_account = user.doctor
        print(user_account.__dict__)
        return render(request, 'home/account.html', { 'account': user_account })
    else:
        user_account = user.patient
        return render(request, 'home/account.html', { 'account': user_account })
