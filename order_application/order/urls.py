from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('<orderId>', views.order_detail, name='detail'),
]
