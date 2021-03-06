from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered': delivered, 'pending':pending}
    return render(request, "accounts/home.html", context)

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, "accounts/product.html", context)

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer':customer,'orders':orders, 'order_count':order_count}
    return render(request, "accounts/customer.html", context)