from django.contrib import admin
from .models import Patient, Doctor, MedicalHistory, SelfMonitoringRecords, ReceptionNotes, MedicalCard, PregnancyOutcome

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalHistory)
admin.site.register(SelfMonitoringRecords)
admin.site.register(ReceptionNotes)
admin.site.register(MedicalCard)
admin.site.register(PregnancyOutcome)
