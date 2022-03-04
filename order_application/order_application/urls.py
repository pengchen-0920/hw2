from django.contrib import admin
from django.urls import path, include
from.import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_page),
    # path('order/', include('order.urls')),
    path('order/', views.second_page, name='second_page'),
]
