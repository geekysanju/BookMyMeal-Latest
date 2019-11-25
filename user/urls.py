from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome),
    path('buyproduct/', views.buyproduct),
    path('orderlistuser/', views.orderlistuser)
]
