# Generated by Django 3.1.7 on 2021-04-17 08:02

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_auto_20210412_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент'),
        ),
    ]