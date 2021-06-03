from django.urls import path
from .views import index_page, display_category, view_news, addnews

urlpatterns = [
    path('', index_page, name='home'),
    path('category/<int:category_id>/', display_category, name='category'),
    path('news/<int:news_id>/', view_news, name='news'),
    path('addnews/', addnews, name='addnews'),
]