from django.shortcuts import render
from .services import DatabasePlaceholder
from .models import Product

# Create your views here.
def index(request):
    constructors = Product.objects.filter(display_type='table_game').only('title', 'price', 'image')[:3]
    table_games = Product.objects.filter(display_type='table_game').only('title', 'price', 'image')[:3]

    context = {'constructors': constructors,
                'table_games': table_games}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')

def products(request):
    constructors = Product.objects.filter(display_type='constructors').only('title', 'price', 'image')[:3]
    table_games = Product.objects.filter(display_type='table_game').only('title', 'price', 'image')[:3]

    context = {'constructors': constructors,
                'table_games': table_games}
    return render(request, 'catalog_outside.html', context)

def type_products(request, product_type):
    print(product_type)
    return render(request, "catalog_inside.html")


def about(request):
    return render(request, "about.html")

def sign_in(request):
    return render(request, 'sign-in.html')

def sign_up(request):
    return render(request, "sign-up.html")

def cart(request):
    return render(request, 'cart.html')


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product-detail.html', context)

def database_placeholder(request):
    data = DatabasePlaceholder.get_data('D:\\.prog\\Django-e-commerce\\config\\user\\data.xlsx')
    DatabasePlaceholder.save_data(data)
    return render(request, '123.html')