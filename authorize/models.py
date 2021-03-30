from django.db import models


class User(models.Model):
    login = models.CharField(max_length=32, verbose_name='Логин')
    email = models.EmailField(max_length=254, verbose_name='Почта')
    password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создание профиля')
    avatar = models.ImageField(upload_to='user_avatar/%Y/%m/%d/', blank=True)
    is_publiced = models.BooleanField(default=True, verbose_name='Тип профиля')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Все пользователи'
        ordering = ['-created_at']
