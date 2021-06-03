from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse_lazy


class Product(models.Model):
    name = models.CharField(max_length=48, verbose_name='Название товара')
    description = RichTextUploadingField(verbose_name='Описание товара')
    availability = models.BooleanField(default=True, verbose_name='Наличие товара')
    price = models.FloatField(verbose_name='Цена')
    features = models.CharField(max_length=48, verbose_name='Особенности товара', default='Нету', blank=True)
    category = models.ForeignKey('Category_Product', on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
    warranty = models.IntegerField(blank=True, verbose_name='Гарантия(В месяцах)', null=True)
    manufacturer_company = models.CharField(max_length=48, blank=True, verbose_name='Компания производитель')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания товара', blank=True)
    seller = models.CharField(max_length=48, verbose_name='Продавец')
    seller_email = models.CharField(max_length=48, verbose_name='E-Mail для связи покупателей с вами')
    photo = models.ImageField(verbose_name='Выберите аватарку товара', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('product_view', kwargs={'product_id': self.pk})

    @property
    def getName(self):
        return self.name

    @property
    def getSeller(self):
        return self.seller

    @property
    def getSellerEmail(self):
        return self.seller_email

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Все товары'
        ordering = ['-created_at']

class Basket(models.Model):
    login_buyer = models.CharField(max_length=48, blank=True, verbose_name='Логин покупателя')
    purchased_product_id = models.CharField(max_length=48, blank=True, verbose_name='id товара')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['-purchased_product_id']


class Category_Product(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категории')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('category_product', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['-title']
