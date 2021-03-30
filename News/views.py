from django.shortcuts import render
from .models import News

def index_page(request):
    news = News.objects.all()
    return render(request, 'News/index_page.html', {'News': news})