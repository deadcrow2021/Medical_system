from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RecordCreationForm
from .models import Patient


@login_required
def home_page(request):
    return render(request, 'home/home.html')


def account(request):
    user: User = User.objects.get(id=request.user.id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == 'doctor':
        user_account = user.doctor
        return render(request, 'home/account.html', { 'account': user_account })
    else:
        user_account = user.patient
        records = user_account.records.all()
        return render(request, 'home/account.html', { 'account': user_account, 'records': records })


def add_selfmonitor_record(request):
    user: User = User.objects.get(id=request.user.id)
    form = RecordCreationForm()
    if request.method == 'POST':
        form = RecordCreationForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.patient = Patient.objects.get(user=user)
            record.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'home/add_record.html', context)
