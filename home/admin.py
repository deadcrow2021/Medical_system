from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Patient, Doctor, MedicalHistory, SelfMonitoringRecords, ReceptionNotes, MedicalCard

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalHistory)
admin.site.register(SelfMonitoringRecords)
admin.site.register(ReceptionNotes)
admin.site.register(MedicalCard)
