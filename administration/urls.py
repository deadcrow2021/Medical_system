from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.doctors, name='doctors-page'),
    path('files', views.files_page, name='files-page'),
    path('upload_files/<file_id>', views.UploadFilesView.as_view(), name='upload-files-page'),
    path('logs', views.logs_page, name='logs-page'),
]