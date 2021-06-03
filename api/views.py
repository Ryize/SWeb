from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from News.models import News
from Shop.models import Product
from api.serializers import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer, NewsListSerializer, \
    NewsDetailSerializer


class ProductListView(APIView):

    def get(self, request):
        product = Product.objects.all()
        serializer = ProductListSerializer(product, many=True)
        return serializer.data

class ProductDetailView(APIView):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(product)
        return serializer.data

class ProductCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product = ProductCreateSerializer(data=request.data)
        if product.is_valid():
            product.save()
        return Response(201)


class NewsListView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)

class NewsDetailView(APIView):

    def get(self, request, pk):
        news = News.objects.get(pk=pk)
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data)