import re
from django.core import paginator
from django.shortcuts import render
from .models import *
import json
from django.core.paginator import Page, Paginator
import random
from .utils import *
# Create your views here.
def add_product(request):
    if 'POST' in request.method:
        product.objects.create(
            name=request.POST['productname'],
            price=request.POST['price'],
            qty=request.POST['qty'],
            amount=request.POST['totalamount'],
            description=request.POST['description']
        )
        msg = "Product added"
        return render(request,'add_product.html',{'msg':msg})
    else:
        return render(request,'add_product.html')
def search(request):
    if request.method=="POST":
        search_string=request.POST['search']
        search_result=product.objects.filter(name__icontains=search_string)
        return render(request,'search.html',{'result':search_result})
    else:
        product_list=product.objects.all()
        p=Paginator(product_list,2)
        page=request.GET.get('page')
        products=p.get_page(page)
        return render(request,'search.html',{'product':products})
def forgotpassword(request):
    if request.method=="POST":
        email=request.POST['email']
        user_id=User.objects.filter(email=email)
        if user_id:
            user_id=User.objects.get(email=email)
            otp=random.randint(111111,999999)
            user_id.otp=otp
            user_id.save()
            sendmail("OTP","mail",email,{'otp':otp})
            return render(request,'new_password.html',{'email':email})
        else:
            msg="Email does not exist"
            return render(request,'forgot_password.html')

    else:
        return render(request,'forgot_password.html')
def newpassword(request):
    if request.method=="POST":
        email=request.POST['email']
        otp=request.POST['otp']
        password=request.POST['password']
        c_password=request.POST['confirmpassword']
        user_id=User.objects.get(email=email)
        if user_id.otp==int(otp):
            if password==c_password:
                user_id.password=password
                user_id.save()
                return render(request,'search.html')
            else:
                msg="New passwod and confirm password must be same"
                return render(request,'new_password.html',{'msg':msg})
        else:
            msg="Incorrect OTP"
            return render(request,'new_password.html',{'msg':msg})
    else:
        return render(request,'new_password.html')
def uploadpic(request):
    if 'POST' in request.method:
        pic=request.FILES['picture']
        print("-------->",pic)
        images.objects.create(image_url=pic)
        image=images.objects.all()
        return render(request,'search.html',{'image':image})
    else:
        return render(request,'search.html')