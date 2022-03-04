from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):
    orders = Order.objects.all().order_by('orderId')
    # the third argument can be sent from view to template
    return render(request, 'second_page.html', {'orders': orders})
