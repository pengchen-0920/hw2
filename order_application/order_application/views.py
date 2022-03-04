from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order

def first_page(request):
    return render(request, 'first_page.html')

def second_page(request):

    if request.method == "POST":
        searched = request.POST['searched']
        orders = Order.objects.filter(customer__contains=searched)
        return render(request, 'second_page.html', {'orders': orders, 'searched': searched})
    else:
        return render(request, 'first_page.html')

    # the third argument can be sent from view to template
