from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from . import models
import time

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

def home(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()
	return render(request,'home.html',{'curl':curl,'media_url':media_url,'clist':clist})

def viewsubcat(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()

	cnm=request.GET.get('cnm')
	query="select * from addsubcat where catnm='%s' " %(cnm)
	models.cursor.execute(query)
	sclist=models.cursor.fetchall()
	return render(request,'viewsubcat.html',{'curl':curl,'media_url':media_url,'clist':clist,'sclist':sclist,'cnm':cnm})

def about(request):
	return render(request,'about.html',{'curl':curl})

def contact(request):
	return render(request,'contact.html',{'curl':curl})

def service(request):
	return render(request,'service.html',{'curl':curl})

def register(request):
	if request.method=="GET":
		return render(request,'register.html',{'curl':curl,'output':''})
	else:
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		city=request.POST.get('city')
		gender=request.POST.get('gender')
		dt=time.asctime(time.localtime(time.time()))

		query="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',0,'%s')" %(name,email,password,address,mobile,city,gender,dt)
		models.cursor.execute(query)
		models.db.commit()

		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText

		me = "phpbatch34@gmail.com"
		you = email

		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Verification Mail Book My Meal"
		msg['From'] = me
		msg['To'] = you

		html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to Book My Meal</h1>
    					<p>You have successfully registered , please click on the link below to verify your account</p>
    					<h2>Username : """+email+"""</h2>
    					<h2>Password : """+str(password)+"""</h2>
    					<br>
    					<a href='http://localhost:8000/verify?vemail="""+email+"""' >Click here to verify account</a>
  					</body>
				</html>
				"""

		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("phpbatch34@gmail.com", "123@@123")

		part2 = MIMEText(html, 'html')

		msg.attach(part2)

		s.sendmail(me,you, str(msg))
		s.quit()
		print("mail send successfully....")

		return render(request,'register.html',{'curl':curl,'output':'Registration successfully done....'})

def verify(request):
	vemail=request.GET.get('vemail')
	query="update register set status=1 where email='%s' " %(vemail)
	models.cursor.execute(query)
	models.db.commit()
	return redirect(curl+'login/')


def login(request):
	if request.method=="GET":
		return render(request,'login.html',{'curl':curl,'output':''})
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')

		query="select * from register where email='%s' and password='%s' and status=1" %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		if len(userDetails)>0:
			if userDetails[0][8]=='user':
				response=redirect(curl+'user/')
			else:
				response=redirect(curl+'myadmin/')
			response.set_cookie('cunm',email,3600)
			return response
		else:
			return render(request,'login.html',{'curl':curl,'output':'Login failed invalid user or verify your account'})


def orderlogin(request):
	if request.method=="GET":
		pid=request.GET.get('pid')
		price=request.GET.get('price')
		return render(request,'orderlogin.html',{'curl':curl,'output':'','pid':pid,'price':price})
	else:
		pid=request.POST.get('pid')
		price=request.POST.get('price')
		email=request.POST.get('email')
		password=request.POST.get('password')

		query="select * from register where email='%s' and password='%s' and status=1" %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		if len(userDetails)>0:
			if userDetails[0][8]=='user':
				response=redirect(curl+'user/buyproduct/?pid='+str(pid)+'&price='+str(price))
			response.set_cookie('cunm',email,3600)
			return response
		else:
			return redirect(curl)


def viewfoodproducts(request):
	query1="select * from addsubcat"
	models.cursor.execute(query1)
	sclist=models.cursor.fetchall()

	scnm=request.GET.get('scnm')
	sprice=request.GET.get('sprice')
	eprice=request.GET.get('eprice')

	if sprice==None:
		query="select * from foodproduct where subcatnm='%s' " %(scnm)
	else:
		query="select * from foodproduct where subcatnm='%s' and price between %s and %s" %(scnm,int(sprice),int(eprice))

	models.cursor.execute(query)
	plist=models.cursor.fetchall()

	return render(request,'viewfoodproducts.html',{'curl':curl,'media_url':media_url,'scnm':scnm,'total':len(plist),'plist':plist,'sclist':sclist})

def payment(request):
	pid=request.GET.get('pid')
	price=request.GET.get('price')
	uid=request.GET.get('uid')
	dt=time.asctime(time.localtime(time.time()))
	query="insert into payment values(NULL,%s,%s,'%s','%s')" %(int(pid),int(price),uid,dt)
	models.cursor.execute(query)
	models.db.commit()
	return redirect(curl+'success/')


def success(request):
	return render(request,'success.html',{'curl':curl})

def cancel(request):
	return render(request,'cancel.html',{'curl':curl})
