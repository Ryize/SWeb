# Generated by Django 3.1.7 on 2021-05-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0013_auto_20210522_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Статус товара'),
        ),
    ]