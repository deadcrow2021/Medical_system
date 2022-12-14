# Generated by Django 4.1 on 2022-12-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0038_receptionnotes_date_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalcard',
            name='territory',
            field=models.CharField(choices=[('Инзенский', 'Инзенский район'), ('Николаевский', 'Николаевский район'), ('Барышский', 'Барышский район'), ('Мелекесский', 'Мелекесский район'), ('Майнский', 'Майнский район'), ('Ульяновский', 'Ульяновский район'), ('Базарносызганский', 'Базарносызганский район'), ('Кузоватовский', 'Кузоватовский район'), ('Радищевский', 'Радищевский район'), ('Сурский', 'Сурский район'), ('Чердаклинский', 'Чердаклинский район '), ('Сенгилеевский', 'Сенгилеевский район'), ('', ''), ('Новомалыклинский', 'Новомалыклинский район'), ('Новоспасский', 'Новоспасский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Павловский', 'Павловский район'), ('Вешкаймский', 'Вешкаймский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Цильнинский', 'Цильнинский район'), ('Карсунский', 'Карсунский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('2', 'Инструментальная диагностика'), ('3', 'Консультация'), ('1', 'Лабораторная диагностика'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
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
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Правая'), ('2', 'Левая')], max_length=1, null=True, verbose_name='ПИ маточных артерий'),
        ),
        migrations.AlterField(
            model_name='comprehensiveriskassessment',
            name='zrp',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Задержка развития плода'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Нативного'), ('2', 'Криоконсервированного')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('2', 'Повторная'), ('', ''), ('1', 'Первая'), ('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('1', 'Первые'), ('2', 'Повторные'), ('', '')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('receptionist', 'Регистратор'), ('specialist', 'Специалист'), ('pediator', 'Педиатр'), ('assistant', 'Лаборант'), ('ophthalmologist', 'Офтальмолог'), ('', ''), ('nurse', 'Медсестра'), ('dentist', 'Стоматолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('therapist', 'Терапевт')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Инзенский', 'Инзенский район'), ('Николаевский', 'Николаевский район'), ('Барышский', 'Барышский район'), ('Мелекесский', 'Мелекесский район'), ('Майнский', 'Майнский район'), ('Ульяновский', 'Ульяновский район'), ('Базарносызганский', 'Базарносызганский район'), ('Кузоватовский', 'Кузоватовский район'), ('Радищевский', 'Радищевский район'), ('Сурский', 'Сурский район'), ('Чердаклинский', 'Чердаклинский район '), ('Сенгилеевский', 'Сенгилеевский район'), ('', ''), ('Новомалыклинский', 'Новомалыклинский район'), ('Новоспасский', 'Новоспасский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Павловский', 'Павловский район'), ('Вешкаймский', 'Вешкаймский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Цильнинский', 'Цильнинский район'), ('Карсунский', 'Карсунский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('d', 'Наркотики'), ('s', 'Курение'), ('a', 'Алкоголь'), ('', '')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('3', 'Мягкая'), ('1', 'Плотная'), ('2', 'Размягченная'), ('', '')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('1', 'Кзади'), ('2', 'Кпереди'), ('3', 'Расположена по центру'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('3', 'Пропускает палец'), ('2', 'Пропускает кончик пальца'), ('1', 'Сомкнут'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('-', 'Не ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('4', 'Масталгия'), ('1', 'Патологических изменений нет'), ('', ''), ('3', 'Безболезненны '), ('2', 'Пальпируется узловое образование')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('3', 'Недостаточно выражена'), ('4', 'Нормально выражена'), ('', ''), ('1', 'По женскому типу'), ('5', 'Избыточно выражена'), ('2', 'По мужскому типу')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('3', 'Болезненное'), ('2', 'Безболезненное'), ('1', 'Подвижное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='where',
            field=models.CharField(blank=True, choices=[('0', 'В отделение патологии беременности'), ('1', 'В отделение акушерского ухода'), ('', '')], max_length=1, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability',
            field=models.CharField(blank=True, choices=[('3', 'Группа 3'), ('1', 'Группа 1'), ('2', 'Группа 2'), ('', '')], max_length=200, null=True, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('2', 'Высшее'), ('1', 'Начальное'), ('2', 'Среднее'), ('', '')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('2', 'Состоит в зарегистрированном браке'), ('', '----'), ('3', 'Состоит в незарегистрированном браке'), ('1', 'Никогда не состояла в браке'), ('5', 'Разведена'), ('4', 'Вдова'), ('6', 'Разошлась')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)'), ('3', 'B(III)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('-', '-'), ('+', '+'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='modelivery',
            name='delivery',
            field=models.CharField(blank=True, choices=[('2', '2 уровень'), ('3', '3 уровень'), ('', ''), ('1', '1 уровень')], max_length=10, null=True, verbose_name='МО родоразрешения'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Первая явка'), ('11-14', 'Явка на 11-14 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('', ''), ('1-2m', '1-2 раза в месяц'), ('1-2w', '1-2 раза в неделю'), ('1', 'Каждый день')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('1', 'Состояла'), ('0', 'Не состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='growth_retardation_risk',
            field=models.CharField(blank=True, choices=[('0', 'Низкий'), ('1', 'Высокий'), ('', '')], max_length=1, null=True, verbose_name='Риск задержки роста плода'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='hiv_status',
            field=models.CharField(blank=True, choices=[('1', 'Положительный'), ('0', 'Отрицательный'), ('', '')], max_length=1, null=True, verbose_name='ВИЧ-статус'),
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
            field=models.CharField(blank=True, choices=[('1', 'Скудные'), ('2', 'Умеренные'), ('3', 'Обильные'), ('', '')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'Нерегулярные'), ('1', 'Регулярные')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('', ''), ('1>', 'Больше 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('1/2-1', 'От 1/2 до 1 пачки')], max_length=10, null=True, verbose_name='Курение (в день)'),
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
            field=models.CharField(blank=True, choices=[('', ''), ('swc', 'Самопроизвольным - без осложнений'), ('ocs', 'Оперативным - кесарево сечение'), ('sc', 'Самопроизвольным - с осложнениями')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('d', 'Смерть'), ('a', 'Аборт'), ('b', 'Роды'), ('', '')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('+', 'Ощущается'), ('-', 'Не ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('гол', 'Головка'), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('', '')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('3', 'Самопроизовльный выкидыш'), ('6', 'Пузырный занос'), ('4', 'Искусственный аборт'), ('5', 'Неразвивающаяся беременность'), ('2', 'Кесарево сечение'), ('1', 'Срочные/Преждевременные'), ('', '')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Самопроизовльно'), ('2', 'Индуцирована'), ('3', 'ВРТ')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(blank=True, choices=[('receptionist', 'Регистратор'), ('specialist', 'Специалист'), ('pediator', 'Педиатр'), ('assistant', 'Лаборант'), ('ophthalmologist', 'Офтальмолог'), ('', ''), ('nurse', 'Медсестра'), ('dentist', 'Стоматолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('therapist', 'Терапевт')], max_length=30, null=True, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='status',
            field=models.CharField(blank=True, choices=[('required', 'Требуется запись'), ('recorded', 'Записана на'), ('declined', 'Отклонение'), ('completed', 'Выполнено')], max_length=20, null=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='samd',
            name='sms_status',
            field=models.CharField(blank=True, choices=[('1', 'Недостаточно данных'), ('3', 'Не подписан'), ('', ''), ('5', 'Отправлен'), ('4', 'Готов к отправке'), ('2', 'Неправильно введены данные')], max_length=300, verbose_name='Статус версии СМС'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'Норма'), ('1', 'Маловодие'), ('2', 'Многоводие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'Норма'), ('1', 'Маловодие'), ('2', 'Многоводие')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('1', 'Тазовое'), ('', ''), ('0', 'Головное')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
    ]
