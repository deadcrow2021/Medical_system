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
    telephone    = PhoneNumberField('Телефонный номер', null=False, blank=True)
    email        = models.EmailField(max_length=60, blank=True, null=True)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-date_updated']
    
    def __str__(self) -> str:
        return self.user.username
    
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

class Pelviometry(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pelviometry')
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
    
    class Meta:
        verbose_name = 'Пельвиометрия'


class PregnantWomanMonitoring(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='pregnant_woman_monitoring')
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    visit_number = models.PositiveSmallIntegerField('Номер посещения', validators=[MaxValueValidator(100)], blank=True, null=True)
    date = models.DateField('Дата', blank=True, null=True)
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)], blank=True, null=True)
    analysis = models.CharField('Анализ', max_length=1000, blank=True, null=True)
    appointment = models.CharField('Назначения', max_length=1000, blank=True, null=True)
    disability_certificate = models.CharField('Листок нетрудоспособности', max_length=1000, blank=True, null=True)
    next_visit_date = models.DateField('Дата', blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class TakingMedications(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medications')
    date_start = models.DateField('Дата начала приема препарата', blank=True, null=True)
    date_finish = models.DateField('Дата окончания приема препарата', blank=True, null=True)
    indications = models.CharField('Показания', max_length=1000, blank=True, null=True)
    dose_duration = models.CharField('Доза/Длительность', max_length=1000, blank=True, null=True)
    side_effects = models.CharField('Побочные эффекты', max_length=1000, blank=True, null=True)


class AntibodiesDetermination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='antibodies')
    date = models.DateField('Дата', blank=True, null=True)
    treponema_antibodies = models.CharField('Антитела к бледной трепонеме', max_length=1000, blank=True, null=True)
    hiv_antibodies = models.CharField('Антитела классов M, G к ВИЧ ½ и антиген р24', max_length=1000, blank=True, null=True)
    hbsag_antibodies = models.CharField('HBsAg или антитела к HBsAg', max_length=1000, blank=True, null=True)
    anti_hcv = models.CharField('anti-HCV IgG и anti-HCV IgM', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class RubellaVirus(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='rubella')
    date = models.DateField('Дата', blank=True, null=True)
    lgm = models.CharField('lgM', max_length=1000, blank=True, null=True)
    lgg = models.CharField('lgG', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class AntiresusBodies(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='antiresus_bodies')
    date = models.DateField('Дата', blank=True, null=True)
    antiresus_bodies = models.CharField('Антирезусные тела', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От обследования отсказалась', default=False, null=True)


class BloodAnalysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='blood_analysis')
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='biochemical_blood')
    date = models.DateField('Дата', blank=True, null=True)
    total_bilirubin = models.CharField('Общий билирубин, мкмоль/л', max_length=1000, blank=True, null=True)
    direct_bilirubin = models.CharField('Прямой билирубин, мкмоль/л', max_length=1000, blank=True, null=True)
    total_protein = models.CharField('Общий белок, г/л', max_length=1000, blank=True, null=True)
    alt = models.CharField('АЛТ, ЕД/л', max_length=1000, blank=True, null=True)
    ast = models.CharField('АСТ, ЕД/л', max_length=1000, blank=True, null=True)
    glucose = models.CharField('Глюкоза, ммоль/л', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class Coagulogram(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='сoagulogram')
    date = models.DateField('Дата', blank=True, null=True)
    platelet_count = models.CharField('Количество тромбоцитов, 10^9/л', max_length=1000, blank=True, null=True)
    astv = models.CharField('АЧТВ, сек.', max_length=1000, blank=True, null=True)
    fibrinogen = models.CharField('Фибриноген, г/л', max_length=1000, blank=True, null=True)
    prothrombin_time = models.CharField('Протромбиновое время, %', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class GlucoseToleranceTest(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='glucose_test')
    date = models.DateField('Дата', blank=True, null=True)
    period = models.CharField('Срок (недель)', max_length=1000, blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class ThyroidStimulatingHormone(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='ts_hormonr')
    date = models.DateField('Дата', blank=True, null=True)
    period = models.CharField('Срок (недель)', max_length=1000, blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class Smears(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='smears')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)
    # examination_refise = models.BooleanField('От результатов отсказалась', default=False, null=True)


class BacterioscopicSmearsExamination(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='bacterio_smears')
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='cervix_exam')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


class UrineAnalysis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='urine')
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
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='urine_sowing')
    date = models.DateField('Дата', blank=True, null=True)
    result = models.CharField('Результат', max_length=1000, blank=True, null=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False, null=True)


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
