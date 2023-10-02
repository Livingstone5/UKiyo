from django.shortcuts import render,redirect
from django.http import HttpResponse
from UKiyoapp.models import Applicant,Company,TravelAgency,Packages,Hotel,Restaurant,Review,Cart,Menu
from .models import Bookings
from django.template import loader




def book(request):
    return render(request,'bookings_user.html')


def bookings(request,id):
    flag=0
    books=Packages.objects.get(id=id)
    bid=books.id
    
    mydata= Packages.objects.get(id=bid)
    applicant=Applicant.objects.get(username=request.user)
    applicant_id=applicant.id
    data=Bookings.objects.all()
    for i in data:
        if i.packages_id==bid and i.applicant_id==applicant_id:
            flag=1
    if flag==0:
        bookobj=Bookings.objects.create(applicant=applicant,packages=books,username=applicant.username,name=books.name,image=books.image,title=books.title,price=books.price)
        bookobj.save()
        bookings=Bookings.objects.filter(username=applicant.username)
        template = loader.get_template('bookings_user.html')
        context = {
        'bookings':bookings,
        }
        return HttpResponse(template.render(context,request))
    else:
        bookings=Bookings.objects.filter(username=applicant.username)
        template = loader.get_template('bookings_user.html')
        
        context = {
        'bookings':bookings,'msg':"Already exists"
        }
        return HttpResponse(template.render(context,request))
        
    


def books(request):
    
    company=Company.objects.get(username=request.user)
    company_id=company.id
    pacs=Packages.objects.filter(company_id=company_id)
    for i in pacs:
        bookings=Bookings.objects.filter(packages_id=i.id)
    return render(request,'bookings_com.html',{'bookobjs':bookings})


def viewbookings(request):
    applicant=request.user
    bookings=Bookings.objects.filter(username=applicant)

    return render(request,'viewbookings.html',{'bookings':bookings})