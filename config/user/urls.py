from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact),
    path('catalog/', products),
    path('catalog/<str:product_type>/', type_products),
    path('about/', about, name='about'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up),
    path('product/<int:product_id>', product_details),
    path('cart/', cart, name='cart'),
    path('database_placeholder/', database_placeholder, name='db_placeholder')
]
