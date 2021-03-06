from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('products/', product, name="product"),
    path('customer/<str:pk>', customer, name="customer"),
]