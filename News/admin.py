from django.contrib import admin
from News.models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author_news', 'content', 'created_at', 'category', 'is_publiced')
    list_display_links = ('id', 'title', 'author_news', 'content', 'created_at')
    search_fields = ('id', 'title', 'author_news', 'category')
    list_editable = ('category', 'is_publiced')
    list_filter = ('category', 'is_publiced')
    list_per_page = 32


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
