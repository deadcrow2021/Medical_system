from typing import Any, Optional
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from home.forms import DoctorCreationForm, PatientChangeForm, PatientCreationForm, DiseaseCreationForm
from django.urls import reverse_lazy
from home.models import Doctor, Patient, MedicalHistory
from django.utils.crypto import get_random_string
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import django.contrib.messages as messages


def generate_username(first_name, date):
    return f'{first_name}_{date.strftime("%d%m%Y")}'


def add_disease(request, profile_id):
    user: User = User.objects.get(id=profile_id)
    form = DiseaseCreationForm()
    if request.method == 'POST':
        form = DiseaseCreationForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            disease.patient = Patient.objects.get(user=user)
            disease.save()
            return HttpResponseRedirect(reverse('profile', args=(profile_id,)))
    context = {'form': form}
    return render(request, 'users/add_disease.html', context)


def profile(request, profile_id):
    user: User = User.objects.get(id=profile_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == "doctor":
        user_profile = user.doctor
        form = DoctorCreationForm(request.POST or None, instance=user_profile)
        return render(request, 'users/profile.html', { 'profile': user_profile, 'user_type': user_type, 'form':form })
    else:
        user_profile = user.patient
        form = PatientChangeForm(request.POST or None, instance=user_profile)
        diseases = user_profile.history.all()
        return render(request, 'users/profile.html', { 'profile': user_profile, 'user_type': user_type, 'diseases': diseases, 'form':form })


def update_profile(request, profile_id):
    user: User = User.objects.get(pk=profile_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'

    if user_type == "doctor":
        user_profile = user.doctor
    else:
        user_profile = user.patient
    form = PatientChangeForm(request.POST or None, instance=user_profile)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('profile', args=(profile_id,)))
    context = {'profile': user_profile, 'form': form}
    return render(request, 'users/update_profile.html', context)


def delete_profile(request, profile_id):
    user_profile: User = User.objects.get(pk=profile_id)
    if request.POST:
        user_profile.delete()
        return redirect('patients')
    context = {'profile': user_profile}
    return render(request, 'users/delete_profile.html', context)


class PatientsView(ListView):
    paginate_by: int = 6
    model = Patient
    template_name: str = 'users/patients.html'
    context_object_name = 'patients'


class RegisterView(CreateView):
    def post(self, request, *args, **kwargs):
        form2 = self.form_class(request.POST)
        if form2.is_valid():
            user: User = User()
            personal: Patient | Doctor = form2.save(commit=False)
            password = get_random_string(length=8)
            user.set_password(password)
            user.username = generate_username(personal.first_name, user.date_joined)
            user.save()
            personal.user = user
            personal.save()
            
            if isinstance(personal, Patient) and request.user.doctor:
                personal.doctors.add(request.user.doctor)
                personal.save()
            messages.success(request, 'Запись успешно добавлена!')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form2': form2 })


class RegisterDoctorView(RegisterView):
    template_name = 'users/add_doctor.html'
    success_url: Optional[str] = reverse_lazy('admin-page')
    form_class = DoctorCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context = { 'form1': UserCreationForm, 'form2': DoctorCreationForm }
        return context


class RegisterPatientView(RegisterView):
    template_name = 'users/add_patient.html'
    success_url: Optional[str] = reverse_lazy('patients')
    form_class = PatientCreationForm
    
    def post(self, request, *args, **kwargs):
        return super().post(request)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'form1': UserCreationForm, 'form2': PatientCreationForm }
        return context


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
        return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
