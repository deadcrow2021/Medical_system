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


class AdminPageView(ListView):
    paginate_by: int = 3 ## Не работает из-за модели
    model = Patient
    template_name: str = 'administration/admin_page.html'
    context_object_name: Optional[str] = 'users'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'users': chain(Patient.objects.all(), Doctor.objects.all()) }
        return context
    
    # def get_queryset(self):
    #     return Patient.objects.exclude(groups='a')


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