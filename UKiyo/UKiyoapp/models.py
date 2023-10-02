from django.db import models
from django.contrib.auth.models import User


class Applicant(models.Model):

    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)
    location=models.CharField(max_length=50,blank=True,null=True)
    about=models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.username


    class Meta:
        db_table = 'applicant'
        verbose_name_plural='Applicants'

class Company(models.Model):

    username=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'company'
        verbose_name_plural='Companies'

class TravelAgency(models.Model):
    image=models.ImageField(blank=True,upload_to='')
    name=models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    service=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    daysoftour=models.CharField(max_length=20)
    typeoftour=models.CharField(max_length=50)
    Otime=models.CharField(max_length=20)
    ctime=models.CharField(max_length=20)
    description=models.CharField(max_length=100)

    
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'travelagency'
        verbose_name_plural='TravelAgencies'

class Hotel(models.Model):

    image=models.ImageField(blank=True)
    name=models.CharField(max_length=20)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    place=models.CharField(max_length=30)
    date1=models.DateField()
    date2=models.DateField()
    package=models.CharField(max_length=20)
    price=models.IntegerField()
    aboutofhotel=models.CharField(max_length=200)
    address=models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hotel'
        verbose_name_plural='Hotels'

class Restaurant(models.Model):

    image=models.ImageField(blank=True)
    name=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    place=models.CharField(max_length=30)
    phone=models.IntegerField()
    website=models.CharField(max_length=30)
    Otime=models.TimeField(max_length=20)
    ctime=models.TimeField(max_length=20)
    about=models.CharField(max_length=200)
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'restaurant'
        verbose_name_plural='Restaurants'

class Packages(models.Model):
    image=models.ImageField(blank=True)
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    Travelagency=models.ForeignKey(TravelAgency,on_delete=models.CASCADE,blank=True)
    price=models.IntegerField(default=0000000)
    description=models.CharField(max_length=100)
    duration=models.CharField(max_length=20)
    meals=models.CharField(max_length=20)
    accommodation=models.CharField(max_length=20)
    placeofa=models.CharField(max_length=50)
    dates=models.DateField()
    admission=models.CharField(max_length=20)
    helpno=models.IntegerField()
    canceldate=models.DateField()
    additionalinfo=models.CharField(max_length=100)
    startpoint=models.CharField(max_length=50)
    place1=models.CharField(max_length=50)
    place2=models.CharField(max_length=50)
    place3=models.CharField(max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'packages'
        verbose_name_plural='Package_TAs'

class Review(models.Model):
    
    applicant=models.ForeignKey(Applicant,on_delete=models.CASCADE,blank=True)
    image=models.ImageField(blank=True)
    review=models.CharField(max_length=200)

    def __str__(self):
        return self.review

    class Meta:
        db_table = 'Review'
        verbose_name_plural='Reviews'

class Cart(models.Model):
    user=models.ForeignKey(Applicant,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=20,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'cart'
        verbose_name_plural='Carts'

class Menu(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE,blank=True)
    image=models.ImageField(upload_to='')
    name=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    price=models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'
        verbose_name_plural='Menus'




