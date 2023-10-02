
from django.urls import path
from .import views

urlpatterns = [

path("bookhome/<int:id>",views.bookings,name='book'),
path("viewbookings",views.viewbookings,name='viewbookings'),



]