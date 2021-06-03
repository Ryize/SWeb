from django.core.paginator import Paginator


def get_paginator_list_page(request, all_obj, countObjOnePage: int):
    objPaginator_all_news = Paginator(all_obj, countObjOnePage)
    page_number = request.GET.get('page', 1)
    page_obj = objPaginator_all_news.get_page(page_number)
    return page_obj