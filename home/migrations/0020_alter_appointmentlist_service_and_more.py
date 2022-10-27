# Generated by Django 4.1 on 2022-10-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_remove_antibodiesdetermination_doctor_confirmation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('1', 'Лабораторная диагностика'), ('2', 'Инструментальная диагностика'), ('3', 'Консультация'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_34',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ ранней (до 34 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='preeclampcy_37',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ поздний (до 37 недель)'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='premature_birth',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Преждевременные роды'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_13',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='13 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_18',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='18 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_21',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='21 трисомии'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Задержка развития плода'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('2', 'Криоконсервированного'), ('1', 'Нативного'), ('', '')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('3', 'Наступила спонтанно'), ('1', 'Первая'), ('', ''), ('4', 'Индуцирована с помощью ВРТ'), ('2', 'Повторная')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Одноплодность'), ('2', 'Многоплодность')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('dentist', 'Стоматолог'), ('pediator', 'Педиатор'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('', ''), ('specialist', 'Специалист'), ('ophthalmologist', 'Офтальмолог'), ('therapist', 'Терапевт')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Барышский', 'Барышский район'), ('Вешкаймский', 'Вешкаймский район'), ('Чердаклинский', 'Чердаклинский район '), ('Базарносызганский', 'Базарносызганский район'), ('Павловский', 'Павловский район'), ('Ульяновский', 'Ульяновский район'), ('Инзенский', 'Инзенский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Новоспасский', 'Новоспасский район'), ('Николаевский', 'Николаевский район'), ('Сурский', 'Сурский район'), ('Майнский', 'Майнский район'), ('Цильнинский', 'Цильнинский район'), ('', ''), ('Радищевский', 'Радищевский район'), ('Кузоватовский', 'Кузоватовский район'), ('Старомайнский', 'Старомайнский район'), ('Тереньгульский', 'Тереньгульский район'), ('Мелекесский', 'Мелекесский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Карсунский', 'Карсунский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('d', 'Наркотики'), ('a', 'Алкоголь'), ('s', 'Курение'), ('', '')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('3', 'Мягкая'), ('1', 'Плотная'), ('', ''), ('2', 'Размягченная')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('3', 'Расположена по центру'), ('2', 'Кпереди'), ('1', 'Кзади'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Пропускает кончик пальца'), ('1', 'Пропускает палец'), ('1', 'Сомкнут'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('', ''), ('кос', 'Косое'), ('попер', 'Попереченое'), ('прод', 'Продольное')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Есть особенности'), ('1', 'Без особенностей')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Пальпируется узловое образование'), ('3', 'Безболезненны '), ('1', 'Патологических изменений нет'), ('4', 'Масталгия')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Есть особенности'), ('1', 'Без особенностей')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('1', 'По женскому типу'), ('4', 'Нормально выражена'), ('2', 'По мужскому типу'), ('3', 'Недостаточно выражена'), ('', ''), ('5', 'Избыточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('2', 'Безболезненное'), ('3', 'Болезненное'), ('', ''), ('1', 'Подвижное')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability',
            field=models.CharField(blank=True, choices=[('1', 'Группа 1'), ('2', 'Группа 2'), ('3', 'Группа 3'), ('', '')], max_length=200, null=True, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'A(II)'), ('3', 'B(III)'), ('1', 'O(I)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('', ''), ('+', '+'), ('-', '-')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('6', 'Разошлась'), ('5', 'Разведена'), ('3', 'Состоит в незарегистрированном браке'), ('2', 'Состоит в зарегистрированном браке'), ('', '----'), ('1', 'Никогда не состояла в браке'), ('4', 'Вдова')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'A(II)'), ('3', 'B(III)'), ('1', 'O(I)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('', ''), ('+', '+'), ('-', '-')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('11-14', 'Явка на 11-14 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('', ''), ('30-40', 'Явка на 30-40 неделе'), ('1', 'Первая явка')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1', 'Каждый день'), ('1-2w', '1-2 раза в неделю'), ('1-2m', '1-2 раза в месяц'), ('', '')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('0', 'Не состояла'), ('1', 'Состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hiv_status',
            field=models.CharField(blank=True, choices=[('1', 'Положительный'), ('0', 'Отрицательный'), ('', '')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='preeclampsia_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Риск преэклампсии'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='premature_birth_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Риск преждевременных родов'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('', ''), ('3', 'Обильные'), ('1', 'Скудные'), ('2', 'Умеренные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('a', 'Искусственный'), ('s', 'Самопроизвольный'), ('', '')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('', ''), ('a', 'Аборт'), ('b', 'Роды'), ('d', 'Смерть')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('', ''), ('кос', 'Косое'), ('попер', 'Попереченое'), ('прод', 'Продольное')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('3', 'Самопроизовльный выкидыш'), ('6', 'Пузырный занос'), ('5', 'Неразвивающаяся беременность'), ('4', 'Искисственный аборт'), ('', ''), ('2', 'Кесарево сечение'), ('1', 'Срочные/Преждевременные')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('1', 'Самопроизовльно'), ('2', 'Индуцироваа'), ('3', 'ВРТ'), ('', '')], max_length=10, null=True, verbose_name='Насупила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('dentist', 'Стоматолог'), ('pediator', 'Педиатор'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('', ''), ('specialist', 'Специалист'), ('ophthalmologist', 'Офтальмолог'), ('therapist', 'Терапевт')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('1', 'Маловодие'), ('0', 'Норма'), ('2', 'Многоводие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('1', 'Маловодие'), ('0', 'Норма'), ('2', 'Многоводие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
    ]
