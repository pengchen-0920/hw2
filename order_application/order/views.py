from django.shortcuts import render
from .models import Order

def order_detail(request):
    return render(request, 'order/order_detail.html')
