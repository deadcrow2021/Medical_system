from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .choices import *


class CustomUser(AbstractUser):
    first_name   = models.CharField("Имя", max_length=50)
    last_name    = models.CharField("Фамилия", max_length=50)
    father_name  = models.CharField("Отчество", max_length=50, blank=True)
    date_of_birth= models.DateField('Дата рождения', default='2000-01-12')
    gender       = models.CharField('Пол', max_length=1, choices=GENDERS, default='f')
    groups       = models.CharField('Группа', max_length=1, choices=GROUPS)
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
    
    # last_name.deconstruct
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name} {self.father_name}"