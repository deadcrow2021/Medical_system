from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from home.models import CustomUser
from .models import Files
from .forms import FileUploadForm
from django.views.generic import CreateView


def admin_page(request):
    all_users = CustomUser.objects.exclude(groups="a")
    return render(request, 'administration/admin_page.html', { 'users': all_users })


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
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, { 'form': form })