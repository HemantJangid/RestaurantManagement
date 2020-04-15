from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.http import HttpResponse
from django.contrib import messages
from .models import Outlet, Dish
import json


# Create your views here.

def login(request):
    if request.user.username == '':
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('outlets')
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login')
        else:
            return render(request, 'login.html')
    else:
        return redirect('outlets')


def outlets(request):
    current_user = request.user.username
    if current_user == '':
        messages.info(request, 'Please login first')
        return redirect('login')
    else:
        outlets = Outlet.objects.all().filter(owner_username=current_user)
        return render(request, 'outlets.html', {'outlets': outlets, 'page': 'outlets', 'current_user': current_user})


def dishes(request):
    current_user = request.user.username
    if current_user == '':
        messages.info(request, 'Please login first')
        return redirect('login')
    else:
        dishes = Dish.objects.all().filter(owner_username=current_user)
        categories = dishes.distinct('category').all()
        return render(request, 'dishes.html', {'dishes': dishes, 'page': 'dishes', 'categories': categories})


def addDish(request):
    if request.method == 'POST':
        owner_username = request.user.username
        dish_name = request.POST['dish_name']
        category = request.POST['category']
        dish_type = request.POST['dish_type']
        v_or_n = 'v' if dish_type == 'Veg' else 'n'
        price = request.POST['price']

        dish = Dish(owner_username=owner_username, dish_name=dish_name,
                    category=category, v_or_n=v_or_n, price=price)
        dish.save()
    return redirect('dishes')


def addOutlet(request):
    if request.method == 'POST':
        owner_username = request.user.username
        outlet_name = request.POST['outlet_name']
        address = request.POST['address']
        phone = request.POST['phone']

        outlet = Outlet(owner_username=owner_username,
                        name=outlet_name, address=address, phone=phone)
        outlet.save()
    return redirect('outlets')


def pos(request):
    current_user = request.user.username

    if current_user == '':
        messages.info(request, 'Please login first')
        return redirect('login')
    else:
        dishes = Dish.objects.all().filter(owner_username=current_user)
        categories = dishes.distinct('category').all()
        return render(request, 'pos.html', {'dishes': dishes, 'page': 'dishes', 'categories': categories})


def bill(request):
    print(request.method)
    if request.method == 'POST':
        qty = request.POST['qty']
        item = request.POST['item']
        price = request.POST['price']
        item_total = request.POST['item_total']

        details = {{'qty': qty, 'item': item, 'price': price, 'item_total': item_total}}

        # outlets = Outlet.objects.all().filter(owner_username=current_user)
        # name = outlets[0].name
        # address = outlets[0].address
        # phone = outlets[0].phone
        # bill_no = request.POST['bill_no']
    return render(request, 'bill.html', {'details': details})


def test(request):
    return render(request, 'test.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
