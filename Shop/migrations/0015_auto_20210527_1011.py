# Generated by Django 3.1.7 on 2021-05-27 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_basket_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='status',
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Выберите аватарку товара'),
        ),
    ]
