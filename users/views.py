from itertools import chain
from typing import Any, Optional
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from home.forms import DoctorCreationForm, PatientCreationForm
from django.urls import reverse_lazy
from home.models import Doctor, Patient
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import django.contrib.messages as messages
from django.db.models.fields.related_descriptors import ReverseOneToOneDescriptor

def generate_username(first_name, date):
    return f'{first_name}_{date.strftime("%d%m%Y")}'


def profile(request, profile_id):
    user = User.objects.get(id=profile_id)
    user_type = 'doctor' if hasattr(user, 'doctor') else 'patient'
    if user_type == "doctor":
        user_profile = user.doctor
    else:
        user_profile = user.patient
    return render(request, 'users/profile.html', { 'profile': user_profile })


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
            patient: Patient = form2.save(commit=False)
            password = get_random_string(length=8)
            user.set_password(password)
            # user.set_password('1234')
            user.username = generate_username(patient.first_name, user.date_joined)
            # user.username = 'doc1'
            user.save()
            patient.user = user
            patient.save()
            messages.success(request, 'Запись успешно добавлена!')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form1': 'form1', 'form2': form2 })


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


