from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from home.models import CustomUser
from .models import Files
from .forms import FileUploadForm
from django.views.generic import CreateView, ListView


class AdminPageView(ListView):
    model = CustomUser
    template_name: str = 'administration/admin_page.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context |= { 'users': CustomUser.objects.exclude(groups='a') }
        return context


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