from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('add_doctor', views.RegisterDoctorView.as_view(), name='add-doctor'),
    path('add_patient', views.RegisterPatientView.as_view(), name='add-patient'),
    path('patients', views.PatientsView.as_view(), name='patients'),
    path('recent_patients', views.recent_patients, name='recent-patients'),
    path('profile/<profile_id>', views.profile, name='profile'),
    path('profile/update/<profile_id>', views.update_profile, name='update-profile'),
    # path('profile/delete/<profile_id>', views.delete_profile, name='delete-profile'),
    path('profile/<profile_id>/add_disease', views.add_disease, name='add-disease'),
    path('switch_follow', views.follow_unfollow_patient, name='follow-unfollow'),
    path('add_medical_card', views.add_medical_card, name='add-medical-card'),
]
