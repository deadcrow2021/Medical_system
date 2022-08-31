from django.urls import path
from . import views

urlpatterns = [
    path('admin_page', views.admin_page, name='admin-page'),
    path('files', views.files_page, name='files-page'),
    path('upload_files', views.UploadFilesView.as_view(), name='upload-files-page'),
]