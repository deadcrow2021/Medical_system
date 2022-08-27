from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    GENDERS = {
        ('m', 'Мужчина'),
        ('f', 'Женщина'),
    }

    fio = models.CharField('FIO', max_length=150, default='')
    gender = models.CharField('Gender', max_length=1, choices=GENDERS, default='')
    date_of_birth = models.DateField('Date of birth', default='2000-01-12')


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#     fio = models.CharField('FIO', max_length=150)
#     date_of_birth = models.DateField('Date of birth')
#     age = models.PositiveIntegerField('Age', validators=[MinValueValidator(1), MaxValueValidator(120)])
#     gestation_period = models.PositiveIntegerField('Gestation period', validators=[MinValueValidator(1), MaxValueValidator(50)])
#     trimester = models.PositiveIntegerField('Trimester', validators=[MinValueValidator(1), MaxValueValidator(3)]) # надо добавить определитель триместра по сроку беременности
#     # risk_grade = Не понятно как определять 
#     def __str__(self):
#         return self.fio
    
#     class Meta:
#         verbose_name = "Пользователь"
#         verbose_name_plural = "Пользователи"