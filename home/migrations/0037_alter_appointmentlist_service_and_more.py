# Generated by Django 4.1.2 on 2022-12-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_alter_appointmentlist_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('2', 'Инструментальная диагностика'), ('1', 'Лабораторная диагностика'), ('3', 'Консультация'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_34',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ ранней (до 34 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_37',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ поздний (до 37 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='premature_birth',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Преждевременные роды'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_13',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='13 трисомии'),
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
            field=models.CharField(blank=True, choices=[('2', 'Левая'), ('1', 'Правая'), ('', '')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Задержка развития плода'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('2', 'Криоконсервированного'), ('1', 'Нативного'), ('', '')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('1', 'Первая'), ('', ''), ('3', 'Наступила спонтанно'), ('2', 'Повторная'), ('4', 'Индуцирована с помощью ВРТ')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('1', 'Первые'), ('', ''), ('2', 'Повторные')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('specialist', 'Специалист'), ('', ''), ('nurse', 'Медсестра'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('pediator', 'Педиатр'), ('receptionist', 'Регистратор'), ('assistant', 'Лаборант'), ('dentist', 'Стоматолог'), ('ophthalmologist', 'Офтальмолог'), ('therapist', 'Терапевт')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Чердаклинский', 'Чердаклинский район '), ('Барышский', 'Барышский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Павловский', 'Павловский район'), ('Кузоватовский', 'Кузоватовский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Сурский', 'Сурский район'), ('Николаевский', 'Николаевский район'), ('Базарносызганский', 'Базарносызганский район'), ('', ''), ('Вешкаймский', 'Вешкаймский район'), ('Цильнинский', 'Цильнинский район'), ('Радищевский', 'Радищевский район'), ('Новоспасский', 'Новоспасский район'), ('Старомайнский', 'Старомайнский район'), ('Мелекесский', 'Мелекесский район'), ('Тереньгульский', 'Тереньгульский район'), ('Майнский', 'Майнский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Карсунский', 'Карсунский район'), ('Инзенский', 'Инзенский район'), ('Ульяновский', 'Ульяновский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('', ''), ('a', 'Алкоголь'), ('d', 'Наркотики'), ('s', 'Курение')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('2', 'Размягченная'), ('3', 'Мягкая'), ('1', 'Плотная'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('1', 'Кзади'), ('3', 'Расположена по центру'), ('2', 'Кпереди'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Сомкнут'), ('2', 'Пропускает кончик пальца'), ('3', 'Пропускает палец'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('попер', 'Попереченое'), ('кос', 'Косое'), ('прод', 'Продольное'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('-', 'Не ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('4', 'Масталгия'), ('2', 'Пальпируется узловое образование'), ('3', 'Безболезненны '), ('', ''), ('1', 'Патологических изменений нет')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('5', 'Избыточно выражена'), ('2', 'По мужскому типу'), ('4', 'Нормально выражена'), ('3', 'Недостаточно выражена'), ('', ''), ('1', 'По женскому типу')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Подвижное'), ('3', 'Болезненное'), ('2', 'Безболезненное')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Начальное'), ('2', 'Среднее'), ('2', 'Высшее')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('', ''), ('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('', ''), ('+', '+'), ('-', '-')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('1', 'Никогда не состояла в браке'), ('3', 'Состоит в незарегистрированном браке'), ('6', 'Разошлась'), ('4', 'Вдова'), ('5', 'Разведена'), ('2', 'Состоит в зарегистрированном браке'), ('', '----')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('', ''), ('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('', ''), ('+', '+'), ('-', '-')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='modelivery',
            name='delivery',
            field=models.CharField(blank=True, choices=[('3', '3 уровень'), ('2', '2 уровень'), ('1', '1 уровень'), ('', '')], max_length=10, null=True, verbose_name='МО родоразрешения'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('11-14', 'Явка на 11-14 неделе'), ('30-40', 'Явка на 30-40 неделе'), ('1', 'Первая явка'), ('', ''), ('18-20', 'Явка на 18-20 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1-2m', '1-2 раза в месяц'), ('1-2w', '1-2 раза в неделю'), ('1', 'Каждый день'), ('', '')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
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
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск преэклампсии'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='premature_birth_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск преждевременных родов'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('2', 'Умеренные'), ('1', 'Скудные'), ('3', 'Обильные'), ('', '')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('', ''), ('1/2-1', 'От 1/2 до 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('1>', 'Больше 1 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('', ''), ('a', 'Искусственный'), ('s', 'Самопроизвольный')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('sc', 'Самопроизвольным - с осложнениями'), ('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений'), ('', '')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('', ''), ('d', 'Смерть'), ('a', 'Аборт'), ('b', 'Роды')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('попер', 'Попереченое'), ('кос', 'Косое'), ('прод', 'Продольное'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('-', 'Не ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('5', 'Неразвивающаяся беременность'), ('1', 'Срочные/Преждевременные'), ('', ''), ('3', 'Самопроизовльный выкидыш'), ('6', 'Пузырный занос'), ('4', 'Искусственный аборт'), ('2', 'Кесарево сечение')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('2', 'Индуцирована'), ('1', 'Самопроизовльно'), ('3', 'ВРТ'), ('', '')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(blank=True, choices=[('specialist', 'Специалист'), ('', ''), ('nurse', 'Медсестра'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('pediator', 'Педиатр'), ('receptionist', 'Регистратор'), ('assistant', 'Лаборант'), ('dentist', 'Стоматолог'), ('ophthalmologist', 'Офтальмолог'), ('therapist', 'Терапевт')], max_length=30, null=True, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='samd',
            name='sms_status',
            field=models.CharField(blank=True, choices=[('1', 'Недостаточно данных'), ('', ''), ('4', 'Готов к отправке'), ('5', 'Отправлен'), ('3', 'Не подписан'), ('2', 'Неправильно введены данные')], max_length=300, verbose_name='Статус версии СМС'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('0', 'Норма'), ('', ''), ('1', 'Маловодие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('0', 'Норма'), ('', ''), ('1', 'Маловодие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Тазовое'), ('0', 'Головное')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
    ]
