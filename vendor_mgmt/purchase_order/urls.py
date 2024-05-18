from django.contrib import admin
from django.urls import path,include

from .views import create_order,all_orders

urlpatterns = [
    
    path("",view=create_order),
    path('orders/',view=all_orders),
]