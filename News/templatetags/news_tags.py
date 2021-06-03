from django import template

from News.models import Category, News

register = template.Library()

@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()
