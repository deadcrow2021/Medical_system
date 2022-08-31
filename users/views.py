from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from home.forms import CustomUserCreationForm
from django.urls import reverse_lazy
from home.models import CustomUser
import uuid


### Add check if exist
def generate_password():
    password = str(uuid.uuid4())[:8]
    return password


def generate_username(fio, date):
    # users = CustomUser.objects.all()
    fio_parsed = fio.split(' ')[0]
    return f'{fio_parsed}_{date.strftime("%d%m%Y")}'


def profile(request, profile_id):
    user_profile = CustomUser.objects.get(pk=profile_id)
    return render(request, 'users/profile.html', {'profile':user_profile})


def patients(request):
    patients = CustomUser.objects.filter(groups__name="Patient")
    return render(request, 'users/patients.html', {"patients": patients})


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    
    def post(self, request, template_name, groups, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.cleaned_data['password1'] = ''
            form.cleaned_data['password2'] = ''
            user: CustomUser = form.save(commit=False)
            password = generate_password()
            user.set_password(password)
            user.username = generate_username(user.first_name, user.date_of_birth)
            user.groups = groups
            user.save()
            return redirect('home')
        else:
            return render(request, template_name, { 'form': form })


class RegisterDoctorView(RegisterView):
    template_name = 'users/add_doctor.html'
    
    def post(self, request, *args, **kwargs):
        return super().post(request, template_name=self.template_name, groups='d')


class RegisterPatientView(RegisterView):
    template_name = 'users/add_patient.html'
    
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
