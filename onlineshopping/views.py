from django.http import HttpResponse
from django.shortcuts import render
from .models import product, Contact, Register
from onlineshopping.models import product, Contact, Register

def index(request): 
    products = product.objects.all()
    print(products)
    params = {'product':products}  
    return render(request,'shop/index.html',params)

def about(request):
    # demo
    # 41 
    return render(request,'shop/about.html')

def contact(request):
    if request.method == "POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        # Contact = contact(name='name',email='email',phone='phone',desc='desc')
        contact.save()
    return render(request,'shop/contact.html')

def tracker(request):
    return HttpResponse(" we are at tracker")

def search(request):
    return HttpResponse(" we are at search")

def orders(request):
    return render(request,'shop/orders.html')

def checkout(request):
    products = product.objects.all()
    print(products)
    params = {'product':products} 
    
    return render(request,'shop/checkout.html',params)

def login(request):
    return render(request,'shop/login.html')
    
def register(request):
    if request.method == 'POST':
        print(request)
        name = request.POST.get('name','')
        phone = request.POST.get('phone','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        print(name,email,phone,password)
        register = Register(name=name, email=email, phone=phone, password=password)
        # Contact = contact(name='name',email='email',phone='phone',desc='desc')
        register.save()
    return render(request,'shop/register.html')

def productview(request, myid): 
    # fetch th product using id
    # http://127.0.0.1:8000/onlineshopping/products/13
    
    products = product.objects.filter(id=myid)
    print(products)
    
    return render(request,'shop/productview.html',{'products':products[0]})

def productfetch(request):
    id=request.GET.get('id')
    print(id)
    products = product.objects.filter(id=id)
    return render(request,'shop/productfetch.html',{'products':products[0]})   
    
def demo(request):
    mydata= request.GET.get('myData')
    #params = {'product':products} 
    print(mydata)
    return render(request,'shop/demo.html',{'mydata':mydata})