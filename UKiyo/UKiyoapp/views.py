from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Applicant,Company,TravelAgency,Packages,Hotel,Restaurant,Review,Cart,Menu

from django.template import loader
from django.db.models import Q
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest



def firstpg(request):
    data=TravelAgency.objects.all()
    hotels=Hotel.objects.all()
    rsts=Restaurant.objects.all()
    pacs=Packages.objects.all()
    rvws=Review.objects.all()
    return render (request,"firstpg.html",{'data':data,'hotels':hotels,'rsts':rsts,'pacs':pacs,'rvws':rvws})
    

# @login_required
# def index(request):
#     return render(request,'index.html')

@login_required
def home(request):
    data=TravelAgency.objects.all()
    hotels=Hotel.objects.all()
    rsts=Restaurant.objects.all()
    pacs=Packages.objects.all()
    rvws=Review.objects.all()
    applicant=Applicant.objects.get(username=request.user)
    return render (request,"home.html",{'data':data,'hotels':hotels,'rsts':rsts,'pacs':pacs,'applicant':applicant,'rvws':rvws})

@login_required
def signup(request):

    if request.method=='POST':
        Username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']

        myuser=User.objects.create_user(username=Username,email=email,password=pass1)
        myuser.save()
        my_group = Group.objects.get(name='applicant') 
        my_group.user_set.add(myuser)
        applicant=Applicant(username=myuser,email=email,password=pass1)
        applicant.save()

        messages.success(request,'Your account successfully created.')

        return render(request,"home.html")

    return render(request,'signin.html')

@login_required
def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            userGroup = Group.objects.filter(user=request.user)
            for i in userGroup:
                if i.name=='applicant':
                    return redirect('home')
                elif i.name=='company':
                    return redirect('indexpage')
                else:

                    return render(request,'signin.html')

        else:
            messages.error(request,"bad credentials")
            return redirect('index')
    else:
        return render(request,'signin.html')

@login_required
def resethome(request):
    return render(request,'resetpassword.html')

@login_required
def resetpassword(request):
    responseDic={}
    try:
        name=request.POST['name1']
        newpwd=request.POST['password']
        user=User.objects.get(username=name)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            responseDic["errmsg"]="Password Reset Successfully"
            return render(request,"resetpassword.html",responseDic)
        else:
            responseDic["errmsg"]="Password Reset Failed"
            return render(request,"resetpassword.html",responseDic)
    except:
        responseDic["errmsg"]="No valid user found"
        return render(request,"resetpassword.html",responseDic)


@login_required
def signinpage(request):

    if request.method=="POST":
        username=request.POST['username']
        pass1=request.POST['password']
        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            #print(request.user)
            return redirect("indexpage")
        else:
            messages.error(request,"bad credentials")
            return redirect('index')
            #return render(request,'index.html')

    return render(request,'signinpage.html')

@login_required
def signuppage(request):

    if request.method=='POST':
        Username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password']

        myuser=User.objects.create_user(username=Username,email=email,password=pass1)
        myuser.save()
        my_group = Group.objects.get(name='company') 
        my_group.user_set.add(myuser)
        company=Company(username=myuser,email=email,password=pass1)
        company.save()

        messages.success(request,'Your account successfully created.')

        return render(request,"indexpage.html")

    return render(request,'signinpage.html')

@login_required
def indexpage(request):
    return render(request,'indexpage.html')

@login_required
def homepage1(request):
    data=TravelAgency.objects.all()
    hotels=Hotel.objects.all()
    rsts=Restaurant.objects.all()
    pacs=Packages.objects.all()
    rvws=Review.objects.all()
    
    return render (request,"homepage1.html",{'data':data,'hotels':hotels,'rsts':rsts,'pacs':pacs,'rvws':rvws})

    # return render(request,'homepage1.html')
@login_required
def profileuploadTA(request):
    if request.method=='POST':
        Name=request.POST['name']
        Image=request.FILES['image']
        Comname=request.POST['company']
        Service=request.POST['service']
        Place=request.POST['place']
        Daysoftour=request.POST['daysoftour']
        Typeoftour=request.POST['typeoftour']
        Otime=request.POST['Otime']
        ctime=request.POST['ctime']
        description=request.POST['description']

    
        com_obj=Company.objects.get(username=request.user)
        agent=TravelAgency(company=com_obj,name=Name,image=Image,service=Service,place=Place,daysoftour=Daysoftour,typeoftour=Typeoftour,Otime=Otime,ctime=ctime,description=description)
        agent.save()

        messages.success(request,'Your account successfully created.')

        return redirect('Redirectpg')

    
    return render(request,'profileuploadTA.html')

@login_required
def Redirectpg(request):
    return render(request,'Redirectpg.html')

@login_required
def homepage2(request):
    
    data=TravelAgency.objects.all()
    hotels=Hotel.objects.all()
    rsts=Restaurant.objects.all()
    pacs=Packages.objects.all()
    rvws=Review.objects.all()
    
    return render (request,"homepage2.html",{'data':data,'hotels':hotels,'rsts':rsts,'pacs':pacs,'rvws':rvws})

    # return render(request,'homepage2.html')

@login_required
def profileuploadH(request):
    if request.method=='POST':
        Image=request.FILES['image']
        Name=request.POST['name']
        Comname=request.POST['company']
        Place=request.POST['place']
        Date1=request.POST['date1']
        Date2=request.POST['date2']
        Package=request.POST['package']
        Price=request.POST['price']
        About=request.POST['aboutofhotel']
        Address=request.POST['address']

        htl_obj=Company.objects.get(username=request.user)
        hotel=Hotel(company=htl_obj,image=Image,name=Name,place=Place,date1=Date1,date2=Date2,package=Package,price=Price,aboutofhotel=About,address=Address)
        hotel.save()

        messages.success(request,'Your account successfully created.')

        return redirect('Redirectpg')

    
    return render(request,'profileuploadH.html')

@login_required
def homepage3(request):

    data=TravelAgency.objects.all()
    hotels=Hotel.objects.all()
    rsts=Restaurant.objects.all()
    pacs=Packages.objects.all()
    rvws=Review.objects.all()
    
    return render (request,"homepage3.html",{'data':data,'hotels':hotels,'rsts':rsts,'pacs':pacs,'rvws':rvws})

    # return render(request,'homepage3.html')

@login_required
def profileuploadR(request):
    if request.method=='POST':
        Image=request.FILES['image']
        Name=request.POST['name']
        Comname=request.POST['company']
        Place=request.POST['place']
        Phone=request.POST['phone']
        Website=request.POST['website']
        Otime=request.POST['otime']
        Ctime=request.POST['ctime']
        About=request.POST['about']
        Address=request.POST['address']

        res_obj=Company.objects.get(username=request.user)
        resnt=Restaurant(company=res_obj,image=Image,name=Name,place=Place,phone=Phone,website=Website,Otime=Otime,ctime=Ctime,about=About,address=Address)
        resnt.save()

        messages.success(request,'Your account successfully created.')

        return redirect('Redirectpg')

    
    return render(request,'profileuploadR.html')

@login_required
def displayTA(request):

    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= TravelAgency.objects.filter(company_id=user_id)
    template = loader.get_template('profile_TA.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def displayH(request):

    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Hotel.objects.filter(company_id=user_id)
    template = loader.get_template('profileH.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))

@login_required
def displayR(request):

    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Restaurant.objects.filter(company_id=user_id)
    template = loader.get_template('profileR.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))

@login_required
def deleteprofile_TA(request,id):

    dprofile=TravelAgency.objects.get(id=id)
    dprofile.delete()
    return redirect('Redirectpg')

@login_required
def Profileupdate_TA(request,id):

    try:
 
        newname=request.POST["newname"]
        newimage=request.FILES["newimage"]
        newservice=request.POST["newservice"]
        newplace=request.POST["newplace"]
        newdaysoftour=request.POST["newdaysoftour"]
        newtypeoftour=request.POST["newtypeoftour"]
        newotime=request.POST["newotime"]
        newctime=request.POST["newctime"]
        newdescription=request.POST["newdescription"]


        uproduct=TravelAgency.objects.get(id=id)
        uproduct.name=newname
        uproduct.image=newimage            
        uproduct.service=newservice
        uproduct.place=newplace
        uproduct.dayoftour=newdaysoftour            
        uproduct.typeoftour=newtypeoftour
        uproduct.otime=newotime
        uproduct.ctime=newctime
        uproduct.description=newdescription

        uproduct.save()
        #return render(request,"productupdate.html",{'msg1':"Updated"})
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"Profileupdate_TA.html",{'msg1':"Not updated"})


@login_required
def Profileupdate_H(request,id):

    try:
 
        newimage=request.FILES["newimage"]
        newname=request.POST["newname"]
        newplace=request.POST["newplace"]
        newdate1=request.POST["newdate1"]
        newdate2=request.POST["newdate2"]
        newpackage=request.POST["newpackage"]
        newprice=request.POST["newprice"]
        newabout=request.POST["newabout"]
        newaddress=request.POST["newaddress"]

        uhtl=Hotel.objects.get(id=id)
        uhtl.image=newimage
        uhtl.name=newname            
        uhtl.place=newplace
        uhtl.date1=newdate1         
        uhtl.date2=newdate2
        uhtl.package=newpackage
        uhtl.price=newprice
        uhtl.aboutofhotel=newabout
        uhtl.address=newaddress

        uhtl.save()
        #return render(request,"productupdate.html",{'msg1':"Updated"})
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"Profileupdate_H.html",{'msg1':"Not updated"})


@login_required
def Profileupdate_R(request,id):

    try:
 
        newimage=request.FILES["newimage"]
        newname=request.POST["newname"]
        newplace=request.POST["newplace"]
        newphone=request.POST["newphone"]
        newwebsite=request.POST["newwebsite"]
        newotime=request.POST["newotime"]
        newctime=request.POST["newctime"]
        newabout=request.POST["newabout"]
        newaddress=request.POST["newaddress"]

        pac=Restaurant.objects.get(id=id)
        pac.image=newimage
        pac.name=newname            
        pac.place=newplace
        pac.phone=newphone         
        pac.website=newwebsite
        pac.otime=newotime
        pac.ctime=newctime
        pac.about=newabout
        pac.address=newaddress

        pac.save()
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"Profileupdate_R.html",{'msg1':"Not updated"})


@login_required
def packageupload(request):
    if request.method=='POST':
        Image=request.FILES['image']
        Title=request.POST['title']
        Name=request.POST['name']
        price=request.POST['price']
        nameofTA=request.POST['Travelagency']
        company=request.POST['company']
        Description=request.POST['description']
        Duration=request.POST['duration']
        Meals=request.POST['meals']
        Accommodation=request.POST['accommodation']
        Placeofa=request.POST['placeofa']
        Dates=request.POST['dates']
        Admission=request.POST['admission']
        Helpno=request.POST['helpno']
        Canceldate=request.POST['canceldate']
        Additionalinfo=request.POST['additionalinfo']
        Startpoint=request.POST['startpoint']
        Place1=request.POST['place1']
        Place2=request.POST['place2']
        Place3=request.POST['place3']
        
        pac_obj=TravelAgency.objects.get(name=nameofTA)
        pac_obj2=Company.objects.get(username=company)
        pack=Packages(Travelagency=pac_obj,company=pac_obj2,image=Image,title=Title,name=Name,price=price,description=Description,
        duration=Duration,meals=Meals,accommodation=Accommodation
        ,placeofa=Placeofa,dates=Dates,admission=Admission,helpno=Helpno,canceldate=Canceldate,additionalinfo=Additionalinfo,startpoint=Startpoint,place1=Place1,place2=Place2,place3=Place3)
        pack.save()
        messages.success(request,'Your account successfully created.')
        return redirect('Redirectpg')
    return render(request,'packageupload.html')


@login_required
def displayPac(request):
    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Packages.objects.filter(company_id=user_id)
    template = loader.get_template('packages.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def packages(request):
    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Packages.objects.filter(company_id=user_id)
    template = loader.get_template('packages.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def packageupdate(request,id):

    try:
        # newimage=request.FILES["newimage"]
        newtitle=request.POST["newtitle"]
        newname=request.POST["newname"]
        newdescription=request.POST["newdescription"]
        newduration=request.POST["newduration"]
        newmeals=request.POST["newmeals"]
        newaccommodation=request.POST["newaccommodation"]
        newplaceofa=request.POST["newplaceofa"]
        newdates=request.POST["newdates"]
        newadmission=request.POST["newadmission"]
        newhelpno=request.POST["newhelpno"]
        newcanceldate=request.POST["newcanceldate"]
        newadditionalinfo=request.POST["newadditionalinfo"]
        newstartpoint=request.POST["newstartpoint"]
        newplace1=request.POST["newplace1"]
        newplace2=request.POST["newplace2"]
        newplace3=request.POST["newplace3"]

        pac=Packages.objects.get(id=id)
        # pac.image=newimage
        pac.title=newtitle
        pac.name=newname            
        pac.description=newdescription
        pac.duration=newduration         
        pac.meals=newmeals
        pac.accommodation=newaccommodation
        pac.placeofa=newplaceofa
        pac.dates=newdates
        pac.admission=newadmission
        pac.helpno=newhelpno
        pac.canceldate=newcanceldate
        pac.additionalinfo=newadditionalinfo
        pac.startpoint=newstartpoint
        pac.place1=newplace1
        pac.place2=newplace2
        pac.place3=newplace3
        pac.save()
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"Packageupdate.html")


@login_required
def deletepackage(request,id):

    dpac=Packages.objects.get(id=id)
    dpac.delete()
    return redirect('Redirectpg')

@login_required
def reviewupload(request):
    if request.method=='POST':
        Image=request.FILES['image']
        review=request.POST['review']
        applicant=request.POST['applicant']
        rvw_obj=Applicant.objects.get(username=request.user)
        rvw=Review(applicant=rvw_obj,image=Image,review=review)
        rvw.save()

        messages.success(request,'Your account successfully created.')

        return redirect('Redirectpg')

    
    return render(request,'reviewpage.html')


@login_required
def displayRvw(request):

    current_user=Applicant.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Review.objects.filter(applicant_id=user_id)
    template = loader.get_template('review.html')
    context = {
        'rvw':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def deleteRvw(request,id):

    drvw=Review.objects.get(id=id)
    drvw.delete()
    return redirect('Redirectpg')

@login_required
def displayuser(request):
    return render(request, 'userprofileupload.html')


@login_required
def userprofileupdate(request,id):

    try:
        newname=request.POST["newname"]
        newemail=request.POST["newemail"]
        newlocation=request.POST["newlocation"]
        newabout=request.POST["newabout"]
        userprf=User.objects.get(id=id)
        prf=Applicant.objects.get(username=userprf.username)
        userprf.username=newname
        userprf.email=newemail
        userprf.save()
        
        prf.username=newname 
        prf.email=newemail            
        prf.location=newlocation
        prf.about=newabout
        prf.save()
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"userprofileupdate.html")


@login_required    
def search_TA(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name=q) | Q(place=q))
        data = TravelAgency.objects.filter(multiple_q)
    else:
        data = TravelAgency.objects.all()
    context = {
        'data': data
    }
    return render(request, 'search_TA.html', context)


@login_required
def search_H(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name=q) | Q(place=q))
        data = Hotel.objects.filter(multiple_q)
    else:
        data = Hotel.objects.all()
    context = {
        'data': data
    }
    return render(request, 'search_H.html', context)


@login_required
def search_R(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(Q(name=q) | Q(place=q))
        data = Restaurant.objects.filter(multiple_q)
    else:
        data = Restaurant.objects.all()
    context = {
        'data': data
    }
    return render(request, 'search_R.html', context)


@login_required
def search_rvw(request):

    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        multiple_q = Q(review=q)
        data = Review.objects.filter(multiple_q)
    else:
        data = Review.objects.all()
    context = {
        'data': data
    }
    return render(request, 'search_rvw.html', context)


@login_required
def viewmore_TA(request,id):
    current_agency=TravelAgency.objects.get(id=id)
    user_id=current_agency.id
    mydata= TravelAgency.objects.filter(id=user_id)
    template = loader.get_template('viewmore_TA.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def viewPac(request,id):
    current_agency=TravelAgency.objects.get(id=id)
    user_id=current_agency.id
    mydata= Packages.objects.filter(Travelagency_id=user_id)
    template = loader.get_template('viewPac.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def viewmore_H(request,id):
    current_agency=Hotel.objects.get(id=id)
    user_id=current_agency.id
    mydata= Hotel.objects.filter(id=user_id)
    template = loader.get_template('viewmore_H.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def viewmore_R(request,id):
    current_agency=Restaurant.objects.get(id=id)
    user_id=current_agency.id
    mydata= Restaurant.objects.filter(id=user_id)
    template = loader.get_template('viewmore_R.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def viewmore_Pac(request,id):
    current_agency=Packages.objects.get(id=id)
    user_id=current_agency.id
    mydata= Packages.objects.filter(id=user_id)
    template = loader.get_template('viewmore_Pac.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def addtocart(request,id):
    cart=Packages.objects.get(id=id)
    cid=cart.id
    mydata= Packages.objects.filter(id=cid)
    applicant=Applicant.objects.get(username=request.user)
    applicant_id=applicant.id
    cartobj=Cart.objects.create(user=applicant,name=cart.name,image=cart.image,title=cart.title,price=cart.price)
    cartobj.save()
    template = loader.get_template('Redirectpg.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def cart(request,id):
    
    applicant=Applicant.objects.get(username=request.user)
    applicant_id=applicant.id
    cartobjs=Cart.objects.filter(user_id=applicant_id)
    return render(request,'cart.html',{'cartobjs':cartobjs})


@login_required
def showcart(request,id):
    applicant=Applicant.objects.get(username=request.user)
    applicant_id=applicant.id
    cartobjs=Cart.objects.filter(user_id=applicant_id)
    return render(request,'cart.html',{'cartobjs':cartobjs})


@login_required
def delete_cartobjs(request,id):

    dobjs=Cart.objects.get(id=id)
    dobjs.delete()
    return redirect('Redirectpg')


@login_required
def menuupload(request):
    if request.method=='POST':
        Image=request.FILES['image']
        Name=request.POST['name']
        nameofR=request.POST['restaurant']
        company=request.POST['company']
        Description=request.POST['description']
        Price=request.POST['price']
        menu_obj=Restaurant.objects.get(name=nameofR)
        menu_obj2=Company.objects.get(username=company)
        menu=Menu(restaurant=menu_obj,company=menu_obj2,image=Image,name=Name,description=Description,price=Price)
        menu.save()
        messages.success(request,'Your account successfully created.')
        return redirect('Redirectpg')
    return render(request,'menuupload.html')


@login_required
def displaymenu(request):
    current_user=Company.objects.get(username=request.user)
    user_id=current_user.id
    mydata= Menu.objects.filter(company_id=user_id)
    template = loader.get_template('menu.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))



@login_required
def menuupdate(request,id):

    try:
        newimage=request.FILES["newimage"]
        newname=request.POST["newname"]
        newdescription=request.POST["newdescription"]
        newprice=request.POST["newprice"]
        
        menu=Menu.objects.get(id=id)
        menu.image=newimage
        menu.name=newname
        menu.description=newdescription
        menu.price=newprice 
        menu.save()
        return redirect('Redirectpg')
    
    except Exception as e:
        print(e)
        return render(request,"menuupdate.html")    


@login_required
def deletemenu(request,id):

    dmenu=Menu.objects.get(id=id)
    dmenu.delete()
    return redirect('Redirectpg')


@login_required       
def viewmenu(request,id):
    current_agency=Restaurant.objects.get(id=id)
    user_id=current_agency.id
    mydata= Menu.objects.filter(restaurant_id=user_id)
    template = loader.get_template('viewmenu.html')
    context = {
        'midata':mydata,
    }
    return HttpResponse(template.render(context,request))


@login_required
def paymentsuccess(request):
    return render(request,'paymentsuccess.html')


# def displayprofileTA(request):

#     current_user=Company.objects.get(username=request.user)
#     user_id=current_user.id
#     mydata= TravelAgency.objects.filter(company_id=user_id)
#     template = loader.get_template('.html')
#     context = {
#         'rvw':mydata,
#     }
#     return HttpResponse(template.render(context,request))


@login_required
def intro(request):

    data = TravelAgency.objects.filter(name='Mauritius')
    data2 = Packages.objects.filter(title='mauritius')
   
    return render (request,"intro.html",{'data':data,'data2':data2})



@login_required
def intro2(request):

    data = TravelAgency.objects.filter(name='Greece')
    data2 = Packages.objects.filter(title='Greece')
   
    return render (request,"intro2.html",{'data':data,'data2':data2})



@login_required
def intro3(request):

    data = TravelAgency.objects.filter(name='Scotland')
    data2 = Packages.objects.filter(title='Scotland')
   
    return render (request,"intro3.html",{'data':data,'data2':data2})