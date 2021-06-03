from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page

from .forms import NewsForm
from .models import News, Category
from .services import get_paginator_list_page


@cache_page(5)
def index_page(request):
    this_category = 'Все категории'
    all_news = News.objects.all().select_related('category')
    page_obj = get_paginator_list_page(request, all_news, 27)
    context = {
        'this_category': this_category,
        'News': page_obj,
        'obj': page_obj,
    }
    #send_mail(
    #    'Subject here',
    #    'Here is the message.',
    #    'site-hunter.ru@yandex.ru',
    #    ['chekashovmatvey@gmail.com'],
    #    fail_silently=False,
    #)
    return render(request, 'News/index_page.html', context=context)

def display_category(request, category_id):
    news_category = News.objects.filter(category=category_id).select_related('category')
    this_category = Category.objects.filter(pk=category_id)[0]

    page_obj = get_paginator_list_page(request, news_category, 27)

    context = {
        'News': page_obj,
        'obj': page_obj,
        'this_category': this_category,
    }
    return render(request, 'News/display_category.html', context=context)

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'News/view_news.html', context=context)

@login_required
def addnews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:

                form.photo = request.FILES['photo']
            news = form.save()
            news.author_news = request.user.get_username()
            news.save()
            return redirect(news)
    else:
        form = NewsForm()
    context = {
        'form': form,
    }
    return render(request, 'News/addnews.html', context=context)