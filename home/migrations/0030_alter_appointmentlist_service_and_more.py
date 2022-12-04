# Generated by Django 4.1 on 2022-12-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_alter_appointmentlist_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentlist',
            name='service',
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'Лабораторная диагностика'), ('2', 'Инструментальная диагностика'), ('3', 'Консультация')], max_length=10, null=True, verbose_name='Услуга'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='embryo_transfer',
            field=models.CharField(blank=True, choices=[('1', 'Нативного'), ('2', 'Криоконсервированного'), ('', '')], max_length=1, verbose_name='Перенос эмбрионов'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='pregnancy',
            field=models.CharField(blank=True, choices=[('4', 'Индуцирована с помощью ВРТ'), ('3', 'Наступила спонтанно'), ('', ''), ('1', 'Первая'), ('2', 'Повторная')], max_length=1, verbose_name='Беременность'),
        ),
        migrations.AlterField(
            model_name='currentpregnancyinfo',
            name='upcoming_births',
            field=models.CharField(blank=True, choices=[('', ''), ('2', 'Повторные'), ('1', 'Первые')], max_length=1, verbose_name='Предстоящие роды'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('therapist', 'Терапевт'), ('', ''), ('pediator', 'Педиатр'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('ophthalmologist', 'Офтальмолог'), ('nurse', 'Медсестра'), ('dentist', 'Стоматолог'), ('receptionist', 'Регистратор'), ('specialist', 'Специалист'), ('assistant', 'Лаборант')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Майнский', 'Майнский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Радищевский', 'Радищевский район'), ('Базарносызганский', 'Базарносызганский район'), ('Барышский', 'Барышский район'), ('Новоспасский', 'Новоспасский район'), ('Вешкаймский', 'Вешкаймский район'), ('Чердаклинский', 'Чердаклинский район '), ('Мелекесский', 'Мелекесский район'), ('Цильнинский', 'Цильнинский район'), ('Старомайнский', 'Старомайнский район'), ('Карсунский', 'Карсунский район'), ('Инзенский', 'Инзенский район'), ('Кузоватовский', 'Кузоватовский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Ульяновский', 'Ульяновский район'), ('Павловский', 'Павловский район'), ('', ''), ('Николаевский', 'Николаевский район'), ('Сурский', 'Сурский район'), ('Тереньгульский', 'Тереньгульский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='fatherinfo',
            name='bad_habits',
            field=models.CharField(blank=True, choices=[('', ''), ('d', 'Наркотики'), ('a', 'Алкоголь'), ('s', 'Курение')], max_length=10, null=True, verbose_name='Вредные привычки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('под', 'Подвижна'), ('приж', 'Прижата'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix',
            field=models.CharField(blank=True, choices=[('', ''), ('3', 'Мягкая'), ('1', 'Плотная'), ('2', 'Размягченная')], max_length=10, null=True, verbose_name='Шейка матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='cervix_deviations',
            field=models.CharField(blank=True, choices=[('1', 'Кзади'), ('3', 'Расположена по центру'), ('2', 'Кпереди'), ('', '')], max_length=10, null=True, verbose_name='Отклонения шейки матки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='external_pharynx',
            field=models.CharField(blank=True, choices=[('3', 'Пропускает палец'), ('1', 'Сомкнут'), ('2', 'Пропускает кончик пальца'), ('', '')], max_length=1, null=True, verbose_name='Наружний зев'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('попер', 'Попереченое'), ('кос', 'Косое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='left_appendages',
            field=models.CharField(blank=True, choices=[('1', 'Без особенностей'), ('2', 'Есть особенности'), ('', '')], max_length=1, null=True, verbose_name='Придатки слева'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='mammary',
            field=models.CharField(blank=True, choices=[('3', 'Безболезненны '), ('4', 'Масталгия'), ('', ''), ('2', 'Пальпируется узловое образование'), ('1', 'Патологических изменений нет')], max_length=1, verbose_name='Осмотр и пальпация молочных желез'),
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
            field=models.CharField(blank=True, choices=[('', ''), ('1', 'По женскому типу'), ('4', 'Нормально выражена'), ('2', 'По мужскому типу'), ('5', 'Избыточно выражена'), ('3', 'Недостаточно выражена')], max_length=1, verbose_name='Распределение и выраженность подкожной жировой клетчатки'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('', ''), ('тк', 'Тазовый конец'), ('гол', 'Головка'), ('др', 'Другое')], max_length=10, null=True, verbose_name='Над входом в малый таз (после 34 недель)'),
        ),
        migrations.AlterField(
            model_name='firstexamination',
            name='uterus_body',
            field=models.CharField(blank=True, choices=[('3', 'Болезненное'), ('1', 'Подвижное'), ('2', 'Безболезненное'), ('', '')], max_length=1, null=True, verbose_name='Тело матки. Характеристика'),
        ),
        migrations.AlterField(
            model_name='hospitalizationinformation',
            name='hosp_type',
            field=models.CharField(blank=True, choices=[('', ''), ('0', 'Плановая'), ('1', 'Экстренная')], max_length=1, null=True, verbose_name='Вид'),
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
            name='father_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('', ''), ('4', 'AB(IV)'), ('2', 'A(II)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='father_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор отца ребенка'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('5', 'Разведена'), ('1', 'Никогда не состояла в браке'), ('3', 'Состоит в незарегистрированном браке'), ('6', 'Разошлась'), ('4', 'Вдова'), ('', '----'), ('2', 'Состоит в зарегистрированном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_group',
            field=models.CharField(blank=True, choices=[('3', 'B(III)'), ('', ''), ('4', 'AB(IV)'), ('2', 'A(II)'), ('1', 'O(I)')], max_length=1, null=True, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='mother_blood_rh',
            field=models.CharField(blank=True, choices=[('+', '+'), ('-', '-'), ('', '')], max_length=1, null=True, verbose_name='Rh-фактор'),
        ),
        migrations.AlterField(
            model_name='obstetricrisk',
            name='visit',
            field=models.CharField(blank=True, choices=[('30-40', 'Явка на 30-40 неделе'), ('18-20', 'Явка на 18-20 неделе'), ('11-14', 'Явка на 11-14 неделе'), ('', ''), ('1', 'Первая явка')], max_length=5, null=True, verbose_name='Срок явки'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='alcohol',
            field=models.CharField(blank=True, choices=[('1-2w', '1-2 раза в неделю'), ('1', 'Каждый день'), ('1-2m', '1-2 раза в месяц'), ('', '')], max_length=10, null=True, verbose_name='Алкоголь'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='dispensary_accounting',
            field=models.CharField(blank=True, choices=[('1', 'Состояла'), ('0', 'Не состояла'), ('', '')], max_length=1, null=True, verbose_name='Диспансерский учет'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='profusion',
            field=models.CharField(blank=True, choices=[('3', 'Обильные'), ('2', 'Умеренные'), ('1', 'Скудные'), ('', '')], max_length=10, null=True, verbose_name='Обильность'),
        ),
        migrations.AlterField(
            model_name='patientinformation',
            name='regularity',
            field=models.CharField(blank=True, choices=[('1', 'Регулярные'), ('0', 'Нерегулярные'), ('', '')], max_length=10, null=True, verbose_name='Регулярность'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_abortion',
            field=models.CharField(blank=True, choices=[('a', 'Искусственный'), ('s', 'Самопроизвольный'), ('', '')], max_length=10, null=True, verbose_name='Аборт'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='if_childbirth',
            field=models.CharField(blank=True, choices=[('sc', 'Самопроизвольным - с осложнениями'), ('ocs', 'Оперативным - кесарево сечение'), ('swc', 'Самопроизвольным - без осложнений'), ('', '')], max_length=10, null=True, verbose_name='Роды'),
        ),
        migrations.AlterField(
            model_name='pregnancyoutcome',
            name='pregnancy_outcome',
            field=models.CharField(blank=True, choices=[('', ''), ('b', 'Роды'), ('d', 'Смерть'), ('a', 'Аборт')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='adjacent_part',
            field=models.CharField(blank=True, choices=[('под', 'Подвижна'), ('приж', 'Прижата'), ('', '')], max_length=10, null=True, verbose_name='Предлежащая часть'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetal_position',
            field=models.CharField(blank=True, choices=[('прод', 'Продольное'), ('попер', 'Попереченое'), ('кос', 'Косое'), ('', '')], max_length=10, null=True, verbose_name='Положение плода'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='fetus_stirring',
            field=models.CharField(blank=True, choices=[('-', 'Не ощущается'), ('+', 'Ощущается'), ('', '')], max_length=10, null=True, verbose_name='Шевеление плода: (>16 недель)'),
        ),
        migrations.AlterField(
            model_name='pregnantwomanmonitoring',
            name='to_pelvis_entrance',
            field=models.CharField(blank=True, choices=[('', ''), ('тк', 'Тазовый конец'), ('гол', 'Головка'), ('др', 'Другое')], max_length=10, null=True, verbose_name='Над входом в малый таз'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='outcome',
            field=models.CharField(blank=True, choices=[('1', 'Срочные/Преждевременные'), ('3', 'Самопроизовльный выкидыш'), ('5', 'Неразвивающаяся беременность'), ('', ''), ('6', 'Пузырный занос'), ('4', 'Искусственный аборт'), ('2', 'Кесарево сечение')], max_length=10, null=True, verbose_name='Исход беременности'),
        ),
        migrations.AlterField(
            model_name='previouspregnancy',
            name='pragnancy_has_come',
            field=models.CharField(blank=True, choices=[('3', 'ВРТ'), ('1', 'Самопроизовльно'), ('', ''), ('2', 'Индуцирована')], max_length=10, null=True, verbose_name='Наступила'),
        ),
        migrations.AlterField(
            model_name='receptionnotes',
            name='specialization',
            field=models.CharField(choices=[('therapist', 'Терапевт'), ('', ''), ('pediator', 'Педиатр'), ('obstetrician-gynecologist', 'Акушер-гинеколог'), ('ophthalmologist', 'Офтальмолог'), ('nurse', 'Медсестра'), ('dentist', 'Стоматолог'), ('receptionist', 'Регистратор'), ('specialist', 'Специалист'), ('assistant', 'Лаборант')], max_length=30, verbose_name='Специальность врача'),
        ),
        migrations.AlterField(
            model_name='ultrasoundexamination_30_34',
            name='presentation',
            field=models.CharField(blank=True, choices=[('0', 'Головное'), ('1', 'Тазовое'), ('', '')], max_length=1, null=True, verbose_name='Предлежание'),
        ),
        migrations.CreateModel(
            name='SAMD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('sms_status', models.CharField(blank=True, choices=[('2', 'Неправильно введены данные'), ('1', 'Недостаточно данных'), ('3', 'Не подписан'), ('', ''), ('5', 'Отправлен'), ('4', 'Готов к отправке')], max_length=300, verbose_name='Статус версии СМС')),
                ('patient_fio', models.CharField(blank=True, max_length=10, verbose_name='ФИО пациента')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('sms_type', models.CharField(blank=True, max_length=300, verbose_name='Тип СМС')),
                ('med_org', models.CharField(blank=True, choices=[('', ''), ('1', 'ГУЗ «Центральная городская клиническая больница г. Ульяновска»'), ('2', 'ГУЗ «Центральная клиническая медико-санитарная часть имени заслуженного врача России В.А.Егорова»'), ('3', 'ГУЗ  «Ульяновская областная клиническая станция скорой медицинской помощи»'), ('4', 'ГУЗ «Городская клиническая больница № 1» (Перинатальный центр)'), ('5', 'ГУЗ «Городская больница №2»'), ('6', 'ГУЗ Городская больница № 3'), ('7', 'ГУЗ Детская городская клиническая больница г. Ульяновска'), ('8', 'ГУЗ  городская поликлиника № 1 им. С.М. Кирова'), ('9', 'ГУЗ Городская поликлиника № 3'), ('10', 'ГУЗ «Городская поликлиника № 4»'), ('11', 'ГУЗ «Городская поликлиника №5»'), ('12', 'ГУЗ «Городская поликлиника №6»'), ('13', 'ГБУЗ «Стоматологическая поликлиника города Ульяновска»'), ('14', 'ГУЗ «Базарносызганская районная больница»'), ('15', 'ГУЗ «Барышская районная больница»'), ('16', 'ГУЗ Большенагаткинская районная больница'), ('17', 'ГУЗ Вешкаймская районная больница'), ('18', 'ГУЗ  «Инзенская районная больница»'), ('19', 'ГУЗ  «Карсунская районная больница имени врача В.И. Фиошина»'), ('20', 'ГУЗ «Кузоватовская районная больница»'), ('21', 'ГУЗ  «Майнская районная больница»'), ('22', 'ГУЗ «Николаевская районная больница»'), ('23', 'ГУЗ «Новоульяновская городская больница им. А.Ф.Альберт»'), ('24', 'ГУЗ «Новомалыклинская районная больница»'), ('25', 'ГУЗ «Новоспасская районная больница»'), ('26', 'ГУЗ «Павловская районная больница имени заслуженного врача России А.И.Марьина»'), ('27', 'ГУЗ Радищевская районная больница'), ('28', 'ГУЗ «Сенгилеевская районная больница»'), ('29', 'ГУЗ «Старокулаткинская районная больница»'), ('30', 'ГУЗ «Старомайнская районная больница»'), ('31', 'ГУЗ Сурская районная больница'), ('32', 'ГУЗ «Тереньгульская районная больница»'), ('33', 'ГУЗ «Ульяновская районная больница»'), ('34', 'ГУЗ «Чердаклинская районная больница»'), ('35', 'ГУЗ Зерносовхозская участковая больница'), ('36', 'ГУЗ Мулловская участковая больница'), ('37', 'ГУЗ Ново-Майнская городская больница'), ('38', 'ГУЗ Рязановская участковая больница'), ('39', 'ГУЗ Тиинская участковая больница'), ('40', 'ГУЗ Ульяновская областная клиническая больница'), ('41', 'ГУЗ «Ульяновская областная детская клиническая больница имени политического и общественного деятеля Ю.Ф.Горячева»'), ('42', 'ГУЗ «Ульяновский областной клинический центр специализированных видов медицинской помощи им. Е.М. Чучкалова»'), ('43', 'ГУЗ «Ульяновский областной клинический госпиталь ветеранов войн»'), ('44', 'ГКУЗ «Ульяновская областная клиническая психиатрическая больница имени В.А. Копосова»'), ('45', 'ГУЗ Областной клинический онкологический диспансер'), ('46', 'ГУЗ «Областной кардиологический диспансер»'), ('47', 'ГКУЗ «Областной клинический противотуберкулезный диспансер имени С.Д. Грязнова»'), ('48', 'ГУЗ «Областной клинический кожно-венерологический диспансер»'), ('49', 'ГУЗ «Ульяновская областная клиническая наркологическая больница»'), ('50', 'ГУЗ «Ульяновский областной клинический медицинский центр оказания помощи лицам, пострадавшим от радиационного воздействия, и профессиональной патологии им. Героя РФ Максимчука В.М.»'), ('51', 'ГУЗ Ульяновская областная станция переливания крови'), ('52', 'ГУЗ «Областной центр профилактики и борьбы со СПИД»'), ('53', 'ГУЗ «Областной врачебно-физкультурный диспансер»'), ('54', 'ГУЗ «Детская специализированная психоневрологическая больница № 1»'), ('55', 'ГУЗ «Детская специализированная психоневрологическая больница № 2»'), ('56', 'ГУЗ «Областная детская инфекционная больница»'), ('57', 'ГКУЗ «Областной специализированный дом ребёнка для детей с органическим поражением центральной нервной системы с нарушением психики»'), ('58', 'ГКУЗ Ульяновский областной «ХОСПИС»'), ('59', 'ГУЗ Областной противотуберкулезный санаторий имени врача А.А.Тамарова'), ('60', 'ГУЗ «Костно-туберкулезный санаторий «Сосновка»'), ('61', 'ГУЗ Детский противотуберкулезный санаторий «Белое Озеро»'), ('62', 'ГКУЗ «Ульяновское областное бюро судебно-медицинской экспертизы»'), ('63', 'ГКУЗ Областной медицинский центр мобилизационных резервов «Резерв»'), ('64', 'ГУЗ Ульяновский территориальный центр медицины катастроф'), ('65', 'ГУЗ «Центр общественного здоровья и медицинской профилактики Ульяновской области»'), ('66', 'ГУЗ «Ульяновский областной медицинский информационно-аналитический центр»'), ('67', 'ГБУЗ «Ульяновская областная дезинфекционная станция»'), ('68', 'ГУ «Ульяновская государственная аптека»')], max_length=10, verbose_name='Медицинская организация')),
                ('trigger', models.CharField(blank=True, choices=[('1', 'Направление на оказание медицинских услуг'), ('', '')], max_length=10, verbose_name='Триггер')),
                ('signed', models.BooleanField(default=False, verbose_name='Подпись')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samd', to='home.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samd', to='home.patient')),
            ],
        ),
    ]
