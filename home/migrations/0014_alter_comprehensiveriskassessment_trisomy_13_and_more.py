# Generated by Django 4.1 on 2022-10-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_comprehensiveriskassessment_trisomy_13_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='trisomy_13',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='ПЭ поздний (до 37 недель)'),
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
            name='uterine_pulse_index',
            field=models.CharField(blank=True, choices=[('1', 'Правая'), ('2', 'Левая'), ('', '')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='ЗРП'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('2', 'Криоконсервированного'), ('1', 'Нативного'), ('', '')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Повторная'), ('1', 'Первая'), ('3', 'Наступила спонтанно'), ('4', 'Индуцирована с помощью ВРТ')], max_length=1, verbose_name='Беременность'),
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
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('obstetrician-gynecologist', 'акушер-гинеколог'), ('specialist', 'специалист'), ('dentist', 'стоматолог'), ('pediator', 'педиатор'), ('ophthalmologist', 'офтальмолог'), ('therapist', 'терапевт')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Павловский', 'Павловский район'), ('Николаевский', 'Николаевский район'), ('Карсунский', 'Карсунский район'), ('Барышский', 'Барышский район'), ('Тереньгульский', 'Тереньгульский район'), ('Ульяновский', 'Ульяновский район'), ('Цильнинский', 'Цильнинский район'), ('Старомайнский', 'Старомайнский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Инзенский', 'Инзенский район'), ('Радищевский', 'Радищевский район'), ('Сурский', 'Сурский район'), ('Чердаклинский', 'Чердаклинский район '), ('Новомалыклинский', 'Новомалыклинский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Базарносызганский', 'Базарносызганский район'), ('', '----'), ('Кузоватовский', 'Кузоватовский район'), ('Мелекесский', 'Мелекесский район'), ('Вешкаймский', 'Вешкаймский район'), ('Майнский', 'Майнский район'), ('Новоспасский', 'Новоспасский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='doctorexaminationsdentist',
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='doctorexaminationstherapist',
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('a', 'Алкоголь'), ('', '----'), ('s', 'Курение'), ('d', 'Наркотики')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('1', 'Плотная'), ('3', 'Мягкая'), ('2', 'Размягченная'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('2', 'Кпереди'), ('1', 'Кзади'), ('3', 'Расположена по центру'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Сомкнут'), ('1', 'Пропускает кончик пальца'), ('1', 'Пропускает палец')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('кос', 'Косое'), ('прод', 'Продольное'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Есть особенности'), ('1', 'Без особенностей')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('1', 'Патологических изменений нет'), ('4', 'Масталгия'), ('2', 'Пальпируется узловое образование'), ('', ''), ('3', 'Безболезненны ')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Есть особенности'), ('1', 'Без особенностей')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('1', 'По женскому типу'), ('', ''), ('3', 'Недостаточно выражена'), ('4', 'Нормально выражена'), ('5', 'Избыточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('гол', 'Головка'), ('тк', 'Тазовый конец')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Безболезненное'), ('1', 'Подвижное'), ('3', 'Болезненное')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='where',
            field=models.CharField(blank=True, choices=[('0', 'В отделение патологии беременности'), ('1', 'В отделение акушерского ухода'), ('', '')], max_length=1, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('4', 'AB(IV)'), ('1', 'O(I)'), ('2', 'A(II)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('2', 'Состоит в зарегистрированном браке'), ('5', 'Разведена'), ('', '----'), ('1', 'Никогда не состояла в браке'), ('3', 'Состоит в незарегистрированном браке'), ('4', 'Вдова'), ('6', 'Разошлась')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='med_org',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=150, null=True, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('4', 'AB(IV)'), ('1', 'O(I)'), ('2', 'A(II)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('18-20', 'Явка на 18-20 неделе'), ('1', 'Первая явка'), ('11-14', 'Явка на 11-14 неделе'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужской'), ('', '----'), ('f', 'Женский')], default='f', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1', 'Каждый день'), ('', '----'), ('1-2w', '1-2 раза в неделю'), ('1-2m', '1-2 раза в месяц')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hiv_status',
            field=models.CharField(blank=True, choices=[('1', 'Положительный'), ('0', 'Отрицательный')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='preeclampsia_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск преэклампсии'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='premature_birth_risk',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск преждевременных родов'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('3', 'Обильные'), ('1', 'Скудные'), ('2', 'Умеренные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('1>', 'Больше 1 пачки'), ('', '----'), ('1/2-1', 'От 1/2 до 1 пачки'), ('<1/2', 'Меньше 1/2 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
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
            field=models.CharField(blank=True, choices=[('a', 'Аборт'), ('d', 'Смерть'), ('b', 'Роды')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('кос', 'Косое'), ('прод', 'Продольное'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('гол', 'Головка'), ('тк', 'Тазовый конец')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='med_organization',
            field=models.CharField(blank=True, choices=[('', '----'), ('1', 'Болька 1'), ('2', 'Болька 2'), ('3', 'Болька 3')], max_length=10, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('obstetrician-gynecologist', 'акушер-гинеколог'), ('specialist', 'специалист'), ('dentist', 'стоматолог'), ('pediator', 'педиатор'), ('ophthalmologist', 'офтальмолог'), ('therapist', 'терапевт')], default='----', max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('0', 'Норма'), ('1', 'Маловодие'), ('2', 'Многоводие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('0', 'Норма'), ('1', 'Маловодие'), ('2', 'Многоводие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
    ]
