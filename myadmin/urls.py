from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome),
    path('addcat/', views.addcat),
    path('addsubcat/', views.addsubcat),
    path('addfoodproduct/', views.addfoodproduct),
    path('paymentlistadmin/', views.paymentlistadmin),
    path('changepasswordadmin/', views.changepasswordadmin)
]
