from django.contrib import admin

from .models import Product, Category_Product, Basket


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'availability', 'price', 'category', 'warranty', 'manufacturer_company', 'seller')
    list_display_links = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'category', 'features')
    list_filter = ('category', 'price', 'availability')
    list_per_page = 32


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    list_per_page = 32

class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'login_buyer', 'purchased_product_id')
    list_display_links = ('id', 'login_buyer', 'purchased_product_id')
    search_fields = ('id', 'login_buyer', 'purchased_product_id')
    list_per_page = 32


admin.site.register(Product, ProductAdmin)
admin.site.register(Category_Product, CategoryAdmin)
admin.site.register(Basket, BasketAdmin)
