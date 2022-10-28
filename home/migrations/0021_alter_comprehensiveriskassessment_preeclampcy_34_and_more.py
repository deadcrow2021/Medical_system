# Generated by Django 4.1 on 2022-10-28 01:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_appointmentlist_service_and_more'),
    ]

    operations = [
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
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('1', 'Первая'), ('', ''), ('2', 'Повторная'), ('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно')], max_length=1, verbose_name='Беременность'),
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
            field=models.CharField(choices=[('obstetrician-gynecologist', 'Акушер-гинеколог'), ('therapist', 'Терапевт'), ('pediator', 'Педиатор'), ('dentist', 'Стоматолог'), ('', ''), ('ophthalmologist', 'Офтальмолог'), ('specialist', 'Специалист')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Инзенский', 'Инзенский район'), ('Барышский', 'Барышский район'), ('Павловский', 'Павловский район'), ('Николаевский', 'Николаевский район'), ('Старомайнский', 'Старомайнский район'), ('Тереньгульский', 'Тереньгульский район'), ('Вешкаймский', 'Вешкаймский район'), ('Кузоватовский', 'Кузоватовский район'), ('Новоспасский', 'Новоспасский район'), ('Базарносызганский', 'Базарносызганский район'), ('Сурский', 'Сурский район'), ('Цильнинский', 'Цильнинский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Карсунский', 'Карсунский район'), ('', ''), ('Майнский', 'Майнский район'), ('Чердаклинский', 'Чердаклинский район '), ('Мелекесский', 'Мелекесский район'), ('Ульяновский', 'Ульяновский район'), ('Радищевский', 'Радищевский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Новомалыклинский', 'Новомалыклинский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('d', 'Наркотики'), ('s', 'Курение'), ('a', 'Алкоголь'), ('', '')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('под', 'Подвижна'), ('приж', 'Прижата'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('1', 'Плотная'), ('2', 'Размягченная'), ('3', 'Мягкая'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Кпереди'), ('1', 'Кзади'), ('3', 'Расположена по центру')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_length',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000)], verbose_name='Длина шейки матки (мм)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('3', 'Пропускает палец'), ('1', 'Сомкнут'), ('2', 'Пропускает кончик пальца'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
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
            field=models.CharField(blank=True, choices=[('4', 'Масталгия'), ('3', 'Безболезненны '), ('', ''), ('1', 'Патологических изменений нет'), ('2', 'Пальпируется узловое образование')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('3', 'Недостаточно выражена'), ('2', 'По мужскому типу'), ('1', 'По женскому типу'), ('5', 'Избыточно выражена'), ('', ''), ('4', 'Нормально выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('гол', 'Головка'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('1', 'Подвижное'), ('3', 'Болезненное'), ('2', 'Безболезненное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('0', 'Плановая'), ('1', 'Экстренная'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='where',
            field=models.CharField(blank=True, choices=[('1', 'В отделение акушерского ухода'), ('0', 'В отделение патологии беременности'), ('', '')], max_length=1, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability',
            field=models.CharField(blank=True, choices=[('3', 'Группа 3'), ('2', 'Группа 2'), ('1', 'Группа 1'), ('', '')], max_length=200, null=True, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('1', 'Начальное'), ('2', 'Высшее'), ('2', 'Среднее'), ('', '')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('3', 'B(III)'), ('1', 'O(I)'), ('', ''), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('3', 'Состоит в незарегистрированном браке'), ('4', 'Вдова'), ('', '----'), ('1', 'Никогда не состояла в браке'), ('6', 'Разошлась'), ('5', 'Разведена'), ('2', 'Состоит в зарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('3', 'B(III)'), ('1', 'O(I)'), ('', ''), ('4', 'AB(IV)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('1', 'Первая явка'), ('30-40', 'Явка на 30-40 неделе'), ('11-14', 'Явка на 11-14 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('', '')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('', ''), ('1-2w', '1-2 раза в неделю'), ('1-2m', '1-2 раза в месяц'), ('1', 'Каждый день')], max_length=10, null=True, verbose_name='Алкоголь'),
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
            field=models.CharField(blank=True, choices=[('2', 'Умеренные'), ('3', 'Обильные'), ('1', 'Скудные'), ('', '')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('1>', 'Больше 1 пачки'), ('1/2-1', 'От 1/2 до 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('', '')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('', ''), ('s', 'Самопроизвольный'), ('a', 'Искусственный')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('sc', 'Самопроизвольным - с осложнениями'), ('swc', 'Самопроизвольным - без осложнений'), ('ocs', 'Оперативным - кесарево сечение'), ('', '')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('a', 'Аборт'), ('b', 'Роды'), ('d', 'Смерть'), ('', '')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('под', 'Подвижна'), ('приж', 'Прижата'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('-', 'Не ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('др', 'Другое'), ('гол', 'Головка'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('3', 'Самопроизовльный выкидыш'), ('5', 'Неразвивающаяся беременность'), ('6', 'Пузырный занос'), ('4', 'Искусственный аборт'), ('', ''), ('1', 'Срочные/Преждевременные'), ('2', 'Кесарево сечение')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('3', 'ВРТ'), ('1', 'Самопроизовльно'), ('2', 'Индуцироваа'), ('', '')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('obstetrician-gynecologist', 'Акушер-гинеколог'), ('therapist', 'Терапевт'), ('pediator', 'Педиатор'), ('dentist', 'Стоматолог'), ('', ''), ('ophthalmologist', 'Офтальмолог'), ('specialist', 'Специалист')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('0', 'Норма'), ('1', 'Маловодие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('2', 'Многоводие'), ('0', 'Норма'), ('1', 'Маловодие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.CreateModel(
            name='MODelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery', models.CharField(blank=True, choices=[('1', '1 уровень'), ('2', '2 уровень'), ('3', '3 уровень'), ('', '')], max_length=10, null=True, verbose_name='МО родоразрешения')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mo_delivery', to='home.patient')),
            ],
        ),
    ]
