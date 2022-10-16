# Generated by Django 4.0.2 on 2022-10-16 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_doctor_role_alter_doctor_territory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelviometry',
            options={},
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('3', 'Наступила спонтанно'), ('1', 'Первая'), ('4', 'Индуцирована с помощью ВРТ'), ('', ''), ('2', 'Повторная')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('2', 'Многоплодность'), ('1', 'Одноплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('1', 'Первые'), ('2', 'Повторные'), ('', '')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('акушер-гинеколог', 'акушер-гинеколог'), ('специалист', 'специалист'), ('терапевт ', 'терапевт'), ('педиатор', 'педиатор'), ('стоматолог', 'стоматолог'), ('офтальмолог', 'офтальмолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Чердаклинский', 'Чердаклинский район '), ('Радищевский', 'Радищевский район'), ('Барышский', 'Барышский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Ульяновский', 'Ульяновский район'), ('Майнский', 'Майнский район'), ('Павловский', 'Павловский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Кузоватовский', 'Кузоватовский район'), ('Цильнинский', 'Цильнинский район'), ('Базарносызганский', 'Базарносызганский район'), ('Сурский', 'Сурский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Старомайнский', 'Старомайнский район'), ('Новоспасский', 'Новоспасский район'), ('Мелекесский', 'Мелекесский район'), ('Карсунский', 'Карсунский район'), ('Николаевский', 'Николаевский район'), ('', '----'), ('Инзенский', 'Инзенский район'), ('Вешкаймский', 'Вешкаймский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('s', 'Курение'), ('', '----'), ('a', 'Алкоголь'), ('d', 'Наркотики')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('3', 'Мягкая'), ('1', 'Плотная'), ('2', 'Размягченная'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('', ''), ('3', 'Расположена по центру'), ('2', 'Кпереди'), ('1', 'Кзади')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Сомкнут'), ('1', 'Пропускает палец'), ('1', 'Пропускает кончик пальца'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('3', 'Безболезненны '), ('2', 'Пальпируется узловое образование'), ('4', 'Масталгия'), ('', ''), ('1', 'Патологических изменений нет')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='nipples',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Втянуты'), ('1', 'Сформированы правильно')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('1', 'По женскому типу'), ('4', 'Нормально выражена'), ('', ''), ('3', 'Недостаточно выражена'), ('5', 'Избыточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('1', 'Подвижное'), ('2', 'Безболезненное'), ('3', 'Болезненное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('2', 'A(II)'), ('4', 'AB(IV)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('1', 'Никогда не состояла в браке'), ('4', 'Вдова'), ('6', 'Разошлась'), ('', '----'), ('5', 'Разведена'), ('2', 'Состоит в зарегистрированном браке'), ('3', 'Состоит в незарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('2', 'A(II)'), ('4', 'AB(IV)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('30-40', 'Явка на 30-40 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('11-14', 'Явка на 11-14 неделе'), ('1', 'Первая явка')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('', '----'), ('m', 'Мужской'), ('f', 'Женский')], default='f', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('', '----'), ('1-2w', '1-2 раза в неделю'), ('1', 'Каждый день'), ('1-2m', '1-2 раза в месяц')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('1', 'Регулярные'), ('0', 'Нерегулярные')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('', '----'), ('1/2-1', 'От 1/2 до 1 пачки'), ('1>', 'Больше 1 пачки'), ('<1/2', 'Меньше 1/2 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('sc', 'Самопроизвольным - с осложнениями'), ('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Маловодие'), ('0', 'Норма'), ('2', 'Многоводие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Маловодие'), ('0', 'Норма'), ('2', 'Многоводие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('0', 'Головное'), ('1', 'Тазовое'), ('', '')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
        migrations.CreateModel(
            name='HospitalizationInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(blank=True, null=True, verbose_name='Дата начала')),
                ('date_finish', models.DateField(blank=True, null=True, verbose_name='Дата окончания')),
                ('hosp_type', models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид')),
                ('med_org', models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация')),
                ('diagnosis', models.CharField(blank=True, max_length=200, null=True, verbose_name='Основной диагноз')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата')),
                ('doctor_confirmation_1', models.BooleanField(default=False, null=True, verbose_name='Подтверждение врача')),
                ('prenatal_hospitalization', models.BooleanField(default=False, null=True, verbose_name='Дородовая госпитализация')),
                ('where', models.CharField(blank=True, choices=[('1', 'В отделение акушерского ухода'), ('0', 'В отделение патологии беременности'), ('', '')], max_length=1, verbose_name='Медицинская организация')),
                ('foundation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Основание')),
                ('date_filling', models.DateField(blank=True, null=True, verbose_name='Дата заполнения')),
                ('doctor_confirmation_2', models.BooleanField(default=False, null=True, verbose_name='Подтверждение врача')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospitalization', to='home.patient')),
            ],
        ),
    ]
