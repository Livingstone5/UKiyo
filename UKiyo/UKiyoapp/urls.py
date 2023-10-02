from django.urls import path,include
from .import views
# from Bookings import views 


#from UKiyoapp import views


urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.firstpg,name='firstpg'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    #path('home2',views.home2,name='home2'),
    path('reset',views.resethome,name='reset'),
    path('resetpassword',views.resetpassword,name='resetpassword'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('indexpage',views.indexpage,name='indexpage'),
    path('homepage1',views.homepage1,name='homepage1'),
    path('profileuploadTA',views.profileuploadTA,name='profileuploadTA'),
    path('Redirectpg',views.Redirectpg,name='Redirectpg'),
    path('homepage2',views.homepage2,name='homepage2'),
    path('profileuploadH',views.profileuploadH,name='profileuploadH'),
    path('homepage3',views.homepage3,name='homepage3'),
    path('profileuploadR',views.profileuploadR,name='profileuploadR'),
    path('displayTA',views.displayTA,name='displayTA'),
    path('displayH',views.displayH,name='displayH'),
    path('displayR',views.displayR,name='displayR'),
    path("profileupdate_TA/<int:id>/profileupdate_TA",views.Profileupdate_TA,name='profileupdate_TA'),
    path("profileupdate_H/<int:id>/profileupdate_H",views.Profileupdate_H,name='profileupdate_H'),
    path("profileupdate_R/<int:id>/profileupdate_R",views.Profileupdate_R,name='profileupdate_R'),
    path("deleteprofile_TA/<int:id>/",views.deleteprofile_TA,name='deleteprofile_TA'),
    path('packageupload',views.packageupload,name='packageupload'),
    # path('ProfileT',views.ProfileT,name='ProfileT'),
    path('displayPac',views.displayPac,name='displayPac'),
    path('packages',views.packages,name='packages'),
    path("packageupdate/<int:id>/packageupdate",views.packageupdate,name='packageupdate'),
    path("deletepackage/<int:id>/",views.deletepackage,name='deletepackage'),
    path('reviewupload',views.reviewupload,name='reviewupload'),
    path('displayRvw',views.displayRvw,name='displayRvw'),
    path("deleteRvw/<int:id>/",views.deleteRvw,name='deleteRvw'),
    path('displayuser',views.displayuser,name='displayuser'),
    path("userprofileupdate/<int:id>/userprofileupdate",views.userprofileupdate,name='userprofileupdate'),
    path('search_TA',views.search_TA,name='search_TA'),
    path('search_H',views.search_H,name='search_H'),
    path('search_R',views.search_R,name='search_R'),
    path('search_rvw',views.search_rvw,name='search_rvw'),
    path('viewmore_TA/<int:id>/viewmore_TA',views.viewmore_TA,name='viewmore_TA'),
    path('viewPac/<int:id>/viewPac',views.viewPac,name='viewPac'),
    path('viewmore_H/<int:id>/viewmore_H',views.viewmore_H,name='viewmore_H'),
    path('viewmore_R/<int:id>/viewmore_R',views.viewmore_R,name='viewmore_R'),
    path('viewmore_Pac/<int:id>/viewmore_Pac',views.viewmore_Pac,name='viewmore_Pac'),
    path("addtocart/<int:id>/",views.addtocart,name='addtocart'),
    path('addtocart/<int:id>/cart',views.cart,name='cart'),
    path('cart/<int:id>',views.cart,name='cart'),
    path("delete_cartobjs/<int:id>/",views.delete_cartobjs,name='delete_cartobjs'),
    path('menuupload',views.menuupload,name='menuupload'),
    path('displaymenu',views.displaymenu,name='displaymenu'),
    path("menuupdate/<int:id>/menuupdate",views.menuupdate,name='menuupdate'),
    path("deletemenu/<int:id>/",views.deletemenu,name='deletemenu'),
    path('viewmenu/<int:id>/viewmenu',views.viewmenu,name='viewmenu'),
    path('payment/payment/paymenthandler/paymentsuccess',views.paymentsuccess,name='paymentsuccess'),
    path('book/',include('Bookings.urls')),
    # path("viewbookings",views.viewbookings,name='viewbookings')
    path('intro',views.intro,name='intro'),
    path('intro2',views.intro2,name='intro2'),
    path('intro3',views.intro3,name='intro3'),


    #path("book/bookhome",views.book,name='book')


    # path('payment', views.payment, name='payment'),
    # path('homepage', views.homepage, name='payment'),
	# path('paymenthandler/', views.paymenthandler, name='paymenthandler'),






    







    





    
    
    






]