from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/category/<str:name>/',
         views.filter_products, name="filtered products"),

    path('products/order/', views.order, name="order"),  #form for creating order
    path('products/orderProducts/', views.order_products, name="order_products"), #form without request

    path('api/', views.ApiOverview, name='api'),
    path('api/order/create', views.add_order, name='order_create'), #endpoint for creating order
]
