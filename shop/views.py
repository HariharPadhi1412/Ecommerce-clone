from django.shortcuts import render
from . models import Product
from math import ceil
# from django.http import HttpResponse

# Create your views here.

def index(request):
    products = Product.objects.all()
    product_length = len(products)

    no_of_slides = product_length// 4 + ceil((product_length / 4) - (product_length // 4))
    params = {'no of slides ' : no_of_slides,'range' : range(1,no_of_slides),'product':products}

    return render(request,'shop/index.html',params)


def about(request):
    return render(request,"shop/about.html")

def checkout(request):
    return render(request,"")

def tracker(request):
    return render(request,"")

def search(request):
    return render(request,"")

def contact(request):
    return render(request,"")

def prodView(request):
    return render(request,"")
