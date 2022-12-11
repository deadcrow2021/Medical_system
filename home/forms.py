from .models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from .choices import *

class TextInput(forms.TextInput):
    input_type = 'text'

class DateInput(forms.DateInput):
    input_type = 'date'

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class PatientCreationForm(forms.ModelForm):
    class Meta:
        model = MedicalCard
        fields = 'first_name', 'last_name', 'father_name',\
                'date_of_birth', 'series_number_pass', 'when_issued',\
                'when_whom_issued', 'registration_address', 'oms_policy',\
                'snils', 'mobile_phone', 'email'
        widgets = {
            'mobile_phone': forms.NumberInput(attrs={ 'type': 'tel', 'minlength': 11 }),
            'date_of_birth': DateInput(),
            'when_issued': DateInput()
        }
        error_messages = {
            'mobile_phone' : {
                'invalid': "Неправильный формат ввода, номер должен состоять из 11 цифр"
            }
        }
        #     'date_of_birth': DateInput(),
        #     'date_death': DateInput(),
        # }


class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'cabinet',
            'territory',
            'med_org',
            'role',
            'telephone',
            'email'
        )


class PatientChangeForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = (
            'first_name',
            'last_name',
            'father_name',
            'telephone',
            'email',
        )


class DiseaseCreationForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = (
            'disease',
            'date_cured',
        )
        widgets = {
            'date_cured': DateInput(),
        }


class RecordCreationForm(forms.ModelForm):
    class Meta:
        model = SelfMonitoringRecords
        fields = (
            'title',
            'description',
        )


class PatientFilterForm(forms.Form):
    CHOICES = (
            ('d', 'Текущий день'),
            ('w', 'Текущая неделя'),
            ('m', 'Текущий месяц'),
            ('30', '30 дней'),
        )
    time_interval = forms.ChoiceField(label='Временной промежуток', choices=CHOICES)
    territory = forms.BooleanField(label='Мои территории', required=False)


class ReceptionAddForm(forms.ModelForm):
    class Meta:
        model = ReceptionNotes
        fields = (
            'date_meeting', 'status', 'doctor'
        )
        widgets = {
            'date_meeting': DateTimeInput()
        }
        labels = {
            "doctor": "Доктор"
        }


class ReceptionAddAddingForm(forms.ModelForm):
    serv = RECEPTION_SERVICE
    class Meta:
        model = ReceptionNotes
        fields = (
            'date_recording', 'service', 'deadline_from', 'deadline_to'
        )
        widgets = {
            'date_recording': DateInput(),
            'deadline_from': TextInput(),
            'deadline_to': TextInput(),
        }
        labels = {
            "deadline_to": "По"
        }


class ReceptionAddConfirmForm(forms.ModelForm):
    class Meta:
        model = ReceptionNotes
        fields = (
            'doctor', 'date_meeting'
        )
        widgets = {
            'date_meeting': DateTimeInput()
        }
        labels = {
            'doctor': "Доктор"
        }


class ReceptionAddResultForm(forms.ModelForm):
    file_field = forms.FileField(label="Файлы", widget=forms.ClearableFileInput(attrs={ 'multiple': True }))
    class Meta:
        model = ReceptionNotes
        fields = (
            'date_completed', 'result'
        )
        widgets = {
            'date_completed': DateTimeInput()
        }


class ReceptionViewForm(forms.ModelForm):
    class Meta:
        model = ReceptionNotes
        fields = (
            'date_meeting','med_organization', 'specialization',
            'cabinet', 'status'
        )


class DataSamplingForm(forms.Form):
    mkb_10 = forms.CharField(label='Заболевание по МКБ-10', max_length=270, required=False)
    medical_organization = forms.CharField(label='Медицинская организация', max_length=270, required=False)
    # medical_organization = forms.ChoiceField(label='Медицинская организация', choices=MEDICAL_ORGANIZATION, required=False)
    territory = forms.ChoiceField(label='Территория', choices=TERRITORY, required=False)

    age_from = forms.IntegerField(label='Возраст от', min_value=1, max_value=99, required=False)
    age_to = forms.IntegerField(label='До', min_value=1, max_value=99, required=False)

    date_of_birth = forms.DateField(label='Дата рождения', required=False, widget=DateInput())
    date_of_death = forms.DateTimeField(label='Дата смерти', required=False, widget=DateTimeInput())
    # city_village = forms.ChoiceField(label='Житель города/села', choices=CITYVILLAGE, required=False)
    
    class Meta:
        widgets = {
            'date_of_birth': DateInput(),
            'date_of_death': DateTimeInput()
        }

class MedicalCardForm(forms.ModelForm):
    class Meta:
        model = MedicalCard
        fields = ('last_name', 'first_name', 'father_name', 'date_of_birth', 'age', 'series_number_pass', 'when_issued',    # Личные данные
                'when_whom_issued', 'residence_address', 'registration_address', 'oms_policy', 'snils', 'marital_status',   # Личные данные
                'mobile_phone', 'home_phone', 'work_phone', 'email', 'education', 'profession', 'work_place', 'disability', # Контактны данные
                'trusted_person_fio', 'trusted_person_phone', # Контактны данные
                'maternity_leave_start', 'maternity_leave_finish', 'disability_certificate', 'generic_certificate_number', # Дополнительные данные
                'generic_certificate_date', 'allergy', 'allergy_description',
                'mother_blood_group', 'mother_blood_rh', 'mother_date_of_determination',
                'father_blood_group', 'father_blood_rh', 'father_date_of_determination',
                'pregnancy_count', 'births_by_term',
                'gestation_period_weeks', 'first_visit_date', 'childbirth_date', 'childbirth_gestation_period',
                'med_org', 'diagnosis', 'complications', 'somatic_diseases', 'gynecological_diseases')
        widgets = {
            'date_of_birth': DateInput(),
            'maternity_leave_start': DateInput(),
            'maternity_leave_finish': DateInput(),
            'generic_certificate_date': DateInput(),
            'first_visit_date': DateInput(),
            'childbirth_date': DateInput()
        }


class MedicalCardProfileForm(forms.ModelForm):
    class Meta:
        model = MedicalCard
        fields = 'first_name', 'last_name', 'father_name', 'mobile_phone', 'email'


class ObstetricRiskCreationForm(forms.ModelForm):
    class Meta:
        model = ObstetricRisk
        fields = ('visit', )


class ComplicationRiskCreationForm(forms.ModelForm):
    class Meta:
        model = ComplicationRisk
        fields = ('complication_risk', 'risk_value')


class PregnancyOutcomeForm(forms.ModelForm):
    class Meta:
        model = PregnancyOutcome
        fields = 'pregnancy_count', 'childbirth_date', \
                'pregnancy_outcome', 'if_childbirth', 'if_abortion', 'death_time', \
                'disease', 'gestation_period_weeks', 'number_of_fetuses'
        widgets = {
            'childbirth_date': DateTimeInput(),
            'death_time': DateTimeInput()
        }


class PelviometryForm(forms.ModelForm):
    class Meta:
        model = Pelviometry
        fields = 'date', 'dsp', 'dcr', 'dtroch', \
                'dext', 'cvera', 'cdiag', 'solovyov_index', \
                'michaelis_rhombus_x', 'michaelis_rhombus_y', \
                'pelvis_dimensions',
        widgets = {
            'date': DateInput()
        }


class PregnantWomanMonitoringForm(forms.ModelForm):
    class Meta:
        model = PregnantWomanMonitoring
        fields = 'date', 'gestation_period_weeks', 'complaints', 'weight_gain', \
                'systolic_blood_pressure', 'blood_pressure_diastolic', 'pulse', \
                'fetus_heartbeat', 'fetus_stirring', 'fundal_height', \
                'abdominal_circumference', 'fetal_position', 'to_pelvis_entrance', \
                'adjacent_part', 'protein_in_urine', 'hemoglobin', 'glucose', \
                'ttg', 's_agalactiae', 'bacterioscopic_smears_examination', \
                'cervix_сytological_examination', 'urine_culture', 'fetal_development_assessment_11_14', \
                'fetal_development_assessment_19_21', 'ultrasound_cervicometry', 'fetal_ultrasound', \
                'invasive_diagnostics', 'fetal_cardiotocography',
        widgets = {
            'date': DateInput(),
        }


class AppointmentListForm(forms.ModelForm):
    class Meta:
        model = AppointmentList
        fields = 'visit_number', 'date', 'gestation_period_weeks', 'service', \
                'analysis', 'appointment', 'disability_certificate', \
                'next_visit_date',
        widgets = {
            'date': DateInput(),
            'next_visit_date': DateInput()
        }


class TakingMedicationsForm(forms.ModelForm):
    class Meta:
        model = TakingMedications
        fields = 'name', 'date_start', 'date_finish', 'indications', \
                'dose_duration', 'side_effects'
        widgets = {
            'date_start': DateInput(),
            'date_finish': DateInput()
        }
        

class AntibodiesDeterminationForm(forms.ModelForm):
    class Meta:
        model = AntibodiesDetermination
        fields = 'date', 'treponema_antibodies', 'hiv_antibodies', \
            'hbsag_antibodies', 'anti_hcv',
        widgets = {
            'date': DateInput()
        }


class RubellaVirusForm(forms.ModelForm):
    class Meta:
        model = RubellaVirus
        fields = 'date', 'lgm', 'lgg',
        widgets = {
            'date': DateInput()
        }


class AntiresusBodiesForm(forms.ModelForm):
    class Meta:
        model = AntiresusBodies
        fields = 'date', 'antiresus_bodies',
        widgets = {
            'date': DateInput()
        }


class BloodAnalysisForm(forms.ModelForm):
    class Meta:
        model = BloodAnalysis
        fields = 'date', 'hemoglobin', 'red_blood_cells', 'color_indicator', \
            'reticulocytes', 'platelets', 'white_blood_cells', 'myelocytes', \
            'metamyelocytes', 'stick_core', 'segmentonuclear', 'eosinophils', \
            'basophils', 'lymphocytes', 'monocytes', 'soe',
        widgets = {
            'date': DateInput()
        }


class BiochemicalBloodAnalysisForm(forms.ModelForm):
    class Meta:
        model = BiochemicalBloodAnalysis
        fields = 'date', 'total_bilirubin', 'direct_bilirubin', \
            'total_protein', 'alt', 'ast', 'glucose',
        widgets = {
            'date': DateInput()
        }


class CoagulogramForm(forms.ModelForm):
    class Meta:
        model = Coagulogram
        fields = 'date', 'platelet_count', 'astv', \
            'fibrinogen', 'prothrombin_time',
        widgets = {
            'date': DateInput()
        }


class GlucoseToleranceTestForm(forms.ModelForm):
    class Meta:
        model = GlucoseToleranceTest
        fields = 'date', 'period', 'result',
        widgets = {
            'date': DateInput()
        }


class ThyroidStimulatingHormoneForm(forms.ModelForm):
    class Meta:
        model = ThyroidStimulatingHormone
        fields =  'date', 'period', 'result',
        widgets = {
            'date': DateInput()
        }


class SmearsForm(forms.ModelForm):
    class Meta:
        model = Smears
        fields = 'date', 'result',
        widgets = {
            'date': DateInput()
        }


class BacterioscopicSmearsExaminationForm(forms.ModelForm):
    class Meta:
        model = BacterioscopicSmearsExamination
        fields = 'date', 'c_white_blood_cells', 'c_epithelium', \
            'c_key_cels', 'c_candida', 'c_trichomonads', 'c_gonococci', \
            'c_ph', 'v_white_blood_cells', 'v_epithelium', 'v_key_cels', \
            'v_candida', 'v_trichomonads', 'v_gonococci', 'v_ph', \
            'u_white_blood_cells', 'u_epithelium', 'u_key_cels', \
            'u_candida', 'u_trichomonads', 'u_gonococci', 'u_ph'
        widgets = {
            'date': DateInput()
        }


class CervixCytologicalExaminationForm(forms.ModelForm):
    class Meta:
        model = CervixCytologicalExamination
        fields = 'date', 'result',
        widgets = {
            'date': DateInput()
        }


class UrineAnalysisForm(forms.ModelForm):
    class Meta:
        model = UrineAnalysis
        fields = 'date', 'amount', 'ph', 'density', \
            'u_white_blood_cells', 'red_blood_cells', \
            'protein', 'cylinders', 'salt'
        widgets = {
            'date': DateInput()
        }


class UrineSowingForm(forms.ModelForm):
    class Meta:
        model = UrineSowing
        fields = 'date', 'result',
        widgets = {
            'date': DateInput()
        }


class PatientInformationForm(forms.ModelForm):
    class Meta:
        model = PatientInformation
        fields = 'congenital_malformations', 'congenital_malformations_str', 'height', 'mass', \
                'imt', 'preeclampsia_risk', 'preeclampsia_risk_str', 'premature_birth_risk', \
                'premature_birth_risk_str', 'growth_retardation_risk', 'growth_retardation_risk_str', \
                'thromboembolic_complications', 'thromboembolic_complications_str', 'another_risks', \
                'another_risks_str', 'child_infections', 'child_infections_str', 'dispensary_accounting', \
                'dispensary_accounting_str', 'injures_operations', 'injures_operations_str', 'somatic_diseases', \
                'somatic_diseases_str', 'socially_significant_infections', 'socially_significant_infections_str', \
                'hiv_status', 'date', 'epidnomer', 'antiretroviral_therapy', 'hereditary_diseases', \
                'hereditary_diseases_str', 'blood_transfusions', 'year', 'last_fluorography_date', \
                'last_fluorography_date_result', 'bad_habits', 'smoking', 'alcohol', 'alcohol_type', \
                'drugs', 'occupational_hazards', 'occupational_hazards_str', 'tetanus', 'measles', 'rubella', \
                'chickenpox', 'flu', 'HPV', 'hepatitis_B', 'other_vaccnation', 'year_start', 'profusion', \
                'painfulness', 'regularity', 'sexual_life', 'contraception_method', 'contraception_period', \
                'diseases_operations', 'disease_date', 'sti', 'treatment', 'treatment_date', 'year_mammary', \
                'mammary_method', 'mammary_result', 'year_cervix', 'cervix_method', 'cervix_result',
        widgets = {
            'date': DateInput(),
            'last_fluorography_date': DateInput(),
            'disease_date': DateInput(),
            'treatment_date': DateInput()
        }


class PreviousPregnancyForm(forms.ModelForm):
    class Meta:
        model = PreviousPregnancy
        fields = 'year', 'pragnancy_has_come', 'outcome', 'outcome_str', \
                'birth_number', 'birth_str', 'complications'


class CarvixScarForm(forms.ModelForm):
    class Meta:
        model = CarvixScar
        fields = 'date', 'operation_name', 'if_caesarean', 'scar_localization', 'operation_features'
        widgets = {
            'date': DateInput()
        }


class FatherInfoForm(forms.ModelForm):
    class Meta:
        model = FatherInfo
        fields = 'age', 'height', 'mass', 'imt', 'bad_habits', \
        'chronic_operations', 'chronic_str', 'sti', \
        'sti_str', 'treatment', 'treatment_date', 'hiv', 'tuberculosis', \
        'hepatitis_b', 'hepatitis_c', 'syphilis', 'others', \
        'last_fluorography_date', 'last_fluorography_date_result', \
        'tetanus', 'measles', 'rubella', 'flu', 'diphtheria', \
        'other_vaccnation',
        widgets = {
            'treatment_date': DateInput(),
            'last_fluorography_date': DateInput()
        }


class DoctorExaminationsTherapistForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsTherapist
        fields = 'date', 'result', 'ecg_date', 'ecgresult', \
                'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput(),
            'ecg_date': DateInput()
        }


class DoctorExaminationsDentistForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsDentist
        fields = 'date', 'result', 'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput()
        }

class DoctorExaminationsPediatorForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsPediator
        fields = 'date', 'result', 'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput()
        }

class DoctorExaminationsSpecialistForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsSpecialist
        fields = 'date', 'result', 'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput()
        }

class DoctorExaminationsOphthalmologistForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsOphthalmologist
        fields = 'date', 'result', 'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput()
        }

class DoctorExaminationsObstetricianGynecologistForm(forms.ModelForm):
    class Meta:
        model = DoctorExaminationsObstetricianGynecologist
        fields = 'date', 'result', 'med_org', 'doctor_fio',
        widgets = {
            'date': DateInput()
        }


class CurrentPregnancyinfoForm(forms.ModelForm):
    class Meta:
        model = CurrentPregnancyinfo
        fields = 'pregnancy', 'try_number', 'embryo_transfer', 'embryo_date', \
                'embryo_number', 'mother_age', 'upcoming_births', 'pregnancy_1', \
                'fetus_number', 'last_menstruation', 'first_uzi', 'gestation_period', \
                'pregnancy_accounting_date', 'pregnancy_accounting_period', \
                'fetus_first_stirring', 'suppose_birth_date',
        widgets = {
            'embryo_date': DateInput(),
            'last_menstruation': DateInput(),
            'first_uzi': DateInput(),
            'pregnancy_accounting_date': DateInput(),
            'fetus_first_stirring': DateInput(),
            'suppose_birth_date': DateInput()
        }


class FirstExaminationForm(forms.ModelForm):
    class Meta:
        model = FirstExamination
        fields = 'date', 'complaints', 'complaints_str', 'skin_condition', 'subcutaneous_fat_severity', \
                'edema', 'edema_str', 'lower_extremities_varicose', 'enlarged_lymph_nodes', \
                'lymph_nodes_str', 'mammary', 'mammary_str', 'nipples', 'nipples_str', 'heart_tones', \
                'pulse', 'rh_blood_pressure', 'lh_blood_pressure', 'lungs_auscultation', 'fetus_stirring', \
                'fetus_heartbeat', 'abdominal_circumference', 'fetal_position', 'to_pelvis_entrance', \
                'adjacent_part', 'cervix_examination', 'cervix_visual_changes', 'external_genitalia', \
                'external_genitalia_str', 'vagina', 'vagina_str', 'cervix', 'cervix_length', 'cervix_deviations', \
                'mucosa', 'external_pharynx', 'uterus_body', 'uterus_body', 'uterus_body_str', 'left_appendages', \
                'left_appendages_str', 'right_appendages', 'right_appendages_str', 'exostoses', 'exostoses_str', \
                'cervical_canal_separated', 'vagina_separated', 'gestation_period_weeks', 'analisys', \
                'appointments', 'date_diagnosis',
        widgets = {
            'date': DateInput(),
            'date_diagnosis': DateInput()
        }

class UltrasoundFisrtTrimesterForm(forms.ModelForm):
    class Meta:
        model = UltrasoundFisrtTrimester
        fields = 'date', 'number_of_fetuses', 'choriality_amniality', \
                'egg_diameter', 'ktr', 'choriality_amniality', 'chorion_location', \
                'pathology', 'pathology_str', 'gestation_period_weeks',
        widgets = {
            'date': DateInput()
        }


class ComprehensiveRiskAssessmentForm(forms.ModelForm):
    class Meta:
        model = ComprehensiveRiskAssessment
        fields = 'date', 'number_of_fetuses', 'ktr', 'tvp', \
                'choriality_amniality', 'cervicometry', \
                'uterine_pulse_index', 'vpr', 'vpr_str', \
                'papp_a', 'mom_papp_a', 'b_hgch', 'mom_b_hgch', \
                'trisomy_21', 'trisomy_18', 'trisomy_13', 'zrp', \
                'premature_birth', 'preeclampcy_34', 'preeclampcy_37', \
                'gestation_period_weeks',
        widgets = {
            'date': DateInput()
        }


class UltrasoundExamination_19_21Form(forms.ModelForm):
    class Meta:
        model = UltrasoundExamination_19_21
        fields = 'date', 'number_of_fetuses', 'pmp', 'choriality_amniality', \
                'prp', 'pathology_str', 'echo_marker_ha', 'risk_ha', 'amniotic_fluid', \
                'placenta_location', 'features', 'cervical_canal_length', 'pharynx', \
                'pharynx_str', 'gestation_period_weeks', 'invasive_prenatal_diagnosis', \
                'ipd_date', 'gestation_period_weeks', 'procedure_type', 'cardtype', \
                'consilium_result', 'result_date', 'result_str',
        widgets = {
            'date': DateInput(),
            'ipd_date': DateInput(),
            'result_date': DateInput()
        }


class UltrasoundExamination_30_34Form(forms.ModelForm):
    class Meta:
        model = UltrasoundExamination_30_34
        fields = 'date', 'presentation', 'amniotic_fluid', 'placenta_location', \
                'choriality_amniality', 'gestation_period_weeks', 'uzi_date', 'uzi_result', \
                'features', 'cervical_canal_length', 'pharynx', 'pharynx_str', 'gestation_period_result', \
                'invasive_prenatal_diagnosis', 'ipd_date', 'gestation_period_result_main', 'procedure_type', \
                'cariotype', 'consilium_result', 'result_date', 'result_str',
        widgets = {
            'date': DateInput(),
            'uzi_date': DateInput(),
            'ipd_date': DateInput(),
            'result_date': DateInput()
        }


class HospitalizationInformationForm(forms.ModelForm):
    class Meta:
        model = HospitalizationInformation
        fields = 'date_start', 'date_finish', 'hosp_type', 'med_org', \
                'diagnosis', 'date', \
                'prenatal_hospitalization', 'where', 'foundation', \
                'date_filling',
        widgets = {
            'date_start': DateInput(),
            'date_finish': DateInput(),
            'date': DateInput(),
            'date_filling': DateInput()
        }


class TurnoutScheduleForm(forms.ModelForm):
    class Meta:
        model = TurnoutSchedule
        fields = 'number', 'date', 'gestation_period_weeks',
        widgets = {
            'date': DateInput()
        }

class MODeliveryForm(forms.ModelForm):
    class Meta:
        model = MODelivery
        fields = 'delivery',


class StatisticsForm(forms.Form):
    date_from = forms.DateField(label='За период от', required=False, widget=DateInput())
    date_to = forms.DateField(label='До', required=False, widget=DateInput())
    
    age_from = forms.IntegerField(label='Возраст от', required=False, min_value=1, max_value=99)
    age_to = forms.IntegerField(label='До', required=False, min_value=1, max_value=99)

