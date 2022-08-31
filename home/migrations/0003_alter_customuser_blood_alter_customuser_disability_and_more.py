# Generated by Django 4.1 on 2022-08-30 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_customuser_blood_alter_customuser_city_village_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blood',
            field=models.CharField(blank=True, choices=[('4-', 'AB(IV) Rh-'), ('3-', 'B(III) Rh- '), ('3+', 'B(III) Rh+ '), ('1+', 'O(I) Rh+ '), ('1-', 'O(I) Rh- '), ('2-', 'A(II) Rh- '), ('2+', 'A(II) Rh+ '), ('4+', 'AB(IV) Rh+')], max_length=2, verbose_name='Группа крови'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='disability',
            field=models.CharField(blank=True, choices=[('2', 'Вторая'), ('1', 'Первая'), ('3', 'Третья')], max_length=1, verbose_name='Инвалидность'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('m', 'Мужчина'), ('f', 'Женщина')], default='f', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.CharField(choices=[('a', 'Админ'), ('d', 'Доктор'), ('p', 'Пациент')], max_length=1, verbose_name='Группа'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='insurance',
            field=models.CharField(blank=True, choices=[('3', 'ООО «Страховая медицинская компания РЕСО-МЕД» (Московский филиал)'), ('1', 'АО «Медицинская акционерная страховая компания» (АО «МАКС-М»)'), ('4', 'АО «Страховая компания «СОГАЗ-Мед»»'), ('6', 'ООО «КАПИТАЛ МС» '), ('5', 'ООО «Страховая компания «Ингосстрах-М»'), ('2', 'ООО «МСК «МЕДСТРАХ»»')], max_length=1, verbose_name='Сраховая компания'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='social_status',
            field=models.CharField(blank=True, choices=[('m', 'Средний'), ('h', 'Высший'), ('l', 'Низший')], max_length=1, verbose_name='Соц. Статус'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='territory',
            field=models.CharField(choices=[('Базарносызганский', 'Базарносызганский район'), ('Кузоватовский', 'Кузоватовский район'), ('Новомалыклинский', 'Новомалыклинский район'), ('Барышский', 'Барышский район'), ('Новоспасский', 'Новоспасский район'), ('Радищевский', 'Радищевский район'), ('Сурский', 'Сурский район'), ('Тереньгульский', 'Тереньгульский район'), ('Старомайнский', 'Старомайнский район'), ('Ульяновский', 'Ульяновский район'), ('Вешкаймский', 'Вешкаймский район'), ('Карсунский', 'Карсунский район'), ('Николаевский', 'Николаевский район'), ('Павловский', 'Павловский район'), ('Майнский', 'Майнский район'), ('Инзенский', 'Инзенский район'), ('Цильнинский', 'Цильнинский район'), ('Чердаклинский', 'Чердаклинский район '), ('Сенгилеевский', 'Сенгилеевский район'), ('Мелекесский', 'Мелекесский район'), ('Старокулаткинский', 'Старокулаткинский район')], max_length=25, verbose_name='Территория'),
        ),
    ]