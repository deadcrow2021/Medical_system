# Generated by Django 4.1.2 on 2022-12-10 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_appointmentlist_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='Файл')),
            ],
        ),
        migrations.RemoveField(
            model_name='receptionnotes',
            name='visit_number',
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='date_recording',
            field=models.DateField(default='2001-01-10', verbose_name='Дата записи'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='deadline_from',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Срок выполнения с'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='deadline_to',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Срок выполнения по'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='result',
            field=models.TextField(blank=True, null=True, verbose_name='Результат'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='section',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Раздел'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='service',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('2', 'Инструментальная диагностика'), ('3', 'Консультация'), ('1', 'Лабораторная диагностика'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
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
            name='uterine_pulse_index',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Левая'), ('1', 'Правая')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Задержка развития плода'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Криоконсервированного'), ('1', 'Нативного')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно'), ('1', 'Первая'), ('2', 'Повторная'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('2', 'Повторные'), ('1', 'Первые'), ('', '')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('dentist', 'Стоматолог'), ('', ''), ('therapist', 'Терапевт'), ('specialist', 'Специалист'), ('pediator', 'Педиатр'), ('receptionist', 'Регистратор'), ('ophthalmologist', 'Офтальмолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('assistant', 'Лаборант'), ('nurse', 'Медсестра')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Николаевский', 'Николаевский район'), ('Барышский', 'Барышский район'), ('Ульяновский', 'Ульяновский район'), ('Сурский', 'Сурский район'), ('Майнский', 'Майнский район'), ('Базарносызганский', 'Базарносызганский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Павловский', 'Павловский район'), ('Тереньгульский', 'Тереньгульский район'), ('Чердаклинский', 'Чердаклинский район '), ('', ''), ('Инзенский', 'Инзенский район'), ('Радищевский', 'Радищевский район'), ('Карсунский', 'Карсунский район'), ('Кузоватовский', 'Кузоватовский район'), ('Старомайнский', 'Старомайнский район'), ('Новоспасский', 'Новоспасский район'), ('Мелекесский', 'Мелекесский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Цильнинский', 'Цильнинский район'), ('Вешкаймский', 'Вешкаймский район'), ('Старокулаткинский', 'Старокулаткинский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
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
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Размягченная'), ('3', 'Мягкая'), ('1', 'Плотная')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('1', 'Сомкнут'), ('2', 'Пропускает кончик пальца'), ('3', 'Пропускает палец'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('', ''), ('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('4', 'Масталгия'), ('1', 'Патологических изменений нет'), ('2', 'Пальпируется узловое образование'), ('', ''), ('3', 'Безболезненны ')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='nipples',
            field=models.CharField(blank=True, choices=[('2', 'Втянуты'), ('1', 'Сформированы правильно'), ('', '')], max_length=1, verbose_name='Осмотр и пальпация сосков'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('2', 'По мужскому типу'), ('1', 'По женскому типу'), ('3', 'Недостаточно выражена'), ('', ''), ('5', 'Избыточно выражена'), ('4', 'Нормально выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('тк', 'Тазовый конец'), ('гол', 'Головка'), ('др', 'Другое'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Безболезненное'), ('1', 'Подвижное'), ('3', 'Болезненное')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('0', 'Плановая'), ('1', 'Экстренная'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='where',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'В отделение акушерского ухода'), ('0', 'В отделение патологии беременности')], max_length=1, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability',
            field=models.CharField(blank=True, choices=[('2', 'Группа 2'), ('3', 'Группа 3'), ('1', 'Группа 1'), ('', '')], max_length=200, null=True, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('1', 'Начальное'), ('2', 'Высшее'), ('2', 'Среднее'), ('', '')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('', ''), ('1', 'O(I)'), ('4', 'AB(IV)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('2', 'Состоит в зарегистрированном браке'), ('', '----'), ('6', 'Разошлась'), ('5', 'Разведена'), ('4', 'Вдова'), ('1', 'Никогда не состояла в браке'), ('3', 'Состоит в незарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('2', 'A(II)'), ('', ''), ('1', 'O(I)'), ('4', 'AB(IV)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='modelivery',
            name='delivery',
            field=models.CharField(blank=True, choices=[('3', '3 уровень'), ('1', '1 уровень'), ('2', '2 уровень'), ('', '')], max_length=10, null=True, verbose_name='МО родоразрешения'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('1', 'Первая явка'), ('11-14', 'Явка на 11-14 неделе'), ('30-40', 'Явка на 30-40 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('', '')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('', ''), ('1-2m', '1-2 раза в месяц'), ('1-2w', '1-2 раза в неделю'), ('1', 'Каждый день')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('1', 'Состояла'), ('0', 'Не состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
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
            field=models.CharField(blank=True, choices=[('1', 'Скудные'), ('3', 'Обильные'), ('', ''), ('2', 'Умеренные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('1>', 'Больше 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('1/2-1', 'От 1/2 до 1 пачки'), ('', '')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('1', 'Высокий'), ('0', 'Низкий'), ('', '')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('s', 'Самопроизвольный'), ('a', 'Искусственный'), ('', '')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('', ''), ('sc', 'Самопроизвольным - с осложнениями'), ('swc', 'Самопроизвольным - без осложнений'), ('ocs', 'Оперативным - кесарево сечение')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('', ''), ('d', 'Смерть'), ('b', 'Роды'), ('a', 'Аборт')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('приж', 'Прижата'), ('под', 'Подвижна'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('', ''), ('прод', 'Продольное'), ('кос', 'Косое'), ('попер', 'Попереченое')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('тк', 'Тазовый конец'), ('гол', 'Головка'), ('др', 'Другое'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('5', 'Неразвивающаяся беременность'), ('6', 'Пузырный занос'), ('', ''), ('1', 'Срочные/Преждевременные'), ('3', 'Самопроизовльный выкидыш'), ('4', 'Искусственный аборт'), ('2', 'Кесарево сечение')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('1', 'Самопроизовльно'), ('3', 'ВРТ'), ('2', 'Индуцирована'), ('', '')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='date_meeting',
            field=models.DateTimeField(default=False, null=True, verbose_name='Дата и время приема'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('dentist', 'Стоматолог'), ('', ''), ('therapist', 'Терапевт'), ('specialist', 'Специалист'), ('pediator', 'Педиатр'), ('receptionist', 'Регистратор'), ('ophthalmologist', 'Офтальмолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('assistant', 'Лаборант'), ('nurse', 'Медсестра')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='status',
            field=models.CharField(blank=True, choices=[('required', 'Требуется запись'), ('recorded', 'Записана'), ('declined', 'Отклонение'), ('completed', 'Выполнено')], default='Требуется запись', max_length=20, null=True, verbose_name='Статус'),
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
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('0', 'Головное'), ('1', 'Тазовое'), ('', '')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
        migrations.AddField(
            model_name='receptionnotes',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.file', verbose_name='Файл'),
        ),
    ]