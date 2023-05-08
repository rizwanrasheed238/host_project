from django.shortcuts import render
from django.conf import settings
from itertools import product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from seller.models import seller_product
from antiqueapp.models import Category,product
from cart.models import OrderPlaced
from django.urls import reverse
from django.utils.text import slugify

# Create your views here.



def seller(request):
    user=request.user
    products = product.objects.filter(user_id=user.id)
    return render(request, "seller.html", {'products': products})

def addproduct(request):
    user=request.user
    categories = Category.objects.all()
    if request.method == "POST":
        category_id = request.POST.get('cate')
        category = Category.objects.get(id=category_id)
        print(category,"***********************************************")
        pname = request.POST.get('pname')
        pdesc = request.POST.get('pdesc')
        pimg = request.POST.get('pimg')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        new_product =product(
            user=user,
            name=pname,
            descripton=pdesc,
            slug=slugify(pname),
            availabe=True,
            image=pimg,
            price=price,
            category=category,
            stock=stock,
        )
        new_product.save()
        return redirect('seller')

    return render(request, "addproduct.html", {'categories': categories})

def viewproduct(request):
    user=request.user
    products = product.objects.filter(user_id=user.id)

    return render(request, "seller.html", {'products': products})

def vieworders(request):
    user=request.user
    order=OrderPlaced.objects.filter(user_id=user.id)
    print(order,'222222222222222222222222222222222222')
    for i in order:
        orderdate=i.ordered_date
        print(orderdate)


    return render(request,"vieworders.html")

# def deleteproduct(request, id):

#         item = seller_product.objects.get(id=id)
#         item.delete()
#         return redirect(reverse('seller'))


def logout(request):
    auth.logout(request)
    return redirect('/')