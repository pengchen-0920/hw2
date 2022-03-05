from django.shortcuts import render
from .models import Order

def order_detail(request, orderId):
    order = Order.objects.get(orderId=orderId)
    return render(request, 'order/order_detail.html', {'order': order})
