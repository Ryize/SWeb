# Generated by Django 3.1.7 on 2021-04-19 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_auto_20210419_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='features',
        ),
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.CharField(blank=True, default='Нету', max_length=48, verbose_name='Особенности товара'),
        ),
        migrations.DeleteModel(
            name='Feature_Product',
        ),
    ]
