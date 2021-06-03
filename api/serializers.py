from rest_framework import serializers

from News.models import News
from Shop.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['photo']


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = Product
        exclude = ['photo']

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('__all__')


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ['photo']


class NewsDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    class Meta:
        model = News
        exclude = ['photo']