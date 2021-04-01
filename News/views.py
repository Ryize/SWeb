from django.shortcuts import render
from .models import News, Category

def index_page(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'News': news,
        'categories': categories,
    }
    return render(request, 'News/index_page.html', context=context)

def display_category(request, category_id):
    news_category = News.objects.filter(category=category_id)
    categories = Category.objects.all()
    this_category = Category.objects.filter(pk=category_id)[0]

    print(this_category)

    context = {
        'News': news_category,
        'categories': categories,
        'this_category': this_category,
    }
    return render(request, 'News/display_category.html', context=context)