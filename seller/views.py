from django.shortcuts import render
from django.conf import settings
from itertools import product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from seller.models import seller_product
from antiqueapp.models import Category
from django.urls import reverse


# Create your views here.



def seller(request):
    products = seller_product.objects.filter(user_id=request.user)
    return render(request, "seller.html", {'products': products})

def addproduct(request):
    category = Category.objects.all()
    user = request.user.id
    if request.method == "POST":
        cate = request.POST.get('cate')
        pname = request.POST.get('pname')
        pdesc = request.POST.get('pdesc')
        pimg = request.POST.get('pimg')
        price = request.POST.get('price')
        # color = request.POST.get('color')
        # size = request.POST.get('size')
        stock = request.POST.get('stock')
        # is_active = request.POST.get('isactive')
        # in_stock = request.POST.get('instock')
        # user = request.user.id
        # val = Seller_product.objects.all()
        # user=request.user.id
        val = seller_product(
             user_id=user,category=cate, name=pname, descripton=pdesc, image=pimg, price=price, stock=stock
        )
        val.save()
        # add = seller_product.objects.filter()
        # print(cate,pname,pdesc,pimg,price,stock)
        return redirect('seller')

    return render(request, "addproduct.html",{'category':category})

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