from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('vendors/',view=all_data),
    path('',view=create_vendor),
    path('<str:v_id>/',view=specific_vendor),
    path('put/<str:vendor_id>/',view=put_vendor,name="put_vendor"),
    # path(),

]