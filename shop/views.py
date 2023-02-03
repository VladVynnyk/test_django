from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category
from .forms import UserForm, ProductForm
from django.contrib.auth.models import User


from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status

from .serializers import ProductSerializer, UserSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def products(request):
    products = Product.objects.values_list('name', flat=True).distinct()
    categories = Category.objects.values_list('name', flat=True).distinct()

    for product in products:
        print(product)

    return render(request, 'pages/products.html', {'products': products, 'categories': categories})


def filter_products(request, name):  # name - name of category
    # filtered_products = Product.objects.filter(Product.category == Category)

    # category = Category.objects.all()
    products = Product.objects.filter(category__name=name)
    categories = Category.objects.values_list('name', flat=True).distinct()

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'pages/filtered_products.html', context)


def order(request):
    userForm = UserForm()
    productForm = ProductForm()
    return render(request, 'pages/order.html', {'userForm': userForm, 'productForm': productForm})


def order_products(request):
    userForm = UserForm()
    productForm = ProductForm()
    return render(request, 'pages/order.html', {'userForm': userForm, 'productForm': productForm})


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Create order': '/order/create',
    }
  
    return Response(api_urls)


@api_view(['POST'])
def add_order(request):
    order = dict(request.data)
    print(order)
    usr = order['order[user][username]'][0]
    print(order['order[user][username]'])

    order_user = User.objects.get(username = usr)
    print("User:  ", order_user.id)

    #In dictionary request.data field "user" = "JohnDoe", so we changing this value to id of this user
    order['order[product][user]'][0] = order_user.id

    order_product = {'name': order['order[product][name]'][0], 'category': order['order[product][category]'][0], 'user':order['order[product][user]'][0], 'price': order['order[product][price]'][0]}
    product = ProductSerializer(data=order_product)
    #user = UserSerializer(data=order)

    if product.is_valid():
        print("POST REQUEST")
        product.save()
        # user.save()
        # category.save()
        return Response(request.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    