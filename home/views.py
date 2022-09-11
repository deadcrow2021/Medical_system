from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RecordCreationForm
from .models import Patient, ChangeControlLog


def add_log(who: User, what, before, after) -> ChangeControlLog:
    user_type = 'doctor' if hasattr(who, 'doctor') else 'patient' if hasattr(who, 'patient') else 'Admin'
    if user_type == 'doctor':
        fio = who.doctor.get_full_name()
    elif user_type == 'patient':
        fio = who.patient.get_full_name()
    else:
        fio = who.username
    who_changed = f'{user_type} {fio}'
    return ChangeControlLog.objects.create(
        who_changed=who_changed,
        modified_model = what,
        before=before,
        after=after,
    )

@login_required
def home_page(request):
    return render(request, 'home/home.html')


def account(request):
    user: User = User.objects.get(id=request.user.id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == 'doctor':
        user_account = user.doctor
        related_patients = user_account.patients.all()
        return render(request, 'home/account.html', { 'account': user_account, 'related_patients': related_patients })
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
            add_log(user, 'Запись в журнал самонаблюдения', '-',
                    f'Название: {form.cleaned_data["title"]}, Описание: {form.cleaned_data["description"]}')
            record.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'home/add_record.html', context)
