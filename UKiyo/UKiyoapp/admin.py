from django.contrib import admin
from.models import Applicant,TravelAgency,Company,Hotel,Restaurant,Packages,Review,Cart,Menu


class ApplicantAdmin(admin.ModelAdmin):
    list_display=('username','email','password','location','about')
    ordering=('username',)
    search_fields=('username','email','location')

admin.site.register(Applicant,ApplicantAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display=('username','email','password',)
    ordering=('username',)
    search_fields=('username','email',)

admin.site.register(Company,CompanyAdmin)

class TravelAgencyAdmin(admin.ModelAdmin):
    list_display=('image','name','service','place','daysoftour','typeoftour','Otime','ctime','description',)
    ordering=('name',)
    search_fields=('name','service','place','daysoftour','typeoftour',)

admin.site.register(TravelAgency,TravelAgencyAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display=('image','name','place','date1','date2','package','price','aboutofhotel','address',)
    ordering=('name',)
    search_fields=('name','place',)

admin.site.register(Hotel,HotelAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display=('image','name','place','phone','website','ctime','about','address',)
    ordering=('name',)
    search_fields=('name','place','website',)

admin.site.register(Restaurant,RestaurantAdmin)

class PackagesAdmin(admin.ModelAdmin):
    list_display=('image','title','placeofa','price','description','duration','meals','accommodation','dates','admission','helpno','canceldate','additionalinfo','startpoint','place1','place2','place3')
    ordering=('title',)
    search_fields=('title','place','duration',)

admin.site.register(Packages,PackagesAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=('image','review',)
    ordering=('review',)
    search_fields=('review',)

admin.site.register(Review,ReviewAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display=('image','title','name','price',)
    ordering=('name',)
    search_fields=('name','title',)

admin.site.register(Cart,CartAdmin)

class MenuAdmin(admin.ModelAdmin):
    list_display=('image','name','description','price',)
    ordering=('name',)
    search_fields=('name',)

admin.site.register(Menu,MenuAdmin)