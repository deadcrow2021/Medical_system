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
    path('profile/<profile_id>/add_disease', views.add_disease, name='add-disease'),
    path('switch_follow', views.follow_unfollow_patient, name='follow-unfollow'),
    path('medical_card/<profile_id>', views.medical_card, name='medical-card'),
    path('update_medical_card/<profile_id>', views.update_medical_card, name='update-medical-card'),
    path('pregnancy_outcome/<profile_id>', views.pregnancy_outcome, name='pregnancy-outcome'),
    path('add_pregnancy_outcome/<profile_id>', views.add_pregnancy_outcome, name='add-pregnancy-outcome'),
    path('pregnancy_observation/<profile_id>', views.pregnancy_observation_page, name='pregnancy-observation'),
    path('appearance/<profile_id>', views.appearance, name='appearance'),
    path('add_appearance/<profile_id>', views.add_appearance_page, name='add-appearance'),
    path('add_complication/<profile_id>/<obsteric_id>', views.add_complication_page, name='add-complication'),
    path('update_complication/<profile_id>/<complication_id>', views.update_complication_page, name='update-complication'),
]
