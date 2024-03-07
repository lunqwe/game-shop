from django.urls import include, path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact),
    path('products/', products),
    path('about/', about, name='about'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up),
    path('product-details/', product_details)
]
