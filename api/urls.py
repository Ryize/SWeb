from django.urls import path

from api.views import ProductListView, ProductDetailView, ProductCreateView, NewsListView, NewsDetailView

urlpatterns = [
    path('product/', ProductListView.as_view()),
    path('product/<int:pk>', ProductDetailView.as_view()),
    path('productCreate/', ProductCreateView.as_view()),
    path('news/', NewsListView.as_view()),
    path('news/<int:pk>', NewsDetailView.as_view()),
]
