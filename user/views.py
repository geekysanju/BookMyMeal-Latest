from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from . import  models

curl=settings.CURRENT_URL


# Create your views here.
def userhome(request):
	return render(request,"userhome.html",{'curl':curl,'cunm':request.COOKIES.get('cunm')})
	
	
def buyproduct(request):
	pid=request.GET.get('pid')
	price=request.GET.get('price')
	PAYPAL_URL="https://www.sandbox.paypal.com/cgi-bin/webscr"
	PAYPAL_ID="husain.hm78653-myseller@gmail.com"
	return render(request,"buyproduct.html",{'curl':curl,'cunm':request.COOKIES.get('cunm'),'pid':pid,'price':price,'PAYPAL_URL':PAYPAL_URL,'PAYPAL_ID':PAYPAL_ID})	
	
	
def orderlistuser(request):
	cunm=request.COOKIES.get('cunm')
	query="select * from payment where uid='%s' " %(cunm)
	models.cursor.execute(query)
	payment_details=models.cursor.fetchall()
	return render(request,"orderlistuser.html",{'curl':curl,'payment_details':payment_details,'cunm':request.COOKIES.get('cunm')})
	
	
	
		
	
