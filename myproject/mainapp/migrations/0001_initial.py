# Generated by Django 5.1.5 on 2025-01-24 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainDeskription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название города')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание города')),
                ('image_city', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка города')),
            ],
            options={
                'verbose_name': 'Главная карточка города',
                'verbose_name_plural': 'Главные карточки городов',
            },
        ),
        migrations.CreateModel(
            name='CatalogEkskursii',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_excursion', models.CharField(max_length=100, verbose_name='Название экскурсии')),
                ('price_excursion', models.IntegerField(verbose_name='Цена экскурсии')),
                ('image_excursion', models.ImageField(upload_to='image_excursion/', verbose_name='Картинка экскурсии')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main', to='mainapp.maindeskription', verbose_name='К какому городу относится')),
            ],
            options={
                'verbose_name': 'Экскурсия города',
                'verbose_name_plural': 'Экскурсии городов',
            },
        ),
        migrations.CreateModel(
            name='ModalText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_long', models.CharField(max_length=100, verbose_name='Сколько длится поездка')),
                ('name_place', models.TextField(max_length=5500, verbose_name='Название локаций и места на выбор с указанием времени')),
                ('time_to_departure', models.CharField(max_length=100, verbose_name='Во сколько выезд')),
                ('take_with_you', models.TextField(max_length=1500, verbose_name='Что взять с собой')),
                ('how_many_day_and_night', models.CharField(max_length=100, verbose_name='За сколько дней и ночей')),
                ('how_many_people', models.IntegerField(verbose_name='Стоимость за сколько человек')),
                ('price_russian', models.IntegerField(verbose_name='Цена за русскую поездку')),
                ('price_english', models.IntegerField(verbose_name='Цена за английскую поездку')),
                ('what_is_not_included_in_price', models.CharField(max_length=200, verbose_name='Что не входит в стоимость')),
                ('modal_ekskurs_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modal_texts', to='mainapp.catalogekskursii', verbose_name='К какой экскурсии отосится')),
            ],
            options={
                'verbose_name': 'Модальные окна',
                'verbose_name_plural': 'Модальное окно',
            },
        ),
    ]
