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
def admin_page(request: HttpRequest):
    template_name: str = 'administration/admin_page.html'
    context = { 'users': chain(Patient.objects.all(), Doctor.objects.all()) }
    paginator = Paginator(list(context['users']), 6)
    page_number: int = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context |= { 'page_obj': page_obj, 'paginator': paginator }
    
    if request.method == 'POST':
        pattern: list[str] =  str(request.POST['search']).lower().split()
        try:
            match pattern:
                case longStr, :
                    if len(longStr) % 2 == 1:
                        context = one_word_odd(longStr)
                    else:
                        context = one_word_even(longStr)
                case name, surname, fathername:
                    context = three_words(name, surname, fathername)
                # case name, surname, fathername, params:
                #     context = four_words(name, surname, fathername, params)
                case _:
                    return render(request, template_name, context)
        except Exception as ex:
            return render(request, template_name, { 'error': ' '.join(pattern), 'btn': 'Вернуться' })
        paginator = Paginator(list(context['users']), 6)
        page_obj = paginator.get_page(page_number)
        context.update({ 'page_obj': page_obj, 'paginator': paginator })
        context |= { 'btn': 'Вернуться' }
        return render(request, template_name, context)
    else:
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
            add_log(request.user, f'Добавлен файл.',
                    '-', f'Файл {form.cleaned_data["title"]} был создан.')
            messages.success(request, message='Файл успешно добавлен')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form': form })


class ChangeLogsView(UserIsAdmin, LoginRequiredMixin, ListView):
    model = ChangeControlLog
    paginate_by: int = 3
    template_name: str = 'administration/change_logs.html'
    context_object_name: str = 'logs'