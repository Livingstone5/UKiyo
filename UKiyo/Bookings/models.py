from django.db import models
from UKiyoapp.models import Applicant,Company,TravelAgency,Packages,Hotel,Restaurant,Review,Cart,Menu

class Bookings(models.Model):
    applicant=models.ForeignKey(Applicant,on_delete=models.CASCADE)
    #company=models.ForeignKey(Company,on_delete=models.CASCADE)
    #travelAgency=models.ForeignKey(TravelAgency,on_delete=models.CASCADE)
    packages=models.ForeignKey(Packages,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=20,null=True,blank=True)
    name=models.CharField(max_length=20,null=True,blank=True)
    price=models.IntegerField()
    username=models.CharField(max_length=20,null=True,blank=True)
    location=models.CharField(max_length=20,null=True,blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookings'
        verbose_name_plural='Bookings'
