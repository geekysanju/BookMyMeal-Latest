from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import models

curl=settings.CURRENT_URL


# Create your views here.
def adminhome(request):
	return render(request,'adminhome.html',{'curl':curl,'cunm':request.COOKIES.get('cunm')})

def addcat(request):
	if request.method=='GET':
		return render(request,'addcat.html',{'curl':curl,'output':'','cunm':request.COOKIES.get('cunm')})
	else:
		catnm=request.POST.get('catnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		query="insert into addcat values(NULL,'%s','%s')" %(catnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addcat.html',{'curl':curl,'output':'Category added successfully....','cunm':request.COOKIES.get('cunm')})



def addsubcat(request):
	query="select * from addcat"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()

	if request.method=='GET':
		return render(request,'addsubcat.html',{'curl':curl,'clist':clist,'output':'','cunm':request.COOKIES.get('cunm')})
	else:
		subcatnm=request.POST.get('subcatnm')
		catnm=request.POST.get('catnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		query1="insert into addsubcat values(NULL,'%s','%s','%s')" %(subcatnm,catnm,filename)
		models.cursor.execute(query1)
		models.db.commit()
		return render(request,'addsubcat.html',{'curl':curl,'output':'Sub Category added successfully....','clist':clist,'cunm':request.COOKIES.get('cunm')})

def addfoodproduct(request):
	query="select * from addsubcat"
	models.cursor.execute(query)
	sclist=models.cursor.fetchall()

	if request.method=='GET':
		return render(request,'addfoodproduct.html',{'curl':curl,'sclist':sclist,'output':'','cunm':request.COOKIES.get('cunm')})
	else:
		title=request.POST.get('title')
		subcatnm=request.POST.get('subcatnm')
		description=request.POST.get('description')
		price=request.POST.get('price')

		picon=request.FILES['picon']
		fs = FileSystemStorage()
		filename = fs.save(picon.name,picon)

		query1="insert into foodproduct values(NULL,'%s','%s','%s',%s,'%s')" %(title,subcatnm,description,price,filename)
		models.cursor.execute(query1)
		models.db.commit()

		return render(request,'addfoodproduct.html',{'curl':curl,'sclist':sclist,'output':'Food Product Added Successfully....','cunm':request.COOKIES.get('cunm')})

def paymentlistadmin(request):
	query="select * from payment"
	models.cursor.execute(query)
	payment_details=models.cursor.fetchall()
	return render(request,"paymentlistadmin.html",{'curl':curl,'payment_details':payment_details,'cunm':request.COOKIES.get('cunm')})

def changepasswordadmin(request):
	cunm=request.COOKIES.get('cunm')
	if request.method=="GET":
		return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':''})
	else:
		opass=request.POST.get('opass')
		npass=request.POST.get('npass')
		cnpass=request.POST.get('cnpass')
		query="select * from register where email='%s' and password='%s' " %(cunm,opass)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		if len(userDetails)>0:
			if npass==cnpass:
				query1="update register set password='%s' where email='%s'" %(npass,cunm)
				models.cursor.execute(query1)
				models.db.commit()
				return redirect(curl+'login/')
				return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm')})
			else:
				return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'New password and confirm new password not matched....'})
		else:
			return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'Old password not matched....'})
