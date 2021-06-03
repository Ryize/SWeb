from django.urls import path
from .views import product_page_shop, product_view, index_page, category_product, aboutus, deliveryinfo, privacy, \
    contacts, refund, faq, brands, createProduct, changeProduct, purchases, docapi

urlpatterns = [
    path('', index_page, name='shop_page'),
    path('createProduct/', createProduct, name='createProduct'),
    path('category/<int:category_id>', category_product, name='category_product'),
    path('addProduct/', product_page_shop, name='product_page_shop'),
    path('product/<int:product_id>', product_view, name='product_view'),
    path('aboutus/', aboutus, name='aboutus'),
    path('deliveryinfo/', deliveryinfo, name='deliveryinfo'),
    path('privacy/', privacy, name='privacy'),
    path('contacts/', contacts, name='contacts'),
    path('refund/', refund, name='refund'),
    path('faq/', faq, name='faq'),
    path('brands/', brands, name='brands'),
    path('changeProduct/', changeProduct, name='changeProduct'),
    path('purchases/', purchases, name='purchases'),
    path('docapi/', docapi, name='docapi'),
]
