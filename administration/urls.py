from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.doctors, name='doctors-page'),
    path('files', views.files_page, name='files-page'),
    path('upload_files', views.UploadFilesView.as_view(), name='upload-files-page'),
    path('logs', views.ChangeLogsView.as_view(), name='logs-page'),
]