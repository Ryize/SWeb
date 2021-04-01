from django.urls import path
from .views import index_page, display_category

urlpatterns = [
    path('', index_page, name='home'),
    path('category/<int:category_id>/', display_category, name='category'),
]