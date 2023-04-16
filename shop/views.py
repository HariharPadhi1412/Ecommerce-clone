from django.shortcuts import render
from . models import Product
from math import ceil

# Create your views here.

def index(request):
   
    all_products = []
    product_category = Product.objects.values('category','id')
    product_category_set = {item['category'] for item in product_category}

    for categorys in product_category_set:
        products = Product.objects.filter(category = categorys)
        product_length = len(products)

        no_of_slides = product_length// 4 + ceil((product_length / 4) - (product_length // 4))
        all_products.append([products,range(1,no_of_slides),no_of_slides])

    new_params = {"all_products": all_products}

    return render(request,'shop/index.html',new_params)


def about(request):
    return render(request,"shop/about.html")

def checkout(request):
    return render(request,"shop/checkout.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def contact(request):
    return render(request,"shop/contact.html")

def prodView(request):
    return render(request,"shop/prodView.html")
