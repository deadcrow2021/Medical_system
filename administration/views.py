from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from itertools import chain
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from home.models import Doctor, Patient, ChangeControlLog
from .models import Files
from .forms import FileUploadForm
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .search_patterns import *
from django.core.paginator import Paginator
from home.views import add_log

def user_is_admin(user):
    return not (hasattr(user, 'doctor') or hasattr(user, 'patient'))

class UserIsAdmin(UserPassesTestMixin):
    def test_func(self):
        user_obj = self.request.user
        return not (hasattr(user_obj, 'doctor') or hasattr(user_obj, 'patient'))


@login_required
@user_passes_test(user_is_admin)
def doctors(request: HttpRequest):
    template_name: str = 'administration/doctors.html'
    page_number: int = request.GET.get('page', 1)
    
    if request.method == 'POST':
        users = Doctor.objects
        for f in tuple(request.POST.items())[1:]:
            if len(f[1]) > 0:
                match f[0]:
                    case 'last_name':
                        users = users.filter(last_name__startswith=f[1])
                    case 'first_name':
                        users = users.filter(first_name__startswith=f[1])
                    case 'father_name':
                        users = users.filter(father_name__startswith=f[1])
                    case _:
                        users = users.filter(**dict((f,)))
        if isinstance(users, Doctor.objects.__class__):
            if request.POST['role'] == '':
                users = users.all()
            else:
                users = []
        prev_data = request.POST.copy()
        context = { 'prev_data': prev_data }
    else:
        context = {}
        users = Doctor.objects.all()
    
    paginator = Paginator(users, 8)
    page_obj = paginator.get_page(page_number)
    context |= { 'users': paginator.page(page_number), 'page_obj': page_obj, 'paginator': paginator }
    return render(request, template_name, context)

@login_required
def files_page(request):
    files = Files.objects.all()
    return render(request, 'administration/files.html', { 'files': files })


class UploadFilesView(UserIsAdmin, LoginRequiredMixin, CreateView):
    form_class = FileUploadForm
    template_name: str = 'administration/upload_files.html'
    success_url: str = reverse_lazy('files-page')
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            add_log(request.user, f'Добавлен файл.', '-', '-', f'Файл {form.cleaned_data["title"]} был создан.')
            messages.success(request, message='Файл успешно добавлен')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form': form })


class ChangeLogsView(UserIsAdmin, LoginRequiredMixin, ListView):
    model = ChangeControlLog
    paginate_by: int = 3
    template_name: str = 'administration/change_logs.html'
    context_object_name: str = 'logs'