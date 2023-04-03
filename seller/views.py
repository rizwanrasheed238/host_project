from django.shortcuts import render
from django.conf import settings
from itertools import product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from seller.models import seller_product
from antiqueapp.models import Category,product
from django.urls import reverse


# Create your views here.



def seller(request):
    products = seller_product.objects.filter(user_id=request.user)
    return render(request, "seller.html", {'products': products})

def addproduct(request):
    categories = Category.objects.all()
    if request.method == "POST":
        category_id = request.POST.get('cate')
        category = Category.objects.get(name=category_id)
        print(category,"***********************************************")
        pname = request.POST.get('pname')
        pdesc = request.POST.get('pdesc')
        pimg = request.POST.get('pimg')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        new_product =product(
            name=pname,
            descripton=pdesc,
            image=pimg,
            price=price,
            category=category,
            stock=stock,
        )
        new_product.save()
        return redirect('seller')

    return render(request, "addproduct.html", {'categories': categories})

def viewproduct(request):
    products = seller_product.objects.filter(user_id=request.user)

    return render(request, "seller.html", {'products': products})

def deleteproduct(request, id):

        item = seller_product.objects.get(id=id)
        item.delete()
        return redirect(reverse('seller'))


def logout(request):
    auth.logout(request)
    return redirect('/')