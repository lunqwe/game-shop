from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, "about.html")

def sign_in(request):
    return render(request, 'sign-in.html')

def sign_up(request):
    return render(request, "sign-up.html")


def product_details(request):
    return render(request, 'product-detail.html')
