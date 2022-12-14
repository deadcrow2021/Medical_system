# Generated by Django 4.1.2 on 2022-11-09 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_comprehensiveriskassessment_preeclampcy_34_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('1', 'Лабораторная диагностика'), ('3', 'Консультация'), ('2', 'Инструментальная диагностика'), ('', '')], max_length=10, null=True, verbose_name='Услуга'),
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
            field=models.CharField(blank=True, choices=[('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно'), ('', ''), ('2', 'Повторная'), ('1', 'Первая')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy_1',
            field=models.CharField(blank=True, choices=[('1', 'Одноплодность'), ('2', 'Многоплодность'), ('', '')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('specialist', 'Специалист'), ('pediator', 'Педиатор'), ('therapist', 'Терапевт'), ('', ''), ('ophthalmologist', 'Офтальмолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('dentist', 'Стоматолог')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Сурский', 'Сурский район'), ('Инзенский', 'Инзенский район'), ('Цильнинский', 'Цильнинский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Мелекесский', 'Мелекесский район'), ('Чердаклинский', 'Чердаклинский район '), ('Николаевский', 'Николаевский район'), ('Ульяновский', 'Ульяновский район'), ('Новоспасский', 'Новоспасский район'), ('Павловский', 'Павловский район'), ('Майнский', 'Майнский район'), ('Барышский', 'Барышский район'), ('', ''), ('Карсунский', 'Карсунский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Тереньгульский', 'Тереньгульский район'), ('Базарносызганский', 'Базарносызганский район'), ('Радищевский', 'Радищевский район'), ('Кузоватовский', 'Кузоватовский район'), ('Вешкаймский', 'Вешкаймский район'), ('Старомайнский', 'Старомайнский район'), ('Сенгилеевский', 'Сенгилеевский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('d', 'Наркотики'), ('a', 'Алкоголь'), ('s', 'Курение'), ('', '')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('3', 'Расположена по центру'), ('1', 'Кзади'), ('2', 'Кпереди'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Пропускает кончик пальца'), ('3', 'Пропускает палец'), ('1', 'Сомкнут')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('2', 'Есть особенности'), ('1', 'Без особенностей'), ('', '')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('3', 'Безболезненны '), ('', ''), ('2', 'Пальпируется узловое образование'), ('1', 'Патологических изменений нет'), ('4', 'Масталгия')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='nipples',
            field=models.CharField(blank=True, choices=[('1', 'Сформированы правильно'), ('2', 'Втянуты'), ('', '')], max_length=1, verbose_name='Осмотр и пальпация сосков'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='right_appendages',
            field=models.CharField(blank=True, choices=[('2', 'Есть особенности'), ('1', 'Без особенностей'), ('', '')], max_length=1, null=True, verbose_name='Придатки справа'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='subcutaneous_fat_severity',
            field=models.CharField(blank=True, choices=[('3', 'Недостаточно выражена'), ('1', 'По женскому типу'), ('2', 'По мужскому типу'), ('', ''), ('5', 'Избыточно выражена'), ('4', 'Нормально выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('', ''), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('гол', 'Головка')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('3', 'Болезненное'), ('', ''), ('2', 'Безболезненное'), ('1', 'Подвижное')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('1', 'Экстренная'), ('0', 'Плановая'), ('', '')], max_length=1, null=True, verbose_name='Вид'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='where',
            field=models.CharField(blank=True, choices=[('1', 'В отделение акушерского ухода'), ('0', 'В отделение патологии беременности'), ('', '')], max_length=1, verbose_name='Медицинская организация'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='disability',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Группа 1'), ('3', 'Группа 3'), ('2', 'Группа 2')], max_length=200, null=True, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='education',
            field=models.CharField(blank=True, choices=[('2', 'Высшее'), ('1', 'Начальное'), ('2', 'Среднее'), ('', '')], max_length=5, null=True, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('5', 'Разведена'), ('2', 'Состоит в зарегистрированном браке'), ('6', 'Разошлась'), ('', '----'), ('1', 'Никогда не состояла в браке'), ('4', 'Вдова'), ('3', 'Состоит в незарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('1', 'O(I)'), ('3', 'B(III)'), ('4', 'AB(IV)'), ('', ''), ('2', 'A(II)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='modelivery',
            name='delivery',
            field=models.CharField(blank=True, choices=[('1', '1 уровень'), ('3', '3 уровень'), ('2', '2 уровень'), ('', '')], max_length=10, null=True, verbose_name='МО родоразрешения'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('18-20', 'Явка на 18-20 неделе'), ('', ''), ('11-14', 'Явка на 11-14 неделе'), ('1', 'Первая явка'), ('30-40', 'Явка на 30-40 неделе')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1', 'Каждый день'), ('1-2m', '1-2 раза в месяц'), ('1-2w', '1-2 раза в неделю'), ('', '')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='another_risks',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Другие риски'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('1', 'Состояла'), ('0', 'Не состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
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
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Скудные'), ('3', 'Обильные'), ('2', 'Умеренные')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('0', 'Нерегулярные'), ('1', 'Регулярные'), ('', '')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='smoking',
            field=models.CharField(blank=True, choices=[('1>', 'Больше 1 пачки'), ('1/2-1', 'От 1/2 до 1 пачки'), ('<1/2', 'Меньше 1/2 пачки'), ('', '')], max_length=10, null=True, verbose_name='Курение (в день)'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='thromboembolic_complications',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Высокий'), ('0', 'Низкий')], max_length=1, null=True, verbose_name='Риск тромбоэболических осложнений'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('', ''), ('s', 'Самопроизвольный'), ('a', 'Искусственный')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('', ''), ('ocs', 'Оперативным - кесарево сечение'), ('sc', 'Самопроизвольным - с осложнениями'), ('swc', 'Самопроизвольным - без осложнений')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('d', 'Смерть'), ('a', 'Аборт'), ('', ''), ('b', 'Роды')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('', ''), ('др', 'Другое'), ('тк', 'Тазовый конец'), ('гол', 'Головка')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('1', 'Срочные/Преждевременные'), ('2', 'Кесарево сечение'), ('', ''), ('3', 'Самопроизовльный выкидыш'), ('4', 'Искусственный аборт'), ('6', 'Пузырный занос'), ('5', 'Неразвивающаяся беременность')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('1', 'Самопроизовльно'), ('3', 'ВРТ'), ('2', 'Индуцирована'), ('', '')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('specialist', 'Специалист'), ('pediator', 'Педиатор'), ('therapist', 'Терапевт'), ('', ''), ('ophthalmologist', 'Офтальмолог'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('dentist', 'Стоматолог')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_19_21',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('0', 'Норма'), ('2', 'Многоводие'), ('1', 'Маловодие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='amniotic_fluid',
            field=models.CharField(blank=True, choices=[('0', 'Норма'), ('2', 'Многоводие'), ('1', 'Маловодие'), ('', '')], max_length=1, null=True, verbose_name='Околоплодные воды'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'Головное'), ('1', 'Тазовое')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
        migrations.CreateModel(
            name='TelegramUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_user_id', models.PositiveBigIntegerField(unique=True, verbose_name='ID пользователя в Telegram')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.patient')),
            ],
        ),
    ]
