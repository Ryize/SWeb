from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def product_filter(request, products):
    '''
    A function that filters products by fields using the filter function. Returns context (Dictionary) and products (QuerySet).
    '''
    context = {}
    availability = request.GET.get('availability')
    priceFrom = request.GET.get('priceFrom')
    priceBefore = request.GET.get('priceBefore')
    manufactured_company = request.GET.get('manufactured_company')
    seller = request.GET.get('seller')

    if availability:
        if manufactured_company != '':
            products = products.filter(manufacturer_company__icontains=manufactured_company)
            context['manufactured_company'] = manufactured_company
        if priceFrom != '':
            try:
                priceFrom = int(priceFrom)
            except:
                pass
            if isinstance(priceFrom, int):
                products = products.filter(price__gte=priceFrom)
                context['priceFrom'] = priceFrom

        if priceBefore != '':
            try:
                priceBefore = int(priceBefore)
            except:
                pass
            if isinstance(priceBefore, int):
                products = products.filter(price__lte=priceBefore)
                context['priceBefore'] = priceBefore

        if seller != '':
            products = products.filter(seller__iexact=seller)
            context['seller'] = seller

        if availability != '':
            if availability == 'available':
                products = products.filter(availability__iexact=1)
                context['availability'] = availability
            elif availability == 'noAvailable':
                products = products.filter(availability__iexact=0)
                context['availability'] = availability
    return products, context


def send_email(header, description, text, mail_href):
    html_message = render_to_string('Shop/mail_template.html', {'header': header, 'description': description, 'text': text})
    plain_message = strip_tags(html_message)
    send_mail(header, plain_message, 'site-hunter.ru@yandex.ru' ,[mail_href], fail_silently=False, html_message=html_message)

def get_paginator_list_page(request, all_obj, countObjOnePage: int):
    objPaginator_all_news = Paginator(all_obj, countObjOnePage)
    page_number = request.GET.get('page', 1)
    page_obj = objPaginator_all_news.get_page(page_number)
    return page_obj