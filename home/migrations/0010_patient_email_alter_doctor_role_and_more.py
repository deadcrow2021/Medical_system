# Generated by Django 4.1.1 on 2022-10-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_doctor_role_alter_doctor_territory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='role',
            field=models.CharField(choices=[('акушер-гинеколог', 'акушер-гинеколог'), ('стоматолог', 'стоматолог'), ('специалист', 'специалист'), ('терапевт ', 'терапевт'), ('офтальмолог', 'офтальмолог'), ('педиатор', 'педиатор')], default='----', max_length=30, verbose_name='Должность врача'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='territory',
            field=models.CharField(choices=[('Новоспасский', 'Новоспасский район'), ('Тереньгульский', 'Тереньгульский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('', '----'), ('Мелекесский', 'Мелекесский район'), ('Инзенский', 'Инзенский район'), ('Карсунский', 'Карсунский район'), ('Старомайнский', 'Старомайнский район'), ('Ульяновский', 'Ульяновский район'), ('Сурский', 'Сурский район'), ('Цильнинский', 'Цильнинский район'), ('Базарносызганский', 'Базарносызганский район'), ('Барышский', 'Барышский район'), ('Чердаклинский', 'Чердаклинский район '), ('Николаевский', 'Николаевский район'), ('Кузоватовский', 'Кузоватовский район'), ('Радищевский', 'Радищевский район'), ('Майнский', 'Майнский район'), ('Вешкаймский', 'Вешкаймский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Павловский', 'Павловский район')], default='Ульяновский', max_length=25, verbose_name='Территория'),
        ),
        migrations.AlterField(
            model_name='medicalcard',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('1', 'Никогда не состояла в браке'), ('6', 'Разошлась'), ('3', 'Состоит в незарегистриро-ванном браке'), ('', '----'), ('4', 'Вдова'), ('5', 'Разведена'), ('2', 'Состоит в зарегистри-рованном браке')], default='', max_length=1, null=True, verbose_name='Брачное состояние'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood',
            field=models.CharField(blank=True, choices=[('2-', 'A(II) Rh- '), ('1-', 'O(I) Rh- '), ('4+', 'AB(IV) Rh+'), ('4-', 'AB(IV) Rh-'), ('3+', 'B(III) Rh+ '), ('2+', 'A(II) Rh+ '), ('3-', 'B(III) Rh- '), ('1+', 'O(I) Rh+ ')], max_length=2, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='city_village',
            field=models.CharField(choices=[('', '----'), ('1', 'Город'), ('2', 'Село')], max_length=1, verbose_name='Житель города/села'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='disability',
            field=models.CharField(blank=True, choices=[('3', 'Третья'), ('2', 'Вторая'), ('1', 'Первая')], max_length=1, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('', '----'), ('f', 'Женский'), ('m', 'Мужской')], default='f', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='insurance',
            field=models.CharField(blank=True, choices=[('1', 'АО «Медицинская акционерная страховая компания» (АО «МАКС-М»)'), ('3', 'ООО «Страховая медицинская компания РЕСО-МЕД» (Московский филиал)'), ('4', 'АО «Страховая компания «СОГАЗ-Мед»»'), ('2', 'ООО «МСК «МЕДСТРАХ»»'), ('5', 'ООО «Страховая компания «Ингосстрах-М»'), ('6', 'ООО «КАПИТАЛ МС» ')], max_length=1, verbose_name='Сраховая компания'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_status',
            field=models.CharField(blank=True, choices=[('l', 'Низший'), ('m', 'Средний'), ('h', 'Высший')], max_length=1, verbose_name='Соц. Статус'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='territory',
            field=models.CharField(choices=[('Новоспасский', 'Новоспасский район'), ('Тереньгульский', 'Тереньгульский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('', '----'), ('Мелекесский', 'Мелекесский район'), ('Инзенский', 'Инзенский район'), ('Карсунский', 'Карсунский район'), ('Старомайнский', 'Старомайнский район'), ('Ульяновский', 'Ульяновский район'), ('Сурский', 'Сурский район'), ('Цильнинский', 'Цильнинский район'), ('Базарносызганский', 'Базарносызганский район'), ('Барышский', 'Барышский район'), ('Чердаклинский', 'Чердаклинский район '), ('Николаевский', 'Николаевский район'), ('Кузоватовский', 'Кузоватовский район'), ('Радищевский', 'Радищевский район'), ('Майнский', 'Майнский район'), ('Вешкаймский', 'Вешкаймский район'), ('Сенгилеевский', 'Сенгилеевский район'), ('Старокулаткинский', 'Старокулаткинский район'), ('Павловский', 'Павловский район')], max_length=25, verbose_name='Территория'),
        ),
    ]
