from django.contrib import admin
from .models import *

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(MedicalHistory)
admin.site.register(SelfMonitoringRecords)
admin.site.register(ReceptionNotes)
admin.site.register(MedicalCard)
admin.site.register(PregnancyOutcome)
admin.site.register(ObstetricRisk)
admin.site.register(ComplicationRisk)

# observation
admin.site.register(CurrentPregnancy),
admin.site.register(Pelviometry),
admin.site.register(PregnantWomanMonitoring),
admin.site.register(AppointmentList),
admin.site.register(TakingMedications),
admin.site.register(AntibodiesDetermination),
admin.site.register(RubellaVirus),
admin.site.register(AntiresusBodies),
admin.site.register(BloodAnalysis),
admin.site.register(BiochemicalBloodAnalysis),
admin.site.register(Coagulogram),
admin.site.register(GlucoseToleranceTest),
admin.site.register(ThyroidStimulatingHormone),
admin.site.register(Smears),
admin.site.register(BacterioscopicSmearsExamination),
admin.site.register(CervixCytologicalExamination),
admin.site.register(UrineAnalysis),
admin.site.register(UrineSowing),