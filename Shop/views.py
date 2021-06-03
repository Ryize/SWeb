import datetime
import operator
from functools import reduce

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

from .forms import ProductForm
from .models import Product, Category_Product, Basket
from .services import product_filter, send_email, get_paginator_list_page
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView


def index_page(request):
    context = {}

    categories = Category_Product.objects.all()
    products = None

    search_query = request.GET.get('search_query')
    manufactured_company = request.GET.get('manufactured_company')
    seller = request.GET.get('seller')
    del_product_id = request.GET.get('del_product')
    if del_product_id:
        username = request.user.get_username()
        try:
            product = Product.objects.get(pk=del_product_id)

            if product.getSeller == username:
                product.delete()
                messages.success(request, 'Товар успешно удалён!')
            else:
                messages.error(request, 'У вас нету прав для осуществления этого действия!')
        except:
            messages.error(request, 'У вас нету прав для осуществления этого действия!')

    if seller:
        if seller == request.user.get_username():
            products = Product.objects.filter(seller=seller)
            context['products'] = products
            context['categories'] = categories
            context['is_myself_product'] = True
            return render(request, 'Shop/index_page.html', context=context)

    if search_query:
        query_list = search_query.split()
        products = Product.objects.filter(
            reduce(operator.and_,
                   (Q(name__icontains=q) for q in query_list)) |
            reduce(operator.and_,
                   (Q(description__icontains=q) for q in query_list)) |
            reduce(operator.and_,
                   (Q(manufacturer_company__icontains=q) for q in query_list))
        )

    if manufactured_company:
        query_list = manufactured_company.split()
        products = Product.objects.filter(
            reduce(operator.and_,
                   (Q(manufacturer_company__icontains=q) for q in query_list))
        )

    if not products:
        products = Product.objects.all()

    products, context = product_filter(request, products)

    page_obj = get_paginator_list_page(request, products, 27)

    context['products'] = page_obj
    context['obj'] = page_obj
    context['categories'] = categories

    return render(request, 'Shop/index_page.html', context=context)


def category_product(request, category_id):
    this_category = Category_Product.objects.get(pk=category_id)
    products = Product.objects.filter(category=category_id).select_related('category')
    categories = Category_Product.objects.all()

    products, context = product_filter(request, products)

    context['products'] = products
    context['categories'] = categories
    context['this_category'] = this_category

    return render(request, 'Shop/category_product.html', context=context)


def product_page_shop(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(product)
    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'Shop/product_add.html', context=context)


def product_view(request, product_id):

    login = request.user.get_username()
    block_buy_product = False

    if login:
        try:
            basket = Basket.objects.get(purchased_product_id=product_id, login_buyer=login)
        except:
            basket = False
        if basket:
            block_buy_product = True

    if request.GET.get('productID') and login:
        productPK = request.GET.get('productID')
        productPK = int(productPK)
        product = Product.objects.get(pk=productPK)
        product_name = product.getName
        seller_email = product.getSellerEmail
        user = User.objects.get(username=login)
        send_email('Новый заказ!', 'Получен новый заказ...' ,'Вашим товаром: '+product_name+' заинтересовался: '+user.get_username()+'.\nЕго e-mail для связи: '+user.email, seller_email)
        basket_new = Basket(login_buyer=user, purchased_product_id=productPK)
        basket_new.save()
        messages.success(request, 'Мы сообщили продавцу. Ожидайте, вам напишет продавец на почту!')
        block_buy_product = True


    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'block_buy_product': block_buy_product
    }

    return render(request, 'Shop/product_view.html', context=context)

@cache_page(15)
def createProduct(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            product = form.save(commit=False)
            product.seller = request.user.get_username()
            product.save()
            return redirect(product)
        messages.error(request, 'Не верно заполнены поля!')
    form = ProductForm(initial={'seller': request.user.get_username()})
    context['form'] = form

    return render(request, 'Shop/createProduct.html', context=context)

def changeProduct(request):
    context = {}

    productID = request.GET.get('productID')

    if request.method == 'POST' and productID:
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if 'photo' in request.FILES:
                form.photo = request.FILES['photo']
            product = Product.objects.get(pk=productID)
            product.delete()
            product = form.save(commit=False)
            product.pk = productID
            product.save()
            return redirect(changeProduct)
        messages.error(request, 'Не верно заполнены поля!'+str(form))


    try:
        product = Product.objects.get(pk=productID)
        category_products = Category_Product.objects.all()
        context['category_products'] = category_products
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'availability': product.availability,
            'price': product.price,
            'features': product.features,
            'category': product.category,
            'warranty': product.warranty,
            'manufacturer_company': product.manufacturer_company,
            'seller_email': product.seller_email,
            'seller': request.user.get_username(),
            'photo': product.name,
        })
        context['form'] = form
    except:
        messages.error(request, 'Товар не найден!')
        return redirect(index_page)

    return render(request, 'Shop/changeProduct.html', context=context)

def purchases(request):
    login = request.user.get_username()

    elementIds = request.GET.get('id')

    if elementIds:
        elementId = request.GET.get('id')
        Basket.objects.filter(purchased_product_id=elementId).delete()
        messages.success(request, 'Вы уcпешно удалили этот товар!')

    user_purchases = Basket.objects.filter(login_buyer=login).values('purchased_product_id')
    products = Product.objects.filter(pk__in=user_purchases.all())

    if user_purchases:
        context = {
            'products': products,
        }
        return render(request, 'Shop/user_purchases.html', context=context)
    return render(request, 'Shop/user_purchases.html')

@cache_page(3600*12)
def aboutus(request):
    return render(request, 'Shop/aboutus.html')

@cache_page(3600*12)
def deliveryinfo(request):
    return render(request, 'Shop/deliveryinfo.html')

def privacy(request):
    return render(request, 'Shop/privacypolicy.html')

@cache_page(3600*12)
def contacts(request):
    return render(request, 'Shop/contacts.html')

@cache_page(3600*12)
def refund(request):
    return render(request, 'Shop/refund.html')

@cache_page(3600*12)
def faq(request):
    return render(request, 'Shop/faq.html')

@cache_page(1)
def docapi(request):
    return render(request, 'Shop/docapi.html')

@cache_page(60)
def brands(request):
    manufactured_company = Product.objects.order_by().values('manufacturer_company').distinct()
    context = {
        'manufactured_company': manufactured_company,
    }
    return render(request, 'Shop/brands.html', context=context)