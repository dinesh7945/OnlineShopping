from django.http import HttpResponse
from django.shortcuts import render
from .models import product
from onlineshopping.models import product

def index(request): 
    products = product.objects.all()
    print(products)
    params = {'product':products}  
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def tracker(request):
    return HttpResponse(" we are at tracker")

def search(request):
    return HttpResponse(" we are at search")

def orders(request):
    return render(request,'shop/orders.html')

def checkout(request):
    return HttpResponse(" we are at checkout")

def login(request):
    return render(request,'shop/login.html')
    
def register(request):
    return render(request,'shop/register.html')

def productview(request, myid): 
    product = product.objects.filter(id=id)
    print(product)
    return render(request,'shop/productview.html')
    
