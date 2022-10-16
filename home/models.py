from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator
from .choices import *


class Patient(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name   = models.CharField("Имя", max_length=50)
    last_name    = models.CharField("Фамилия", max_length=50)
    father_name  = models.CharField("Отчество", max_length=50, blank=True)
    gender       = models.CharField('Пол', max_length=1, choices=GENDERS, default='f')
    telephone    = PhoneNumberField('Телефонный номер', blank=True, null=True)
    email        = models.EmailField('Email', max_length=60, blank=True, null=True)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-date_updated']
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name} {self.father_name}"


##### Medical Forms #####

class MedicalCard(models.Model):
    # personal data
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='card')
    date_of_birth= models.DateField('Дата рождения', default='2000-01-12', blank=True, null=True)
    age = models.PositiveSmallIntegerField('Полных лет', validators=[MaxValueValidator(99)], blank=True, null=True)
    residence_address = models.CharField('Адрес проживания', max_length=100, blank=True, null=True)
    registration_address = models.CharField('Адрес регистрции', max_length=100, blank=True, null=True)
    home_phone    = PhoneNumberField('Домашний телефон', max_length=20, blank=True, null=True)
    work_phone    = PhoneNumberField('Рабочий телефон', max_length=20, blank=True, null=True)
    marital_status = models.CharField('Брачное состояние', default='', choices=MARITAL_STATUS, max_length=1, blank=True, null=True)
    trusted_person_fio = models.CharField("ФИО доверенного лица", max_length=300, blank=True, null=True)
    trusted_person_phone = PhoneNumberField('Мобильный телефон', max_length=20, blank=True, null=True)
    oms_policy   = models.CharField('Полис ОМС', max_length=16, blank=True, null=True)
    snils        = models.CharField('СНИЛС', max_length=11, blank=True, null=True)
    maternity_leave_start = models.DateField('Начало декретного отпуска', blank=True, null=True)
    maternity_leave_finish = models.DateField('Окончание декретного отпуска', blank=True, null=True)
    disability_certificate = models.CharField('Номер отпуска по беременности и родам', max_length=16, blank=True, null=True)
    generic_certificate_number = models.CharField('Номер родового сертификата', max_length=20, blank=True, null=True)
    generic_certificate_date = models.DateField('Дата выдачи родового сертификата', blank=True, null=True)
    
    # allergy
    allergy = models.BooleanField('Аллергическая реакция', default=False, null=True)
    allergy_description = models.CharField('Описание аллергической реакции', default='', max_length=100, blank=True, null=True)
    
    # blood fields
    mother_blood_group = models.CharField('Группа крови', max_length=1, choices=BLOOD, blank=True, null=True)
    mother_blood_rh = models.CharField('Rh-фактор', max_length=1, choices=RH, blank=True, null=True)
    mother_date_of_determination = models.DateField('Дата определения', default='2022-01-01', blank=True, null=True)
    father_blood_group = models.CharField('Группа крови', max_length=1, choices=BLOOD, blank=True, null=True)
    father_blood_rh = models.CharField('Rh-фактор', max_length=1, choices=RH, blank=True, null=True)
    father_date_of_determination = models.DateField('Дата определения', default='2022-01-01', blank=True, null=True)
    
    # pregnancy data
    pregnancy_count = models.PositiveSmallIntegerField('Беременность по счету', blank=True, validators=[MaxValueValidator(99)], null=True)
    births_by_term = models.CharField('Данные роды по сроку', max_length=200, blank=True, null=True)
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    first_visit_date = models.DateField('Дата первой явки (взятие на учет)', blank=True, null=True)
    
    # birth data
    childbirth_date = models.DateField('Дата родов', blank=True, null=True)
    childbirth_gestation_period = models.PositiveSmallIntegerField('Срок беременности родов (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    med_org      = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True, null=True)
    
    # diagnosis
    diagnosis = models.CharField('Основной диагноз', max_length=200, blank=True, null=True)
    complications = models.CharField('Осложнения данной беременности', max_length=200, blank=True, null=True)
    
    # other diseases
    somatic_diseases = models.CharField('Соматические заболевания', max_length=200, blank=True, null=True)
    gynecological_diseases = models.CharField('Гинекологические  заболевания', max_length=200, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    
    class Meta:
        verbose_name = 'Медицинская карта'
        verbose_name_plural = 'Медицинские карты'
    
    def __str__(self) -> str:
        return self.patient.get_full_name()


class ObstetricRisk(models.Model):
    card = models.ForeignKey(MedicalCard, on_delete=models.CASCADE, related_name='risks')
    visit = models.CharField('Срок явки', max_length=5, choices=VISIT, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Акушерский риск'
        verbose_name_plural = 'Акушерские риски'
    
    def __str__(self) -> str:
        return self.card.__str__() + ' ' + self.visit


class ComplicationRisk(models.Model):
    risk = models.ForeignKey(ObstetricRisk, on_delete=models.CASCADE, related_name='complications')
    complication_risk = models.CharField('Риск осложнениний', max_length=150, blank=True, null=True)
    risk_value = models.PositiveSmallIntegerField('Значение индивидуального риска', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Риск осложнения'
        verbose_name_plural = 'Риски осложнений'
    
    def __str__(self) -> str:
        return self.complication_risk


class PregnancyOutcome(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pregnancy_outcome')
    pregnancy_count = models.PositiveSmallIntegerField('Беременность по счету', validators=[MaxValueValidator(99)], unique=True)
    childbirth_date = models.DateTimeField('Дата исхода беременности', blank=True, null=True)
    pregnancy_outcome = models.CharField('Исход беременности', max_length=10, choices=PREGNANCY_OUTCOME, blank=True, null=True)
    
    if_childbirth = models.CharField('Роды', max_length=10, choices=CHILDBIRTH, blank=True, null=True)
    
    if_abortion = models.CharField('Аборт', max_length=10, choices=ABORTION, blank=True, null=True)
    
    # if death
    death_time = models.DateTimeField('Смерть', blank=True, null=True)
    disease = models.CharField('Причина смерти (шифр по МКБ-10)', max_length=10, blank=True, null=True)
    
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    number_of_fetuses = models.PositiveSmallIntegerField('Количество плодов', validators=[MaxValueValidator(10)], blank=True, null=True)

    class Meta:
        verbose_name = 'Исход беременности'
        verbose_name_plural = 'Исходы беременностей'
        ordering = ['pregnancy_count']
    
    def __str__(self) -> str:
        return self.patient.get_full_name() + " count: " + str(self.pregnancy_count)


# Наблюдения во время настоящей беременности

class CurrentPregnancy(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='current_pregnancy')


class Pelviometry(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='pelviometry')
    date = models.DateField('Дата', blank=True, null=True)
    dsp = models.PositiveSmallIntegerField('D.sp. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    dcr = models.PositiveSmallIntegerField('D.cr. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    dtroch = models.PositiveSmallIntegerField('D.troch. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    dext = models.PositiveSmallIntegerField('D.ext. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    cvera = models.PositiveSmallIntegerField('C.vera. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    cdiag = models.PositiveSmallIntegerField('C.diag. (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    solovyov_index = models.PositiveSmallIntegerField('Индекс соловьева (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    michaelis_rhombus_x = models.PositiveSmallIntegerField('Ромб Михаэлиса X (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    michaelis_rhombus_y = models.PositiveSmallIntegerField('Ромб Михаэлиса Y (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    pelvis_dimensions = models.PositiveSmallIntegerField('Дополнительные размеры таза (по показаниям)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class PregnantWomanMonitoring(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='pregnant_woman_monitoring')
    date = models.DateField('Дата', blank=True, null=True)
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    complaints = models.CharField('Жалобы', max_length=1000, blank=True, null=True)
    weight_gain = models.PositiveIntegerField('Прибака к массе тела (+г)', validators=[MaxValueValidator(100000)], blank=True, null=True)
    systolic_blood_pressure = models.CharField('Артериальное даавление систолическое (мм.рт.ст.)', max_length=50, blank=True, null=True)
    blood_pressure_diastolic = models.CharField('Артериальное даавление диастолическое (мм.рт.ст.)', max_length=50, blank=True, null=True)
    pulse = models.CharField('Пульс (уд/мин)', max_length=50, blank=True, null=True)
    fetus_heartbeat = models.CharField('Сердцебиение плода (уд/мин) (>12 недель)', max_length=50, blank=True, null=True)
    fetus_stirring = models.CharField('Шевеление плода: (>16 недель)', max_length=10, choices=FETUS_STIRRING, blank=True, null=True)
    fundal_height = models.PositiveSmallIntegerField('Высота дна матки (см) (>20 недель)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    abdominal_circumference = models.PositiveSmallIntegerField('Окружность живота (см) (>20 недель)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    fetal_position = models.CharField('Положение плода', max_length=10, choices=FETAL_POSITION, blank=True, null=True)
    to_pelvis_entrance = models.CharField('Над входом в малый таз', max_length=10, choices=PELVIS_ENTRANCE, blank=True, null=True)
    adjacent_part = models.CharField('Предлежащая часть', max_length=10, choices=ADJACENT_PART, blank=True, null=True)
    protein_in_urine = models.CharField('Белок в моче (-,1+,2+,3+)', max_length=50, blank=True, null=True)
    hemoglobin = models.CharField('Гемоглобин (г/л)', max_length=50, blank=True, null=True)
    glucose = models.CharField('Глюкоза, ммоль/л', max_length=50, blank=True, null=True)
    ttg = models.CharField('ТТГ , мкМЕ/л', max_length=50, blank=True, null=True)
    s_agalactiae = models.CharField('S. agalactiae в мазке', max_length=1000, blank=True, null=True)
    bacterioscopic_smears_examination = models.CharField('Бактериоскопическое исследование мазков', max_length=1000, blank=True, null=True)
    cervix_сytological_examination = models.CharField('Цитологическое исследование микропрепарата шейки матки', max_length=1000, blank=True, null=True)
    urine_culture = models.CharField('Посев мочи на бессимптомную бактериурию', max_length=1000, blank=True, null=True)
    fetal_development_assessment_11_14 = models.CharField('Комплексная оценка антенатального развития плода в 11-14 недель (скрининг 1-ого триместра)', max_length=1000, blank=True, null=True)
    fetal_development_assessment_19_21 = models.CharField('Оценка антенатального развития плода в 19-21 неделю (скрининг 2-ого триместра)', max_length=1000, blank=True, null=True)
    ultrasound_cervicometry = models.CharField('УЗИ-цервикометрия', max_length=1000, blank=True, null=True)
    fetal_ultrasound = models.CharField('УЗИ плода/плодов по показаниям', max_length=1000, blank=True, null=True)
    invasive_diagnostics = models.CharField('Инвазивная диагностика при высоком риске хромосомных аномалий (ХА)', max_length=200, blank=True, null=True)
    fetal_cardiotocography = models.CharField('Кардиотокография плода/плодов (КТГ)', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class AppointmentList(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='appointments')
    visit_number = models.PositiveSmallIntegerField('Номер посещения', validators=[MaxValueValidator(100)], blank=True, null=True)
    date = models.DateField('Дата', blank=True, null=True)
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    analysis = models.CharField('Анализ', max_length=1000, blank=True, null=True)
    appointment = models.CharField('Назначения', max_length=1000, blank=True, null=True)
    disability_certificate = models.CharField('Листок нетрудоспособности', max_length=1000, blank=True, null=True)
    next_visit_date = models.DateField('Дата', blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class TakingMedications(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='medications')
    date_start = models.DateField('Дата начала приема препарата', blank=True, null=True)
    date_finish = models.DateField('Дата окончания приема препарата', blank=True, null=True)
    indications = models.CharField('Показания', max_length=1000, blank=True, null=True)
    dose_duration = models.CharField('Доза/Длительность', max_length=1000, blank=True, null=True)
    side_effects = models.CharField('Побочные эффекты', max_length=1000, blank=True, null=True)


class AntibodiesDetermination(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='antibodies')
    date = models.DateField('Дата', blank=True, null=True)
    treponema_antibodies = models.CharField('Антитела к бледной трепонеме', max_length=1000, blank=True, null=True)
    hiv_antibodies = models.CharField('Антитела классов M, G к ВИЧ ½ и антиген р24', max_length=1000, blank=True, null=True)
    hbsag_antibodies = models.CharField('HBsAg или антитела к HBsAg', max_length=1000, blank=True, null=True)
    anti_hcv = models.CharField('anti-HCV IgG и anti-HCV IgM', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class RubellaVirus(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='rubella')
    date = models.DateField('Дата', blank=True, null=True)
    lgm = models.CharField('lgM', max_length=1000, blank=True, null=True)
    lgg = models.CharField('lgG', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class AntiresusBodies(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='antiresus_bodies')
    date = models.DateField('Дата', blank=True, null=True)
    antiresus_bodies = models.CharField('Антирезусные тела', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class BloodAnalysis(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='blood_analysis')
    date = models.DateField('Дата', blank=True, null=True)
    hemoglobin = models.CharField('Гемоглобин, г/л', max_length=1000, blank=True, null=True)
    red_blood_cells = models.CharField('Эритроциты, 10^12/л', max_length=1000, blank=True, null=True)
    color_indicator = models.CharField('Цветовой показатель, %', max_length=1000, blank=True, null=True)
    reticulocytes = models.CharField('Ретикулоциты, %', max_length=1000, blank=True, null=True)
    platelets = models.CharField('Тромбоциты, 10^9/л', max_length=1000, blank=True, null=True)
    white_blood_cells = models.CharField('Лейкоциты, 10^9/л', max_length=1000, blank=True, null=True)
    myelocytes = models.CharField('Миелоциты, %', max_length=1000, blank=True, null=True)
    metamyelocytes = models.CharField('Метамиелоциты, %', max_length=1000, blank=True, null=True)
    stick_core = models.CharField('Палочкоядерные, %', max_length=1000, blank=True, null=True)
    segmentonuclear = models.CharField('Сегметоядерные, %', max_length=1000, blank=True, null=True)
    eosinophils = models.CharField('Эозинофилы, %', max_length=1000, blank=True, null=True)
    basophils = models.CharField('Базофилы, %', max_length=1000, blank=True, null=True)
    lymphocytes = models.CharField('Лимфоциты , %', max_length=1000, blank=True, null=True)
    monocytes = models.CharField('Моноциты, %', max_length=1000, blank=True, null=True)
    soe = models.CharField('СОЭ, мм/ч', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class BiochemicalBloodAnalysis(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='biochemical_blood')
    date = models.DateField('Дата', blank=True, null=True)
    total_bilirubin = models.CharField('Общий билирубин, мкмоль/л', max_length=1000, blank=True, null=True)
    direct_bilirubin = models.CharField('Прямой билирубин, мкмоль/л', max_length=1000, blank=True, null=True)
    total_protein = models.CharField('Общий белок, г/л', max_length=1000, blank=True, null=True)
    alt = models.CharField('АЛТ, ЕД/л', max_length=1000, blank=True, null=True)
    ast = models.CharField('АСТ, ЕД/л', max_length=1000, blank=True, null=True)
    glucose = models.CharField('Глюкоза, ммоль/л', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class Coagulogram(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='сoagulogram')
    date = models.DateField('Дата', blank=True, null=True)
    platelet_count = models.CharField('Количество тромбоцитов, 10^9/л', max_length=1000, blank=True, null=True)
    astv = models.CharField('АЧТВ, сек.', max_length=1000, blank=True, null=True)
    fibrinogen = models.CharField('Фибриноген, г/л', max_length=1000, blank=True, null=True)
    prothrombin_time = models.CharField('Протромбиновое время, %', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class GlucoseToleranceTest(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='glucose_test')
    date = models.DateField('Дата', blank=True, null=True)
    period = models.CharField('Срок (недель)', max_length=1000, blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class ThyroidStimulatingHormone(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='ts_hormonr')
    date = models.DateField('Дата', blank=True, null=True)
    period = models.CharField('Срок (недель)', max_length=1000, blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class Smears(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='smears')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От результатов отсказалась', default=False, null=True)


class BacterioscopicSmearsExamination(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='bacterio_smears')
    date = models.DateField('Дата', blank=True, null=True)
    # locus C
    c_white_blood_cells = models.CharField('Лейкоциты', max_length=1000, blank=True, null=True)
    c_epithelium = models.CharField('Эпителий', max_length=1000, blank=True, null=True)
    c_key_cels = models.CharField('Ключевые клетки', max_length=1000, blank=True, null=True)
    c_candida = models.CharField('Кандиды', max_length=1000, blank=True, null=True)
    c_trichomonads = models.CharField('Трихомонады', max_length=1000, blank=True, null=True)
    c_gonococci = models.CharField('Гонококки', max_length=1000, blank=True, null=True)
    c_ph = models.CharField('pH', max_length=1000, blank=True, null=True)
    # locus V
    v_white_blood_cells = models.CharField('Лейкоциты', max_length=1000, blank=True, null=True)
    v_epithelium = models.CharField('Эпителий', max_length=1000, blank=True, null=True)
    v_key_cels = models.CharField('Ключевые клетки', max_length=1000, blank=True, null=True)
    v_candida = models.CharField('Кандиды', max_length=1000, blank=True, null=True)
    v_trichomonads = models.CharField('Трихомонады', max_length=1000, blank=True, null=True)
    v_gonococci = models.CharField('Гонококки', max_length=1000, blank=True, null=True)
    v_ph = models.CharField('pH', max_length=1000, blank=True, null=True)
    # locus U
    u_white_blood_cells = models.CharField('Лейкоциты', max_length=1000, blank=True, null=True)
    u_epithelium = models.CharField('Эпителий', max_length=1000, blank=True, null=True)
    u_key_cels = models.CharField('Ключевые клетки', max_length=1000, blank=True, null=True)
    u_candida = models.CharField('Кандиды', max_length=1000, blank=True, null=True)
    u_trichomonads = models.CharField('Трихомонады', max_length=1000, blank=True, null=True)
    u_gonococci = models.CharField('Гонококки', max_length=1000, blank=True, null=True)
    u_ph = models.CharField('pH', max_length=1000, blank=True, null=True)


class CervixCytologicalExamination(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='cervix_exam')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class UrineAnalysis(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='urine')
    date = models.DateField('Дата', blank=True, null=True)
    amount = models.CharField('Количество, мл', max_length=1000, blank=True, null=True)
    ph = models.CharField('pH', max_length=1000, blank=True, null=True)
    density = models.CharField('Плотность', max_length=1000, blank=True, null=True)
    u_white_blood_cells = models.CharField('Лейкоциты', max_length=1000, blank=True, null=True)
    red_blood_cells = models.CharField('Эритроциты', max_length=1000, blank=True, null=True)
    protein = models.CharField('Белок, г/л', max_length=1000, blank=True, null=True)
    cylinders = models.CharField('Цилиндры', max_length=1000, blank=True, null=True)
    salt = models.CharField('Соли', max_length=1000, blank=True, null=True)


class UrineSowing(models.Model):
    current_pregnancy = models.ForeignKey(CurrentPregnancy, on_delete=models.CASCADE, related_name='urine_sowing')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Сведения о пациентке

class PatientInformation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_information')
    
    # Врожденные пороки развития
    congenital_malformations = models.BooleanField('Врожденные пороки развития', default=False, null=True)
    congenital_malformations_str = models.CharField('Перечисление врожденных пороков', max_length=200, blank=True, null=True)
    
    # Рост
    height = models.PositiveSmallIntegerField('Рост (см)', validators=[MaxValueValidator(999)], blank=True, null=True)
    
    # Масса тела
    mass = models.PositiveSmallIntegerField('Масса тела при поставке на учет (кг)', validators=[MaxValueValidator(999)], blank=True, null=True)
    
    # ИМТ
    imt = models.PositiveSmallIntegerField('ИМТ (кг/м2)', blank=True, null=True) # auto
    
    # Риск преэклампсии
    preeclampsia_risk = models.CharField('Риск преэклампсии', max_length=1, choices=RISK_LEVEL, blank=True, null=True)
    preeclampsia_risk_str = models.CharField('Значение риска', max_length=200, blank=True, null=True)
    
    # Риск преждевременных родов
    premature_birth_risk = models.CharField('Риск преждевременных родов', max_length=1, choices=RISK_LEVEL, blank=True, null=True)
    premature_birth_risk_str = models.CharField('Значение риска', max_length=200, blank=True, null=True)
    
    # Риск задержки роста плода
    growth_retardation_risk = models.CharField('Риск задержки роста плода', max_length=1, choices=RISK_LEVEL, blank=True, null=True)
    growth_retardation_risk_str = models.CharField('Значение риска', max_length=200, blank=True, null=True)
    
    # Риск тромбоэболических осложнений
    thromboembolic_complications = models.CharField('Риск тромбоэболических осложнений', max_length=1, choices=RISK_LEVEL, blank=True, null=True)
    thromboembolic_complications_str = models.CharField('Значение риска', max_length=200, blank=True, null=True)
    
    # Другие риски
    another_risks = models.CharField('Другие риски', max_length=1, choices=RISK_LEVEL, blank=True, null=True)
    another_risks_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Детские инфекции
    child_infections = models.BooleanField('Детские инфекции', default=False, null=True)
    child_infections_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Диспансерский учет
    dispensary_accounting = models.CharField('Диспансерский учет', max_length=1, choices=REGISTERED, blank=True, null=True)
    dispensary_accounting_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Травмы/операции
    injures_operations = models.BooleanField('Травмы/операции', default=False, null=True)
    injures_operations_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Соматические заболевания
    somatic_diseases = models.BooleanField('Соматические заболевания', default=False, null=True)
    somatic_diseases_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Социально значимые инфекции
    socially_significant_infections = models.CharField('Социально значимые инфекции', max_length=200, blank=True, null=True) ###
    socially_significant_infections_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # ВИЧ-статус
    hiv_status = models.CharField('ВИЧ-статус', max_length=1, choices=IS_POSITIVE, blank=True, null=True)
    date = models.DateField('Дата (при наличии)', blank=True, null=True)
    epidnomer = models.CharField('Эпидномер (при наличии)', max_length=10, blank=True, null=True)
    
    # Антиретровирусная терапия
    antiretroviral_therapy = models.CharField('Антиретровирусная терапия во время беременности', max_length=200, blank=True, null=True)
    
    # Наследственные заболевания
    hereditary_diseases = models.BooleanField('Наследственные заболевания', default=False, null=True)
    hereditary_diseases_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Гемотрансфузии
    blood_transfusions = models.BooleanField('Гемотрансфузии', default=False, null=True)
    year = models.CharField('Год', max_length=4, blank=True, null=True)
    
    # Последняя флюорография
    last_fluorography_date = models.DateField('Последняя флюорография (дата)', blank=True, null=True)
    last_fluorography_date_result = models.CharField('Последняя флюорография (результат)', max_length=200, blank=True, null=True)
    
    # Вредные привычки
    bad_habits = models.BooleanField('Вредные привычки', default=False, null=True)
    smoking = models.CharField('Курение (в день)', max_length=10, blank=True, null=True, choices=SMOKING)
    alcohol = models.CharField('Алкоголь', max_length=10, blank=True, null=True, choices=ALCOHOL)
    alcohol_type = models.CharField('Вид алкоголя', max_length=200, blank=True, null=True)
    drugs = models.CharField('Наркотики (название)', max_length=200, blank=True, null=True)
    
    # Профессиональные вредности
    occupational_hazards = models.BooleanField('Профессиональные вредности', default=False, null=True)
    occupational_hazards_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    # Сведения о прививках
    tetanus = models.BooleanField('Столбняк', default=False, null=True)
    measles = models.BooleanField('Корь', default=False, null=True)
    rubella = models.BooleanField('Краснуха', default=False, null=True)
    chickenpox = models.BooleanField('Ветряная оспа', default=False, null=True)
    flu = models.BooleanField('Грипп', default=False, null=True)
    HPV = models.BooleanField('ВПЧ', default=False, null=True)
    hepatitis_B = models.BooleanField('гепатит В', default=False, null=True)
    other_vaccnation = models.CharField('Другие прививки', max_length=200, blank=True, null=True)
    
    # менструация
    year_start = models.CharField('Год начала', max_length=4, blank=True, null=True)
    profusion = models.CharField('Обильность', max_length=10, blank=True, null=True, choices=PROFUSION)
    painfulness = models.CharField('Болезненность', max_length=10, blank=True, null=True, choices=PAINFULNESS)
    regularity = models.CharField('Регулярность', max_length=10, blank=True, null=True, choices=REGULARITY)
    
    # Половая жизнь
    sexual_life = models.CharField('Половая жизнь (год)', max_length=4, blank=True, null=True)
    
    # Контрацепция
    contraception_method = models.CharField('Контрацепция (метод)', max_length=200, blank=True, null=True)
    contraception_period = models.CharField('Контрацепция (период)', max_length=200, blank=True, null=True)
    
    # Гинекологические заболевания
    diseases_operations = models.CharField('Гинекологические заболевания, операции', max_length=200, blank=True, null=True)
    disease_date = models.DateField('Дата', blank=True, null=True)
    
    # Инфекции, передаваемые половым путем
    sti = models.BooleanField('Инфекции, передаваемые половым путем', default=False, null=True)
    treatment = models.CharField('Лечение', max_length=200, blank=True, null=True)
    treatment_date = models.DateField('Дата', blank=True, null=True)
    
    # Последнее обследование молочных желез
    year_mammary = models.CharField('Год обследования', max_length=4, blank=True, null=True)
    mammary_method = models.CharField('Метод', max_length=200, blank=True, null=True)
    mammary_result = models.CharField('Результат', max_length=200, blank=True, null=True)
    
    # Последнее цитологическое исследование микропрепарата шейки матки
    year_cervix = models.CharField('Год обследования', max_length=4, blank=True, null=True)
    cervix_method = models.CharField('Метод', max_length=200, blank=True, null=True)
    cervix_result = models.CharField('Результат', max_length=200, blank=True, null=True)
    
    # Подтверждение врача
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class CarvixScar(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='carvix')
    date = models.DateField('Дата', blank=True, null=True)
    operation_name = models.CharField('Название операции', max_length=200, blank=True, null=True)
    if_caesarean = models.CharField('При кесаревом сечении', max_length=200, blank=True, null=True)
    scar_localization = models.CharField('Локализация рубца на матке', max_length=200, blank=True, null=True)
    operation_features = models.CharField('Особенности операции, п/о периода', max_length=200, blank=True, null=True)


class FatherInfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='father')
    age = models.PositiveSmallIntegerField('Полных лет', validators=[MaxValueValidator(99)], blank=True, null=True)
    height = models.PositiveSmallIntegerField('Рост (см)', validators=[MaxValueValidator(999)], blank=True, null=True)
    mass = models.PositiveSmallIntegerField('Масса тела при поставке на учет (кг)', validators=[MaxValueValidator(999)], blank=True, null=True)
    imt = models.PositiveSmallIntegerField('ИМТ (кг/м2)', blank=True, null=True) # auto
    bad_habits = models.CharField('Вредные привычки', max_length=10, blank=True, null=True, choices=BAD_HABITS)
    sti = models.BooleanField('Инфекции, передаваемые половым путем', default=False, null=True)
    sti_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    treatment = models.CharField('Лечение', max_length=200, blank=True, null=True)
    treatment_date = models.DateField('Дата', blank=True, null=True)

    # Социально значимые инфекции
    hiv = models.BooleanField('ВИЧ', default=False, null=True)
    tuberculosis = models.BooleanField('Туберкулез', default=False, null=True)
    hepatitis_b = models.BooleanField('Гепатит В', default=False, null=True)
    hepatitis_c = models.BooleanField('Гепатит С', default=False, null=True)
    syphilis = models.BooleanField('Сифилис', default=False, null=True)
    others = models.BooleanField('Другие', default=False, null=True)

    last_fluorography_date = models.DateField('Последняя флюорография (дата)', blank=True, null=True)
    last_fluorography_date_result = models.CharField('Последняя флюорография (результат)', max_length=200, blank=True, null=True)

    # Сведегия о прививках
    tetanus = models.BooleanField('Столбняк', default=False, null=True)
    measles = models.BooleanField('Корь', default=False, null=True)
    rubella = models.BooleanField('Краснуха', default=False, null=True)
    flu = models.BooleanField('Грипп', default=False, null=True)
    diphtheria = models.BooleanField('Дифтерия', default=False, null=True)
    other_vaccnation = models.CharField('Другие прививки', max_length=200, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Осмотры врачей специалистов

class DoctorExaminations(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_examination')
    date = models.DateField('Дата осмотра', blank=True, null=True)
    result = models.CharField('Результаты осмотра, заключение', max_length=1000, blank=True, null=True)
    
    ecg_date = models.DateField('Дата ЭКГ', blank=True, null=True)
    ecgresult = models.CharField('Результаты ЭКГ', max_length=1000, blank=True, null=True)
    
    med_org = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True)
    doctor_fio = models.CharField('Ф.И.О. врача, проводившего осмотр', max_length=300, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Сведения о настоящей беременности

class CurrentPregnancyinfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pregnancy_info')
    pregnancy = models.CharField('Беременность', max_length=1, choices=PREGNANCY, blank=True)
    # if ВРТ
    try_number = models.PositiveSmallIntegerField('Номер попытки', validators=[MaxValueValidator(999)], blank=True, null=True)
    embryo_transfer = models.CharField('Перенос эмбрионов', max_length=1, choices=EMBRYO, blank=True)
    embryo_date = models.DateField('Дата переноса эмбриона', blank=True, null=True)
    embryo_number = models.PositiveSmallIntegerField('Число перенесенных эмбрионов', validators=[MaxValueValidator(999)], blank=True, null=True)
    mother_age = models.PositiveSmallIntegerField('Число перенесенных эмбрионов', validators=[MaxValueValidator(999)], blank=True, null=True)
    
    upcoming_births = models.CharField('Предстоящие роды', max_length=1, choices=UPCOMING_BIRTH, blank=True)
    pregnancy_1 = models.CharField('Беременность', max_length=1, choices=PREGNANCY_1, blank=True)
    fetus_number = models.PositiveSmallIntegerField('Количество плодов', validators=[MaxValueValidator(9)], blank=True, null=True)
    last_menstruation = models.DateField('Последняя менструация', blank=True, null=True)
    
    first_uzi = models.DateField('Дата 1-го УЗИ', blank=True, null=True)
    gestation_period = models.PositiveSmallIntegerField('Срок беременности (недель)', validators=[MaxValueValidator(99)], blank=True, null=True)
    
    pregnancy_accounting_date = models.DateField('Учет по беременности', blank=True, null=True)
    pregnancy_accounting_period = models.PositiveSmallIntegerField('Срок (недель)', validators=[MaxValueValidator(99)], blank=True, null=True)
    
    fetus_first_stirring = models.DateField('Первое шевеление плода', blank=True, null=True)
    suppose_birth_date = models.DateField('Предполагаемая дата родов', blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class FirstExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='first_examination')
    date = models.DateField('Дата осмотра', blank=True, null=True)
    complaints = models.BooleanField('Жалобы', default=False, null=True)
    complaints_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    subcutaneous_fat_severity = models.CharField('Распределение и выраженность подкожной жировой клетчатки', max_length=1, choices=FAT_SEVERITY, blank=True)
    edema = models.BooleanField('Отеки', default=False, null=True)
    edema_str = models.CharField('Дополнительная информация (локация, выраженнось)', max_length=200, blank=True, null=True)
    lower_extremities_varicose = models.BooleanField('Варикозное расширение вен нижних конечностей', default=False, null=True)
    enlarged_lymph_nodes = models.BooleanField('Увеличение лимфатических узлов', default=False, null=True)
    lymph_nodes_str = models.CharField('Дополнительная информация (локализация, болезненность)', max_length=200, blank=True, null=True)
    # Осмотр и пальпация
    mammary = models.CharField('Осмотр и пальпация молочных желез', max_length=1, choices=MAMMARY, blank=True)
    mammary_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Соски
    nipples = models.CharField('Осмотр и пальпация молочных желез', max_length=1, choices=NIPPLES, blank=True)
    nipples_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    heart_tones = models.CharField('Тоны сердца', max_length=200, blank=True, null=True)
    pulse = models.CharField('Пульс (уд/мин)', max_length=50, blank=True, null=True)
    rh_blood_pressure = models.CharField('Артериальное даавлениена правой руке (мм.рт.ст.)', max_length=50, blank=True, null=True)
    lh_blood_pressure = models.CharField('Артериальное даавление на левой руке (мм.рт.ст.)', max_length=50, blank=True, null=True)
    fetus_stirring = models.CharField('Шевеление плода: (>16 недель)', max_length=10, choices=FETUS_STIRRING, blank=True, null=True)
    fetus_heartbeat = models.CharField('Сердцебиение плода (уд/мин) (>12 недель)', max_length=50, blank=True, null=True)
    abdominal_circumference = models.PositiveSmallIntegerField('Окружность живота (см) (>20 недель)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    fetal_position = models.CharField('Положение плода', max_length=10, choices=FETAL_POSITION, blank=True, null=True)
    to_pelvis_entrance = models.CharField('Над входом в малый таз (после 34 недель)', max_length=10, choices=PELVIS_ENTRANCE, blank=True, null=True)
    adjacent_part = models.CharField('Предлежащая часть (после 34 недель)', max_length=10, choices=ADJACENT_PART, blank=True, null=True)
    # Геникологический осмотр
    cervix_examination = models.CharField('Осмотр шейки матки в зеркалах', max_length=200, blank=True, null=True)
    cervix_visual_changes = models.CharField('Визуальные изменения', max_length=200, blank=True, null=True)
    # Влагалищное исследование
    external_genitalia = models.CharField('Наружные половые органы (указать отклонения, если есть)', max_length=200, blank=True, null=True)
    external_genitalia_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Влагалище
    vagina = models.CharField('Указать патологии (если есть)', max_length=200, blank=True, null=True)
    vagina_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Шейка матки
    cervix = models.CharField('Шейка матки', max_length=10, choices=CERVIX, blank=True, null=True)
    cervix_length = models.PositiveSmallIntegerField('Длина шейки матки (см)', validators=[MaxValueValidator(1000)], blank=True, null=True)
    cervix_deviations = models.CharField('Отклонения шейки матки', max_length=10, choices=CERVIX_DEVIATIONS, blank=True, null=True)
    mucosa = models.CharField('Слизистая', max_length=200, blank=True, null=True)
    external_pharynx = models.CharField('Наружний зев', max_length=1, choices=PHARYNX, blank=True, null=True)
    # Тело матки
    uterus_body = models.CharField('Тело матки. Увеличено до (недель беременности)', max_length=200, blank=True, null=True)
    uterus_body = models.CharField('Тело матки. Характеристика', max_length=1, choices=UTERUS, blank=True, null=True)
    uterus_body_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)

    left_appendages = models.CharField('Придатки слева', max_length=1, choices=APPENDAGES, blank=True, null=True)
    left_appendages_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    right_appendages = models.CharField('Придатки справа', max_length=1, choices=APPENDAGES, blank=True, null=True)
    right_appendages_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    
    exostoses = models.BooleanField('Экзостозы', default=False, null=True)
    exostoses_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    cervical_canal_separated = models.CharField('Отделяемое из цервикального канала', max_length=200, blank=True, null=True)
    vagina_separated = models.CharField('Отделяемое из влагалища', max_length=200, blank=True, null=True)
    # Диагноз
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    analisys = models.CharField('Анализы', max_length=200, blank=True, null=True)
    appointments = models.CharField('Назначения', max_length=200, blank=True, null=True)
    date_diagnosis = models.DateField('Дата', blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


##### Оценка антенатольного состояния плода #####

# Узи 1 триместра 
class UltrasoundFisrtTrimester(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='ultrasound_1')
    date = models.DateField('Дата осмотра', blank=True, null=True)
    number_of_fetuses = models.PositiveSmallIntegerField('Количество плодов', validators=[MaxValueValidator(10)], blank=True, null=True)
    choriality_amniality = models.CharField('Хориальность/амниальность', max_length=200, blank=True, null=True)
    egg_diameter = models.PositiveSmallIntegerField('Диаметр плодового яйца (мм)', validators=[MaxValueValidator(9999)], blank=True, null=True)
    ktr = models.PositiveSmallIntegerField('КТР (мм)', validators=[MaxValueValidator(9999)], blank=True, null=True)
    choriality_amniality = models.CharField('СБ эмбрионов (уд/мин / не определяется)', max_length=200, blank=True, null=True)
    chorion_location = models.CharField('Хорион расположен', max_length=200, blank=True, null=True)
    pathology = models.CharField('Патологии (если есть)', max_length=200, blank=True, null=True)
    pathology_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Комплексная оценка рисков (11-14 недель)
class ComprehensiveRiskAssessment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='risk_assessment')
    date = models.DateField('Дата осмотра', blank=True, null=True)
    # УЗИ
    number_of_fetuses = models.PositiveSmallIntegerField('Количество плодов', validators=[MaxValueValidator(10)], blank=True, null=True)
    ktr = models.PositiveSmallIntegerField('КТР (мм)', validators=[MaxValueValidator(9999)], blank=True, null=True)
    tvp = models.PositiveSmallIntegerField('ТВП (мм)', validators=[MaxValueValidator(9999)], blank=True, null=True)
    choriality_amniality = models.CharField('СБ эмбрионов (уд/мин)', max_length=200, blank=True, null=True)
    cervicometry = models.CharField('Цервикометрия (мм)', max_length=1000, blank=True, null=True)
    uterine_pulse_index = models.CharField('ПИ маточных артерий', max_length=1, choices=UTERINE_PULSE, blank=True, null=True)
    # ВПР
    vpr = models.BooleanField('ВПР', default=False, null=True)
    vpr_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Другая патология
    # БХМ
    papp_a = models.CharField('РАРР-А (мЕД/мл)', max_length=1000, blank=True, null=True)
    mom_papp_a = models.CharField('МОМ', max_length=1000, blank=True, null=True)
    b_hgch = models.CharField('бета-ХГЧ (мЕД/мл)', max_length=1000, blank=True, null=True)
    mom_b_hgch = models.CharField('МОМ', max_length=1000, blank=True, null=True)
    # Комплексный индивидуальный риск
    trisomy_21 = models.CharField('21 трисомии', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    trisomy_18 = models.CharField('18 трисомии', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    trisomy_13 = models.CharField('13 трисомии', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    zrp = models.CharField('ЗРП', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    trisomy_13 = models.CharField('ПР', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    trisomy_13 = models.CharField('ПЭ ранней (до 34 недель)', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    trisomy_13 = models.CharField('ПЭ поздний (до 37 недель)', max_length=1, choices=HIGH_LOW, blank=True, null=True)
    # Заключение
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Ультразвуковое исследование (19-21 неделя)
class UltrasoundExamination_19_21(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='uzi_exam_1')
    date = models.DateField('Дата', blank=True, null=True)
    # УЗИ
    number_of_fetuses = models.PositiveSmallIntegerField('Количество плодов', validators=[MaxValueValidator(10)], blank=True, null=True)
    pmp = models.PositiveSmallIntegerField('ПМП (г)', validators=[MaxValueValidator(9999)], blank=True, null=True)
    choriality_amniality = models.CharField('СБ плода (уд/мин / не определяется)', max_length=200, blank=True, null=True)
    prp = models.BooleanField('ПРП', default=False, null=True)
    pathology_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    echo_marker_ha = models.CharField('Эхо маркеры ХА', max_length=200, blank=True, null=True)
    risk_ha = models.CharField('Риск ХА (перерасчет при эхо-маркерах ХА)', max_length=200, blank=True, null=True)
    amniotic_fluid = models.CharField('Околоплодные воды', max_length=1, choices=AMNIOTIC_FLUID, blank=True, null=True)
    placenta_location = models.CharField('Плацента расположена', max_length=200, blank=True, null=True)
    features = models.CharField('Особенности', max_length=200, blank=True, null=True)
    # УЗИ-цервикометрия
    cervical_canal_length = models.CharField('длина сомкнутой части цервикального канала (мм)', max_length=200, blank=True, null=True)
    pharynx = models.BooleanField('Зев закрыт', blank=True, null=True)
    pharynx_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Заключение
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    invasive_prenatal_diagnosis = models.CharField('Инвазивная пренатальная диагностика (при высоком риске ХА)', max_length=200, blank=True, null=True)
    ipd_date = models.DateField('Дата', blank=True, null=True)
    
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    procedure_type = models.PositiveSmallIntegerField('Вид процедуры', validators=[MaxValueValidator(99)], blank=True, null=True)
    cardtype = models.PositiveSmallIntegerField('Кариотип/другое', validators=[MaxValueValidator(99)], blank=True, null=True)
    consilium_result = models.PositiveSmallIntegerField('Заключение консилиума (при ПРП и ХА) ', validators=[MaxValueValidator(99)], blank=True, null=True)
    result_date = models.DateField('Дата', blank=True, null=True)
    result_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Ультразвуковое исследование (30-34 неделя) 
class UltrasoundExamination_30_34(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='uzi_exam_2')
    date = models.DateField('Дата', blank=True, null=True)
    presentation = models.CharField('Предлежание', max_length=1, choices=PRESENTATION, blank=True, null=True)
    amniotic_fluid = models.CharField('Околоплодные воды', max_length=1, choices=AMNIOTIC_FLUID, blank=True, null=True)
    placenta_location = models.CharField('Плацента расположена', max_length=200, blank=True, null=True)
    choriality_amniality = models.CharField('СБ плода (уд/мин)', max_length=200, blank=True, null=True)
    # Заключение
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    # УЗИ-цервикометрия 1
    uzi_date = models.DateField('УЗИ-цервикометрия. Дата', blank=True, null=True)
    uzi_result = models.CharField('Заключение', max_length=200, blank=True, null=True)
    features = models.CharField('Особенности', max_length=200, blank=True, null=True)
    # УЗИ-цервикометрия 2
    cervical_canal_length = models.CharField('длина сомкнутой части цервикального канала (мм)', max_length=200, blank=True, null=True)
    pharynx = models.BooleanField('Зев закрыт', blank=True, null=True)
    pharynx_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    # Заключение
    gestation_period_result = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    invasive_prenatal_diagnosis = models.CharField('Инвазивная пренатальная диагностика (при высоком риске ХА)', max_length=200, blank=True, null=True)
    ipd_date = models.DateField('Дата', blank=True, null=True)
    gestation_period_result_main = models.PositiveSmallIntegerField('Срок беременности', validators=[MaxValueValidator(99)], blank=True, null=True)
    procedure_type = models.PositiveSmallIntegerField('Вид процедуры', validators=[MaxValueValidator(99)], blank=True, null=True)
    cariotype = models.CharField('Кариотип/другое', max_length=200, blank=True, null=True)
    consilium_result = models.PositiveSmallIntegerField('Заключение консилиума (при ПРП и ХА) ', validators=[MaxValueValidator(99)], blank=True, null=True)
    result_date = models.DateField('Дата', blank=True, null=True)
    result_str = models.CharField('Дополнительная информация', max_length=200, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


# Сведения о госпитализации во время беременности

class HospitalizationInformation(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='hospitalization')
    date_start = models.DateField('Дата начала', blank=True, null=True)
    date_finish = models.DateField('Дата окончания', blank=True, null=True)
    hosp_type = models.CharField('Вид', max_length=1, choices=HOSP_TYPE, blank=True, null=True)
    med_org = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True)
    diagnosis = models.CharField('Основной диагноз', max_length=200, blank=True, null=True)

    date = models.DateField('Дата', blank=True, null=True)
    doctor_confirmation_1 = models.BooleanField('Подтверждение врача', default=False, null=True)
    
    prenatal_hospitalization = models.BooleanField('Дородовая госпитализация', default=False, null=True)
    where = models.CharField('Медицинская организация', max_length=1, choices=WHERE, blank=True)
    foundation = models.CharField('Основание', max_length=200, blank=True, null=True)
    date_filling = models.DateField('Дата заполнения', blank=True, null=True)
    doctor_confirmation_2 = models.BooleanField('Подтверждение врача', default=False, null=True)


#############


class SelfMonitoringRecords(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    title = models.CharField('Краткое описание', max_length=150)
    description = models.TextField('Описание', max_length=1000, blank=True)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    def __str__(self) -> str:
        return self.title


class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='history')
    disease = models.CharField('Заболевание', max_length=270)
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    date_cured = models.DateTimeField('Дата излечения', blank=True, null=True)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    def __str__(self) -> str:
        return self.disease


class Doctor(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    patients     = models.ManyToManyField(Patient, related_name='doctors', blank=True)
    first_name   = models.CharField("Имя", max_length=50, default='usr')
    last_name    = models.CharField("Фамилия", max_length=50, default='sur')
    father_name  = models.CharField("Отчество", max_length=50, blank=True)
    cabinet      = models.CharField('Кабинет', max_length=6)
    territory    = models.CharField('Территория', max_length=25, choices=TERRITORY, default='Ульяновский')
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    med_org      = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True)
    role         = models.CharField('Должность врача', max_length=30, choices=ROLES, default='----')
    
    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'
        ordering = ['-date_updated']
        
    def __str__(self) -> str:
        return self.user.username
    
    def get_full_name(self) -> str:
        return f"{self.last_name} {self.first_name} {self.father_name}"


class ReceptionNotes(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    med_organization = models.CharField('Медицинская организация', max_length=10, choices=MEDICAL_ORGANIZATION, blank=True)
    cabinet = models.CharField('Кабинет', max_length=10, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_meeting = models.DateTimeField('Время приема')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    def __str__(self) -> str:
        return  f'Доктор {self.doctor.first_name} {self.doctor.last_name}, '\
                f'пациент {self.patient.first_name} {self.patient.last_name}'
    
    class Meta:
        verbose_name = 'Запись приема'
        verbose_name_plural = 'Записи приема'
        ordering = ['-date_meeting', '-date_updated']


class ChangeControlLog(models.Model):
    who_changed = models.CharField("Кто изменил", max_length=100, default='')
    modified_model = models.CharField("Кого изменили", max_length=100, default='')
    change_type = models.CharField("Изменение", max_length=100)
    before = models.CharField('Было', max_length=500, default='')
    after = models.CharField('Стало', max_length=500, default='')
    date_created = models.DateTimeField('Дата создания', auto_now_add=True)
    
    def __str__(self) -> str:
        return self.who_changed
    
    class Meta:
        ordering = ['-date_created']
