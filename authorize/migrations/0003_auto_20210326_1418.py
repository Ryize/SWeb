# Generated by Django 3.1.7 on 2021-03-26 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorize', '0002_auto_20210324_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-created_at'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Все пользователи'},
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='user_avatar/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Создание профиля'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_publiced',
            field=models.BooleanField(default=True, verbose_name='Тип профиля'),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=32, verbose_name='Логин'),
        ),
    ]
