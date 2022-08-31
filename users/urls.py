from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('add_doctor', views.RegisterDoctorView.as_view(), name='add-doctor'),
    path('add_patient', views.RegisterPatientView.as_view(), name='add-patient'),
    path('patients', views.PatientsView.as_view(), name='patients'),
    path('profile/<profile_id>', views.profile, name='profile')
]
