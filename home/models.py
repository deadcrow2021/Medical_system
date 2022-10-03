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
    date_of_birth= models.DateField('Дата рождения', default='2000-01-12')
    gender       = models.CharField('Пол', max_length=1, choices=GENDERS, default='f')
    social_status= models.CharField('Соц. Статус', max_length=1, choices=SOCIAL_STATUS, blank=True)
    disability   = models.CharField('Инвалидность', max_length=1, choices=DISABILITY, blank=True)
    blood        = models.CharField('Группа крови', max_length=2, choices=BLOOD, blank=True)
    telephone    = PhoneNumberField('Телефонный номер', null=False, blank=True)
    work_address = models.CharField('Адресс работы', max_length=150, blank=True)
    oms_policy   = models.CharField('Полис ОМС', max_length=16, blank=True)
    insurance    = models.CharField('Сраховая компания', max_length=1, choices=INSURANCE, blank=True)
    snils        = models.CharField('СНИЛС', max_length=11, blank=True)
    city_village = models.CharField('Житель города/села', max_length=1, choices=CITYVILLAGE)
    address      = models.CharField('Адресс', max_length=150, blank=True)
    territory    = models.CharField('Территория', max_length=25, choices=TERRITORY)
    date_updated = models.DateTimeField('Дата изменения', auto_now=True)
    date_death   = models.DateTimeField('Дата смерти', blank=True, null=True)
    med_org      = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True)
    
    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['-date_updated']
    
    def __str__(self) -> str:
        return self.user.username
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name} {self.father_name}"


class MedicalCard(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='card')
    first_name   = models.CharField("Имя", max_length=100)
    last_name    = models.CharField("Фамилия", max_length=100)
    father_name  = models.CharField("Отчество", max_length=100, blank=True)
    date_of_birth= models.DateField('Дата рождения', default='2000-01-12')
    age = models.PositiveSmallIntegerField('Полных лет', validators=[MaxValueValidator(99)])
    residence_address = models.CharField('Адрес проживания', max_length=100)
    registration_address = models.CharField('Адрес регистрции', max_length=100)
    mobile_phone    = PhoneNumberField('Мобильный телефон', max_length=10)
    home_phone    = PhoneNumberField('Домашний телефон', max_length=10, blank=True)
    work_phone    = PhoneNumberField('Рабочий телефон', max_length=10, blank=True)
    email = models.EmailField('Адрес электронной почты', max_length=100)
    marital_status = models.CharField('Брачное состояние', default='', choices=MARITAL_STATUS, max_length=1)
    trusted_person_fio = models.CharField("ФИО доверенного лица", max_length=300)
    trusted_person_phone = PhoneNumberField('Мобильный телефон', max_length=10)
    oms_policy   = models.CharField('Полис ОМС', max_length=16)
    snils        = models.CharField('СНИЛС', max_length=11)
    maternity_leave_start = models.DateField('Начало декретного отпуска', blank=True)
    maternity_leave_finish = models.DateField('Окончание декретного отпуска', blank=True)
    disability_certificate = models.CharField('Номер отпуска по беременности и родам', max_length=16, blank=True)
    generic_certificate_number = models.CharField('Номер родового сертификата', max_length=20, blank=True)
    generic_certificate_date = models.DateField('Дата выдачи родового сертификата', blank=True)
    allergy = models.BooleanField('Аллергическая реакция', default=False)
    allergy_description = models.CharField('Описание аллергической реакции', default='', max_length=100)
    # blood        = models.CharField('Группа крови', max_length=2, choices=BLOOD)
    pregnancy_count = models.PositiveSmallIntegerField('Беременность по счету', blank=True, validators=[MaxValueValidator(99)])
    gestation_period_weeks = models.PositiveSmallIntegerField('Срок беременности (недели)', validators=[MaxValueValidator(99)])
    first_visit_date = models.DateField('Дата первой явки (взятие на учет)')
    childbirth_date = models.DateField('Дата родов', blank=True)
    childbirth_gestation_period = models.PositiveSmallIntegerField('Срок беременности родов (недели)', validators=[MaxValueValidator(99)])
    med_org      = models.CharField('Медицинская организация', max_length=150, choices=MEDICAL_ORGANIZATION, blank=True)
    # obstetric_risk_screening =
    # obstetric_risk_recomendations = 
    diagnosis = models.CharField('Основной диагноз', max_length=200, blank=True)
    complications = models.CharField('Осложнения данной беременности', max_length=200, blank=True)
    somatic_diseases = models.CharField('Осложнения данной беременности', max_length=200, blank=True)
    gynecological_diseases = models.CharField('Осложнения данной беременности', max_length=200, blank=True)
    doctor_confirmation = models.BooleanField('Подтверждение врача', default=False)


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
