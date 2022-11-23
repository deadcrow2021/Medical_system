# Generated by Django 4.1.2 on 2022-11-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_alter_appointmentlist_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('3', 'Консультация'), ('2', 'Инструментальная диагностика'), ('1', 'Лабораторная диагностика'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_34',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='ПЭ ранней (до 34 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_37',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='ПЭ поздний (до 37 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='premature_birth',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Преждевременные роды'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_13',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='13 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_18',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='18 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_21',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='21 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='uterine_pulse_index',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Левая'), ('1', 'Правая')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Задержка развития плода'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('2', 'Криоконсервированного'), ('1', 'Нативного'), ('', '')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('1', 'Первая'), ('', ''), ('4', 'Индуцирована с помощью ВРТ'), ('2', 'Повторная'), ('3', 'Наступила спонтанно')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Повторные'), ('1', 'Первые')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='cabinet',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Кабинет'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=60, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('pediator', 'Педиатор'), ('receptionist', 'Регистратор'), ('', ''), ('assistant', 'Лаборант'), ('specialist', 'Специалист'), ('dentist', 'Стоматолог'), ('therapist', 'Терапевт'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('nurse', 'Медсестра'), ('ophthalmologist', 'Офтальмолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Радищевский', 'Радищевский район'), ('Карсунский', 'Карсунский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Павловский', 'Павловский район'), ('Вешкаймский', 'Вешкаймский район'), ('Майнский', 'Майнский район'), ('Кузоватовский', 'Кузоватовский район'), ('Чердаклинский', 'Чердаклинский район '), ('Мелекесский', 'Мелекесский район'), ('Цильнинский', 'Цильнинский район'), ('Николаевский', 'Николаевский район'), ('Сурский', 'Сурский район'), ('Новоспасский', 'Новоспасский район'), ('', ''), ('Ульяновский', 'Ульяновский район'), ('Базарносызганский', 'Базарносызганский район'), ('Барышский', 'Барышский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Инзенский', 'Инзенский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('a', 'Алкоголь'), ('s', 'Курение'), ('d', 'Наркотики'), ('', '')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('приж', 'Прижата'), ('под', 'Подвижна'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('2', 'Размягченная'), ('3', 'Мягкая'), ('1', 'Плотная'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('3', 'Расположена по центру'), ('2', 'Кпереди'), ('', ''), ('1', 'Кзади')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Сомкнут'), ('3', 'Пропускает палец'), ('2', 'Пропускает кончик пальца'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('', ''), ('-', 'Не ощущается')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('2', 'Пальпируется узловое образование'), ('3', 'Безболезненны '), ('', ''), ('1', 'Патологических изменений нет'), ('4', 'Масталгия')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('5', 'Избыточно выражена'), ('', ''), ('3', 'Недостаточно выражена'), ('4', 'Нормально выражена'), ('1', 'По женскому типу')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('2', 'Безболезненное'), ('1', 'Подвижное'), ('3', 'Болезненное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Высшее'), ('1', 'Начальное'), ('2', 'Среднее')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('1', 'Никогда не состояла в браке'), ('3', 'Состоит в незарегистрированном браке'), ('5', 'Разведена'), ('6', 'Разошлась'), ('2', 'Состоит в зарегистрированном браке'), ('', '----'), ('4', 'Вдова')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='modelivery',
            name='delivery',
            field=models.CharField(blank=True, choices=[('3', '3 уровень'), ('1', '1 уровень'), ('2', '2 уровень'), ('', '')], max_length=10, null=True, verbose_name='МО родоразрешения'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('30-40', 'Явка на 30-40 неделе'), ('1', 'Первая явка'), ('11-14', 'Явка на 11-14 неделе'), ('', ''), ('18-20', 'Явка на 18-20 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Каждый день'), ('1-2w', '1-2 раза в неделю'), ('1-2m', '1-2 раза в месяц')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('0', 'Не состояла'), ('1', 'Состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hiv_status',
            field=models.CharField(blank=True, choices=[('0', 'Отрицательный'), ('1', 'Положительный'), ('', '')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='painfulness',
            field=models.CharField(blank=True, choices=[('0', 'Безболезненные'), ('1', 'Болезненные'), ('', '')], max_length=10, null=True, verbose_name='Болезненность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='preeclampsia_risk',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск преэклампсии'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='premature_birth_risk',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск преждевременных родов'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('1', 'Скудные'), ('3', 'Обильные'), ('2', 'Умеренные'), ('', '')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('1', 'Регулярные'), ('0', 'Нерегулярные'), ('', '')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('<1/2', 'Меньше 1/2 пачки'), ('1>', 'Больше 1 пачки'), ('1/2-1', 'От 1/2 до 1 пачки'), ('', '')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('a', 'Искусственный'), ('s', 'Самопроизвольный'), ('', '')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('', ''), ('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений'), ('sc', 'Самопроизвольным - с осложнениями')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('d', 'Смерть'), ('a', 'Аборт'), ('b', 'Роды'), ('', '')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('приж', 'Прижата'), ('под', 'Подвижна'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('', ''), ('-', 'Не ощущается')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('4', 'Искусственный аборт'), ('3', 'Самопроизовльный выкидыш'), ('', ''), ('2', 'Кесарево сечение'), ('6', 'Пузырный занос'), ('1', 'Срочные/Преждевременные'), ('5', 'Неразвивающаяся беременность')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('1', 'Самопроизовльно'), ('3', 'ВРТ'), ('2', 'Индуцирована'), ('', '')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('pediator', 'Педиатор'), ('receptionist', 'Регистратор'), ('', ''), ('assistant', 'Лаборант'), ('specialist', 'Специалист'), ('dentist', 'Стоматолог'), ('therapist', 'Терапевт'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('nurse', 'Медсестра'), ('ophthalmologist', 'Офтальмолог')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('1', 'Маловодие'), ('2', 'Многоводие'), ('0', 'Норма'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('1', 'Маловодие'), ('2', 'Многоводие'), ('0', 'Норма'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('1', 'Тазовое'), ('0', 'Головное'), ('', '')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
    ]