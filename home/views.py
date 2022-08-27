from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import Group
from .models import CustomUser
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

@login_required
def home_page(request):
    role = request.user.groups.all()[0].name
    return render(request, 'home/home.html', {"role": role })

def patients(request):
    patients = CustomUser.objects.filter(groups__name="Patient")
    return render(request, 'home/patients.html', {"patients": patients})

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'home/add_doctor.html'
    
    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            return redirect('home')
        else:
            return render(request, self.template_name, {'form':form})


def create_patient(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name=form.cleaned_data['groups'])
            user.groups.add(user_group)
            return redirect('home')
    else:
        return render(request, 'home/add_patient.html', {'form':form})
            

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