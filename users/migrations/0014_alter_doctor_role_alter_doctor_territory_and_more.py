# Generated by Django 4.0.2 on 2022-10-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_medicalcard_births_by_term_alter_doctor_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('специалист', 'специалист'), ('педиатор', 'педиатор'), ('офтальмолог', 'офтальмолог'), ('акушер-гинеколог', 'акушер-гинеколог'), ('терапевт ', 'терапевт'), ('стоматолог', 'стоматолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Кузоватовский', 'Кузоватовский район'), ('Новоспасский', 'Новоспасский район'), ('Цильнинский', 'Цильнинский район'), ('Мелекесский', 'Мелекесский район'), ('Базарносызганский', 'Базарносызганский район'), ('Николаевский', 'Николаевский район'), ('Радищевский', 'Радищевский район'), ('Карсунский', 'Карсунский район'), ('Инзенский', 'Инзенский район'), ('Ульяновский', 'Ульяновский район'), ('Майнский', 'Майнский район'), ('Барышский', 'Барышский район'), ('Тереньгульский', 'Тереньгульский район'), ('Сурский', 'Сурский район'), ('Старомайнский', 'Старомайнский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Чердаклинский', 'Чердаклинский район '), ('Старокулаткинский', 'Старокулаткинский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Павловский', 'Павловский район'), ('Вешкаймский', 'Вешкаймский район'), ('', '----')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('2', 'A(II)'), ('4', 'AB(IV)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистрированном браке'), ('5', 'Разведена'), ('', '----'), ('2', 'Состоит в зарегистрированном браке'), ('6', 'Разошлась'), ('1', 'Никогда не состояла в браке'), ('4', 'Вдова')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('2', 'A(II)'), ('4', 'AB(IV)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('11-14', 'Явка на 11-14 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('1', 'Первая явка'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('f', 'Женский'), ('', '----')], default='f', max_length=1, verbose_name='Пол'),
        ),
    ]
