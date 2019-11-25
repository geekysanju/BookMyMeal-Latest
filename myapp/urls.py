from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('viewsubcat/', views.viewsubcat),
    path('viewfoodproducts/', views.viewfoodproducts),
    path('orderlogin/', views.orderlogin),
    path('payment/', views.payment),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('about/', views.about),
    path('contact/', views.contact),
    path('register/', views.register),
    path('verify/', views.verify),
    path('service/', views.service),
    path('login/', views.login),
    path('user/', include('user.urls')),
    path('myadmin/', include('myadmin.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
