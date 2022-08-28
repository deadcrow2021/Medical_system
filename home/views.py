from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from .models import CustomUser
import uuid

def generate_password():
    password = str(uuid.uuid4())[:8]
    return password

def generate_username(fio, date):
    # users = CustomUser.objects.all()
    fio_parsed = fio.split(' ')[0]
    return f'{fio_parsed}_{date.strftime("%d%m%Y")}'



@login_required
def home_page(request):
    role = request.user.groups.all()[0].name
    return render(request, 'home/home.html', {"role": role })

def patients(request):
    patients = CustomUser.objects.filter(groups__name="Patient")
    return render(request, 'home/patients.html', {"patients": patients})

class RegisterDoctorView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'home/add_doctor.html'
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = generate_password()
            user.set_password(password)
            user.username = generate_username(user.fio, user.date_of_birth)
            # print(user.username, user.fio, password)
            user.save()
            user_group = Group.objects.get(name='Doctor')
            user.groups.add(user_group)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form':form})


class RegisterPatientView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'home/add_patient.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = generate_password()
            user.set_password(password)
            user.username = generate_username(user.fio, user.date_of_birth)
            # print(user.username, user.fio, password)
            user.save()
            user_group = Group.objects.get(name='Patient')
            user.groups.add(user_group)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form':form})
            

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
        return render(request, 'home/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')