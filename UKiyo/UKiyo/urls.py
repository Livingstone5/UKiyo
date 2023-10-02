"""
URL configuration for UKiyo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
#from UKiyoapp import views
import Bookings.views
from payment import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('UKiyoapp.urls')),
    path('book/bookhome/payment/<int:pk>', views.payment, name='payment'),
    path('book/bookhome/payment/payment/homepage',views.homepage,name='homepage'),
    #path('homepage', views.homepage, name='payment'),
	path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('book/bookhome/payment/payment/paymenthandler/',views.paymentsuccess,name='paymentsuccess'),
    path("books",Bookings.views.books,name='books'),
    path("viewbookings",Bookings.views.viewbookings,name='viewbookings'),
    path('payment/<int:pk>', views.payment, name='payment'),
    path('payment/payment/homepage',views.homepage,name='homepage'),
    path('payment/payment/paymenthandler/',views.paymentsuccess,name='paymentsuccess'),


    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)