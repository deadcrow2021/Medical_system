# Generated by Django 4.1.1 on 2022-10-17 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_comprehensiveriskassessment_trisomy_13_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorExaminationsDentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата осмотра')),
                ('result', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Результаты осмотра, заключение')),
                ('med_org', models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация')),
                ('doctor_fio', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О. врача, проводившего осмотр')),
                ('doctor_confirmation', models.BooleanField(default=False, null=True, verbose_name='Подтверждение врача')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorExaminationsTherapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата осмотра')),
                ('result', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Результаты осмотра, заключение')),
                ('ecg_date', models.DateField(blank=True, null=True, verbose_name='Дата ЭКГ')),
                ('ecgresult', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Результаты ЭКГ')),
                ('med_org', models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация')),
                ('doctor_fio', models.CharField(blank=True, max_length=300, null=True, verbose_name='Ф.И.О. врача, проводившего осмотр')),
                ('doctor_confirmation', models.BooleanField(default=False, null=True, verbose_name='Подтверждение врача')),
            ],
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_13',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ поздний (до 37 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_18',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='18 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_21',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='21 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='uterine_pulse_index',
            field=models.CharField(blank=True, choices=[('1', 'Правая'), ('2', 'Левая'), ('', '')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='ЗРП'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('3', 'Наступила спонтанно'), ('2', 'Повторная'), ('1', 'Первая'), ('', ''), ('4', 'Индуцирована с помощью ВРТ')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Первые'), ('2', 'Повторные')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('specialist', 'специалист'), ('obstetrician-gynecologist', 'акушер-гинеколог'), ('pediator', 'педиатор'), ('therapist ', 'терапевт'), ('dentist', 'стоматолог'), ('ophthalmologist', 'офтальмолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Сурский', 'Сурский район'), ('Кузоватовский', 'Кузоватовский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Барышский', 'Барышский район'), ('Ульяновский', 'Ульяновский район'), ('Павловский', 'Павловский район'), ('Цильнинский', 'Цильнинский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Старомайнский', 'Старомайнский район'), ('Майнский', 'Майнский район'), ('Мелекесский', 'Мелекесский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Инзенский', 'Инзенский район'), ('Чердаклинский', 'Чердаклинский район '), ('Вешкаймский', 'Вешкаймский район'), ('Базарносызганский', 'Базарносызганский район'), ('', '----'), ('Новоспасский', 'Новоспасский район'), ('Карсунский', 'Карсунский район'), ('Радищевский', 'Радищевский район'), ('Тереньгульский', 'Тереньгульский район'), ('Николаевский', 'Николаевский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('s', 'Курение'), ('d', 'Наркотики'), ('', '----'), ('a', 'Алкоголь')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('1', 'Плотная'), ('2', 'Размягченная'), ('3', 'Мягкая'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Пропускает палец'), ('1', 'Сомкнут'), ('', ''), ('1', 'Пропускает кончик пальца')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('', ''), ('2', 'Есть особенности')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('4', 'Масталгия'), ('', ''), ('2', 'Пальпируется узловое образование'), ('1', 'Патологических изменений нет'), ('3', 'Безболезненны ')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='nipples',
            field=models.CharField(blank=True, choices=[('1', 'Сформированы правильно'), ('2', 'Втянуты'), ('', '')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('', ''), ('2', 'Есть особенности')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('1', 'По женскому типу'), ('4', 'Нормально выражена'), ('', ''), ('5', 'Избыточно выражена'), ('3', 'Недостаточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('тк', 'Тазовый конец'), ('гол', 'Головка')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('2', 'Безболезненное'), ('1', 'Подвижное'), ('3', 'Болезненное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистрированном браке'), ('4', 'Вдова'), ('', '----'), ('2', 'Состоит в зарегистрированном браке'), ('5', 'Разведена'), ('1', 'Никогда не состояла в браке'), ('6', 'Разошлась')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('18-20', 'Явка на 18-20 неделе'), ('1', 'Первая явка'), ('11-14', 'Явка на 11-14 неделе'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('', '----'), ('f', 'Женский'), ('m', 'Мужской')], default='f', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1-2m', '1-2 раза в месяц'), ('1', 'Каждый день'), ('', '----'), ('1-2w', '1-2 раза в неделю')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('0', 'Не состояла'), ('1', 'Состояла')], max_length=1, null=True, verbose_name='Диспансерский учет'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hiv_status',
            field=models.CharField(blank=True, choices=[('1', 'Положительный'), ('0', 'Отрицательный')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='preeclampsia_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Риск преэклампсии'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='premature_birth_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Риск преждевременных родов'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('1', 'Скудные'), ('2', 'Умеренные'), ('3', 'Обильные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('', '----'), ('1>', 'Больше 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('1/2-1', 'От 1/2 до 1 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('a', 'Искусственный'), ('s', 'Самопроизвольный')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('sc', 'Самопроизвольным - с осложнениями'), ('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('b', 'Роды'), ('a', 'Аборт'), ('d', 'Смерть')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('тк', 'Тазовый конец'), ('гол', 'Головка')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
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
            field=models.CharField(blank=True, choices=[('1', 'Тазовое'), ('0', 'Головное'), ('', '')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
        migrations.DeleteModel(
            name='DoctorExaminations',
        ),
        migrations.AddField(
            model_name='doctorexaminationstherapist',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_examination_therapist', to='home.patient'),
        ),
        migrations.AddField(
            model_name='doctorexaminationsdentist',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_examination_dentist', to='home.patient'),
        ),
    ]
