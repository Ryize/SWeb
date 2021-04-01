from django.db import models


class News(models.Model):
    author_news = models.CharField(max_length=33, verbose_name='Автор новости')
    title = models.CharField(max_length=64, verbose_name='Название', null=True)
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to='image_news/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    is_publiced = models.BooleanField(default=True, verbose_name='Доступна')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.author_news

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Все новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']