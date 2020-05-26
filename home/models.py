from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings
#from django.contrib.auth import get_user_model

    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    message = models.TextField(max_length=500)


class State(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class SubDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Pincode(models.Model):
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#class CustomUser(AbstractUser):
#    is_farmer = models.BooleanField(default=False)
#    is_financier = models.BooleanField(default=False)
#    is_admin = models.BooleanField(default=False)

class Usertype(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_farmer = models.BooleanField(default=False)
    is_financier = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    #is_farmer = models.BooleanField(default=False)
    modeltype = 'Farmer'
    Mooma_user_id  = models.IntegerField(blank=False) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True)
    pincode = models.ForeignKey(Pincode, on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=300)
    #phone_regex = RegexValidator(regex=r'^\?1?\d{9,10}$')
    #Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #Phone_number = models.CharField(max_length=10)
    #Phone_number =  PhoneField()
    Phone_number = PhoneNumberField(null=False,unique=True)
    Size_of_farm = models.IntegerField()
    Equipment_used = models.CharField(max_length=300)
    Installed_date = models.DateField(default=date.today())
    #Breed_type = models.CharField(max_length=50)
    #Breed_type = models.ManyToManyField(Choices)
    Jersey = models.BooleanField(blank=True,default=False)
    Holstein_Friesian = models.BooleanField(blank=True,default=False)
    Sahiwal = models.BooleanField(blank=True,default=False)
    Khillar = models.BooleanField(blank=True,default=False)
    Gir = models.BooleanField(blank=True,default=False)
    Other_breed = models.CharField(max_length=200,blank=True)
    Mixed_breed = models.CharField(max_length=200,blank=True)
     
    def __unicode__(self):
        return self.user.username


class FinancierProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    #is_financier = models.BooleanField(default=False)
    modeltype = 'Financier'
    Mooma_user_id  = models.IntegerField(blank=False) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.SET_NULL, null=True)
    pincode = models.ForeignKey(Pincode, on_delete=models.SET_NULL, null=True)
    Address = models.CharField(max_length=300)
    #phone_regex = RegexValidator(regex=r'^\?1?\d{9,10}$')
    #Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #Phone_number = models.CharField(max_length=10)
    #Phone_number =  PhoneField()
    Phone_number = PhoneNumberField(null=False,unique=True)
    Size_of_farm = models.IntegerField()
    Equipment_used = models.CharField(max_length=300)
    Installed_date = models.DateField(default=date.today())
    #Breed_type = models.CharField(max_length=50)
    #Breed_type = models.ManyToManyField(Choices)
    Jersey = models.BooleanField(blank=True,default=False)
    Holstein_Friesian = models.BooleanField(blank=True,default=False)
    Sahiwal = models.BooleanField(blank=True,default=False)
    Khillar = models.BooleanField(blank=True,default=False)
    Gir = models.BooleanField(blank=True,default=False)
    Other_breed = models.CharField(max_length=200,blank=True)
    Mixed_breed = models.CharField(max_length=200,blank=True)
     
    def __unicode__(self):
        return self.user.username
