from itertools import chain
from typing import Any, Optional
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from home.models import Doctor, Patient
from .models import Files
from .forms import FileUploadForm
from django.views.generic import CreateView, ListView
from django.contrib import messages
from .search_patterns import *
from django.core.paginator import Paginator


def admin_page(request: HttpRequest):
    template_name: str = 'administration/admin_page.html'
    context = { 'users': chain(Patient.objects.all(), Doctor.objects.all()) }
    paginator = Paginator(list(context['users']), 6)
    page_number: int = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(f"{page_obj}")
    context |= { 'page_obj': page_obj, 'paginator': paginator }
    
    if request.method == 'POST':
        pattern: list[str] =  str(request.POST['search']).lower().split()
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
        paginator = Paginator(list(context['users']), 6)
        page_obj = paginator.get_page(page_number)
        context.update({ 'page_obj': page_obj, 'paginator': paginator })
        context |= { 'btn': 'Вернуться' }
        return render(request, template_name, context)
    else:
        return render(request, template_name, context)


def files_page(request):
    files = Files.objects.all()
    return render(request, 'administration/files.html', { 'files': files })


class UploadFilesView(CreateView):
    form_class = FileUploadForm
    template_name: str = 'administration/upload_files.html'
    success_url: str = reverse_lazy('files-page')
    
    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, message='Файл успешно добавлен')
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form': form })