from typing import Any, Optional
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from home.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from home.models import CustomUser
from django.utils.crypto import get_random_string


def generate_username(first_name, date):
    return f'{first_name}_{date.strftime("%d%m%Y")}'


def profile(request, profile_id):
    user_profile = CustomUser.objects.get(pk=profile_id)
    return render(request, 'users/profile.html', { 'profile': user_profile })


class PatientsView(ListView):
    model = CustomUser
    template_name: str = 'users/patients.html'
    # context_object_name = 'patients'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'patients': CustomUser.objects.filter(groups='p') }
        return context


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    
    def post(self, request, template_name, groups, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['password1'] = ''
            form.cleaned_data['password2'] = ''
            user: CustomUser = form.save(commit=False)
            password = get_random_string(length=8)
            user.set_password(password)
            user.username = generate_username(user.first_name, user.date_of_birth)
            user.groups = groups
            user.save()
            return redirect(self.success_url)
        else:
            return render(request, template_name, { 'form': form })


class RegisterDoctorView(RegisterView):
    template_name = 'users/add_doctor.html'
    success_url: Optional[str] = reverse_lazy('admin-page')
    
    def post(self, request, *args, **kwargs):
        return super().post(request, template_name=self.template_name, groups='d')


class RegisterPatientView(RegisterView):
    template_name = 'users/add_patient.html'
    success_url: Optional[str] = reverse_lazy('patients')
    
    def post(self, request, *args, **kwargs):
        return super().post(request, template_name=self.template_name, groups='p')


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
