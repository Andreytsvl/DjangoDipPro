# Generated by Django 5.0.7 on 2024-07-23 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Price_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Ценовая категория')),
            ],
            options={
                'verbose_name': 'Ценовая категория',
                'verbose_name_plural': 'Ценовые категории',
            },
        ),
        migrations.CreateModel(
            name='Recipe_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Рецептурный статус')),
            ],
            options={
                'verbose_name': 'Рецептурный статус',
                'verbose_name_plural': 'Рецептурные статусы',
            },
        ),
        migrations.CreateModel(
            name='Storage_conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Условия хранения')),
            ],
            options={
                'verbose_name': 'Условия хранения',
                'verbose_name_plural': 'Условия хранения',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название и дозировка')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Инструкция')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products_images', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена базовая')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Скидка в %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products_app.categories', verbose_name='Группа')),
                ('price_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products_app.price_category', verbose_name='Ценовая категория')),
                ('recipe_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products_app.recipe_status', verbose_name='Рецептурный статус')),
                ('storage_conditions', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products_app.storage_conditions', verbose_name='Условия хранения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'db_table': 'product',
            },
        ),
    ]
