# Generated by Django 4.1.1 on 2022-10-05 17:31

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_patient_email_alter_doctor_role_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalcard',
            options={'verbose_name': 'Медицинская карта', 'verbose_name_plural': 'Медицинские карты'},
        ),
        migrations.RemoveField(
            model_name='medicalcard',
            name='age',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='blood',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='city_village',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_death',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='disability',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='insurance',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='med_org',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='oms_policy',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='snils',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='social_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='territory',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='work_address',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('стоматолог', 'стоматолог'), ('специалист', 'специалист'), ('офтальмолог', 'офтальмолог'), ('терапевт ', 'терапевт'), ('акушер-гинеколог', 'акушер-гинеколог'), ('педиатор', 'педиатор')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Радищевский', 'Радищевский район'), ('Вешкаймский', 'Вешкаймский район'), ('Мелекесский', 'Мелекесский район'), ('Барышский', 'Барышский район'), ('Майнский', 'Майнский район'), ('Базарносызганский', 'Базарносызганский район'), ('', '----'), ('Новомалыклинский', 'Новомалыклинский район'), ('Инзенский', 'Инзенский район'), ('Ульяновский', 'Ульяновский район'), ('Карсунский', 'Карсунский район'), ('Николаевский', 'Николаевский район'), ('Старомайнский', 'Старомайнский район'), ('Павловский', 'Павловский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Новоспасский', 'Новоспасский район'), ('Сурский', 'Сурский район'), ('Кузоватовский', 'Кузоватовский район'), ('Чердаклинский', 'Чердаклинский район '), ('Цильнинский', 'Цильнинский район'), ('Тереньгульский', 'Тереньгульский район'), ('Сенгилеевский', 'Сенгилеевский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='home_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Домашний телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистрированном браке'), ('6', 'Разошлась'), ('5', 'Разведена'), ('4', 'Вдова'), ('1', 'Никогда не состояла в браке'), ('', '----'), ('2', 'Состоит в зарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mobile_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='trusted_person_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Мобильный телефон'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='work_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region=None, verbose_name='Рабочий телефон'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский'), ('', '----')], default='f', max_length=1, verbose_name='Пол'),
        ),
    ]