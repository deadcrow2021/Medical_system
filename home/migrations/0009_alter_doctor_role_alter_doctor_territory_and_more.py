# Generated by Django 4.0.2 on 2022-10-04 18:48

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_doctor_role_alter_doctor_territory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('стоматолог', 'стоматолог'), ('акушер-гинеколог', 'акушер-гинеколог'), ('педиатор', 'педиатор'), ('терапевт ', 'терапевт'), ('специалист', 'специалист'), ('офтальмолог', 'офтальмолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Базарносызганский', 'Базарносызганский район'), ('Ульяновский', 'Ульяновский район'), ('Инзенский', 'Инзенский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Майнский', 'Майнский район'), ('Кузоватовский', 'Кузоватовский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Сурский', 'Сурский район'), ('Вешкаймский', 'Вешкаймский район'), ('Николаевский', 'Николаевский район'), ('Карсунский', 'Карсунский район'), ('Павловский', 'Павловский район'), ('Новоспасский', 'Новоспасский район'), ('Мелекесский', 'Мелекесский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Чердаклинский', 'Чердаклинский район '), ('', '----'), ('Радищевский', 'Радищевский район'), ('Барышский', 'Барышский район'), ('Цильнинский', 'Цильнинский район'), ('Новомалыклинский', 'Новомалыклинский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='allergy',
            field=models.BooleanField(default=False, null=True, verbose_name='Аллергическая реакция'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='allergy_description',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Описание аллергической реакции'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='childbirth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата родов'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='complications',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Осложнения данной беременности'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='date_of_birth',
            field=models.DateField(blank=True, default='2000-01-12', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='diagnosis',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Основной диагноз'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability_certificate',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Номер отпуска по беременности и родам'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='doctor_confirmation',
            field=models.BooleanField(default=False, null=True, verbose_name='Подтверждение врача'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='first_visit_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата первой явки (взятие на учет)'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='generic_certificate_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи родового сертификата'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='generic_certificate_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер родового сертификата'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='gynecological_diseases',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Осложнения данной беременности'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, null=True, region=None, verbose_name='Домашний телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистриро-ванном браке'), ('1', 'Никогда не состояла в браке'), ('', '----'), ('2', 'Состоит в зарегистри-рованном браке'), ('5', 'Разведена'), ('4', 'Вдова'), ('6', 'Разошлась')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='maternity_leave_finish',
            field=models.DateField(blank=True, null=True, verbose_name='Окончание декретного отпуска'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='maternity_leave_start',
            field=models.DateField(blank=True, null=True, verbose_name='Начало декретного отпуска'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, null=True, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, null=True, region=None, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='oms_policy',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Полис ОМС'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='registration_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес регистрции'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='residence_address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='snils',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='СНИЛС'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='somatic_diseases',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Осложнения данной беременности'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='trusted_person_fio',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='ФИО доверенного лица'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='trusted_person_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, null=True, region=None, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='work_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=10, null=True, region=None, verbose_name='Рабочий телефон'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood',
            field=models.CharField(blank=True, choices=[('2+', 'A(II) Rh+ '), ('1+', 'O(I) Rh+ '), ('4-', 'AB(IV) Rh-'), ('4+', 'AB(IV) Rh+'), ('3-', 'B(III) Rh- '), ('1-', 'O(I) Rh- '), ('2-', 'A(II) Rh- '), ('3+', 'B(III) Rh+ ')], max_length=2, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='disability',
            field=models.CharField(blank=True, choices=[('2', 'Вторая'), ('1', 'Первая'), ('3', 'Третья')], max_length=1, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance',
            field=models.CharField(blank=True, choices=[('5', 'ООО «Страховая компания «Ингосстрах-М»'), ('2', 'ООО «МСК «МЕДСТРАХ»»'), ('4', 'АО «Страховая компания «СОГАЗ-Мед»»'), ('3', 'ООО «Страховая медицинская компания РЕСО-МЕД» (Московский филиал)'), ('1', 'АО «Медицинская акционерная страховая компания» (АО «МАКС-М»)'), ('6', 'ООО «КАПИТАЛ МС» ')], max_length=1, verbose_name='Сраховая компания'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='territory',
            field=models.CharField(choices=[('Базарносызганский', 'Базарносызганский район'), ('Ульяновский', 'Ульяновский район'), ('Инзенский', 'Инзенский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Майнский', 'Майнский район'), ('Кузоватовский', 'Кузоватовский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Сурский', 'Сурский район'), ('Вешкаймский', 'Вешкаймский район'), ('Николаевский', 'Николаевский район'), ('Карсунский', 'Карсунский район'), ('Павловский', 'Павловский район'), ('Новоспасский', 'Новоспасский район'), ('Мелекесский', 'Мелекесский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Чердаклинский', 'Чердаклинский район '), ('', '----'), ('Радищевский', 'Радищевский район'), ('Барышский', 'Барышский район'), ('Цильнинский', 'Цильнинский район'), ('Новомалыклинский', 'Новомалыклинский район')], max_length=25, verbose_name='Территория'),
        ),
    ]
