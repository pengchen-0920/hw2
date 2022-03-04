from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order

def homepage(request):
    return HttpResponse('homepage')
    # orders = Order.objects.all().order_by('orderID')
    # return render(request, 'orders/order_list.html')
