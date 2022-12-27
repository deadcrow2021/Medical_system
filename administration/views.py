from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from home.models import Doctor, ChangeControlLog
from .models import Files
from home.models import SAMD
from .forms import FileUploadForm
from django.views.generic import CreateView
from django.contrib import messages
from django.core.paginator import Paginator
from home.views import add_log
from med_system.funcs import get_and_add_cookie
from urllib.parse import quote

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
    to_add = f'/doctors!Доктора'
    
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
    resp = render(request, template_name, context)
    resp.set_cookie('nav', quote(to_add, safe='!#/'), samesite='strict')
    return resp

@login_required
def files_page(request):
    to_add: str = f'/files!Файлы'
    
    if request.method == "POST":
        id = request.POST.get('delete_id')
        Files.objects.get(pk=id).delete()
    
    files = Files.objects.all()
    
    resp = render(request, 'administration/files.html', { 'files': files })
    resp.set_cookie('nav', quote(to_add, safe='!#/'), samesite='strict')
    return resp


class UploadFilesView(UserIsAdmin, LoginRequiredMixin, CreateView):
    form_class = FileUploadForm
    template_name: str = 'administration/upload_files.html'
    success_url: str = reverse_lazy('files-page')
    
    def post(self, request: HttpRequest, file_id: int, *args: Any, **kwargs: Any) -> HttpResponse:
        if int(file_id) > -1:
            file = Files.objects.get(pk=file_id)
            form = FileUploadForm(request.POST, request.FILES, instance=file)
        else:
            form = FileUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save(commit=True)
            add_log(request.user, f'Добавлен файл.', '-', '-', f'Файл {form.cleaned_data["title"]} был создан.')
            messages.success(request, message='Файл успешно добавлен')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form': form })
    
    def get(self, request: HttpRequest, file_id: int, *args: str, **kwargs: Any) -> HttpResponse:
        if int(file_id) > -1:
            file = Files.objects.get(pk=file_id)
            form = FileUploadForm(request.POST, request.FILES, instance=file)
        else:
            form = FileUploadForm(request.POST, request.FILES)
        return render(request, self.template_name, { 'form': form })


# class ChangeLogsView(UserIsAdmin, LoginRequiredMixin, ListView):
def logs_page(request: HttpRequest):
    template_name: str = 'administration/change_logs.html'
    to_add = '/logs!Жунал изменений'
    page_number: int = request.GET.get('page', 1)
    
    logs = ChangeControlLog.objects.all()
    paginator = Paginator(logs, 5)
    page_obj = paginator.get_page(page_number)
    context = { 'logs': paginator.page(page_number), 'page_obj': page_obj, 'paginator': paginator }
    resp = render(request, template_name, context)
    resp.set_cookie('nav', quote(to_add, safe='!#/'), samesite='strict')
    return resp


def admin_samd(request: HttpRequest) -> HttpResponse:
    template_name: str = 'administration/admin_samd.html'
    samd_docs = SAMD.objects.all()
    to_add = f'#/samd/!СЭМД документы'
    resp = render(request, template_name, { 'samd_docs': samd_docs })
    return get_and_add_cookie(request, to_add, resp)

