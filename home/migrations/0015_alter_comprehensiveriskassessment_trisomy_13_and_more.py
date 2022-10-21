# Generated by Django 4.1 on 2022-10-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_comprehensiveriskassessment_trisomy_13_and_more'),
    ]

    operations = [
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
            name='zrp',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='ЗРП'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('2', 'Повторная'), ('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно'), ('', ''), ('1', 'Первая')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('specialist', 'специалист'), ('therapist', 'терапевт'), ('dentist', 'стоматолог'), ('obstetrician-gynecologist', 'акушер-гинеколог'), ('pediator', 'педиатор'), ('ophthalmologist', 'офтальмолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Тереньгульский', 'Тереньгульский район'), ('', '----'), ('Чердаклинский', 'Чердаклинский район '), ('Радищевский', 'Радищевский район'), ('Вешкаймский', 'Вешкаймский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Базарносызганский', 'Базарносызганский район'), ('Николаевский', 'Николаевский район'), ('Цильнинский', 'Цильнинский район'), ('Новоспасский', 'Новоспасский район'), ('Карсунский', 'Карсунский район'), ('Майнский', 'Майнский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Барышский', 'Барышский район'), ('Павловский', 'Павловский район'), ('Мелекесский', 'Мелекесский район'), ('Ульяновский', 'Ульяновский район'), ('Кузоватовский', 'Кузоватовский район'), ('Сурский', 'Сурский район'), ('Инзенский', 'Инзенский район'), ('Старомайнский', 'Старомайнский район'), ('Новомалыклинский', 'Новомалыклинский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('a', 'Алкоголь'), ('', '----'), ('d', 'Наркотики'), ('s', 'Курение')], max_length=10, null=True, verbose_name='Вредные привычки'),
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
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('2', 'Есть особенности'), ('1', 'Без особенностей'), ('', '')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('', ''), ('3', 'Безболезненны '), ('2', 'Пальпируется узловое образование'), ('4', 'Масталгия'), ('1', 'Патологических изменений нет')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('2', 'Есть особенности'), ('1', 'Без особенностей'), ('', '')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('4', 'Нормально выражена'), ('', ''), ('5', 'Избыточно выражена'), ('1', 'По женскому типу'), ('3', 'Недостаточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('тк', 'Тазовый конец'), ('гол', 'Головка')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('2', 'Безболезненное'), ('3', 'Болезненное'), ('1', 'Подвижное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('0', 'Плановая'), ('1', 'Экстренная'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('3', 'B(III)'), ('2', 'A(II)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистрированном браке'), ('', '----'), ('5', 'Разведена'), ('6', 'Разошлась'), ('2', 'Состоит в зарегистрированном браке'), ('4', 'Вдова'), ('1', 'Никогда не состояла в браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('3', 'B(III)'), ('2', 'A(II)'), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('11-14', 'Явка на 11-14 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('1', 'Первая явка'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1-2m', '1-2 раза в месяц'), ('', '----'), ('1', 'Каждый день'), ('1-2w', '1-2 раза в неделю')], max_length=10, null=True, verbose_name='Алкоголь'),
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
            field=models.CharField(blank=True, choices=[('0', 'Отрицательный'), ('1', 'Положительный')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='painfulness',
            field=models.CharField(blank=True, choices=[('0', 'Безболезненные'), ('1', 'Болезненные')], max_length=10, null=True, verbose_name='Болезненность'),
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
            field=models.CharField(blank=True, choices=[('2', 'Умеренные'), ('3', 'Обильные'), ('1', 'Скудные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('0', 'Нерегулярные'), ('1', 'Регулярные')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('<1/2', 'Меньше 1/2 пачки'), ('', '----'), ('1>', 'Больше 1 пачки'), ('1/2-1', 'От 1/2 до 1 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений'), ('sc', 'Самопроизвольным - с осложнениями')], max_length=10, null=True, verbose_name='Роды'),
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
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('specialist', 'специалист'), ('therapist', 'терапевт'), ('dentist', 'стоматолог'), ('obstetrician-gynecologist', 'акушер-гинеколог'), ('pediator', 'педиатор'), ('ophthalmologist', 'офтальмолог')], default='----', max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('1', 'Маловодие'), ('0', 'Норма'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('1', 'Маловодие'), ('0', 'Норма'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
    ]
