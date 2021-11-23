from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders
from math import ceil
# Create your views here.
def index(request):
    # products=Product.objects.all()
    # print(products)
    # n=len(products)
    # nSlides=(n//4)+ceil((n/4)-(n//4))

    allProds=[]
    catprods=Product.objects.values('catogery','id')
    cats={item['catogery'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(catogery=cat)
        n=len(prod)
        nSlides=(n//4)+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])

    # params={'no_of_slides':nSlides,'range':range(1,nSlides),'Product':products}
    # allProds=[[products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

    return render(request,"shop/contact.html")

def tracker(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def prodectView(request,myid):
    # fetch the product using id
    product=Product.objects.filter(id=myid) 
     
    return render(request,"shop/prodview.html",{'product':product[0]})

def checkout(request):
    if request.method=="POST":
        print(request)
        items_Json=request.POST.get('items_json','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address1','')+" "+request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip','')
        phone=request.POST.get('phone','')
        
        order=Orders(items_Json=items_Json,name=name,email=email,phone=phone,city=city,state=state,address=address,zip_code=zip_code,)
        order.save()
        thank=True
        id=order.order_id
        return render(request,"shop/checkout.html",{'thank':thank,'id':id})
    return render(request,"shop/checkout.html")
