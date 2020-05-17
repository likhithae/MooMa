from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

#class Choices(models.Model):
#    name = models.CharField(max_length=30,default="jersey")
#    def __str__(self):        
#        return f'{self.name}'
    
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    message = models.TextField(max_length=500)

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    Mooma_user_id  = models.IntegerField(blank=False) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #email = models.EmailField(max_length=254)
    Address = models.CharField(max_length=300)
    #phone_regex = RegexValidator(regex=r'^\?1?\d{9,10}$')
    #Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    #Phone_number = models.CharField(max_length=10)
    #Phone_number =  PhoneField()
    Phone_number = PhoneNumberField(null=False,unique=True)
    Size_of_farm = models.IntegerField()
    Equipment_used = models.CharField(max_length=300)
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
'''
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = FarmerProfile.objects.create(user=instance)
         #profile = MyProfile(user=instance)
        profile.save()
    #instance.profile.save()

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        #Profile.objects.create(user=instance)
        profile = Profile(user=instance)
        profile.save()
    superuser = User.objects.filter(is_superuser=True)
    if not superuser:
       instance.profile.save()

#try:
#   instance.profile.save()
#except 'ObjectDoesNotExist':
# Profile.objects.create(user=instance)
#instance.profile.save()
post_save.connect(update_user_profile, sender=User)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

if instance and created:
        instance.profile = Profile.objects.create(user=instance)
'''