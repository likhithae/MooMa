from django.contrib import admin
from .models import Contactus,FarmerProfile,State,District,SubDistrict,Pincode,FinancierProfile,Usertype
# Register your models here.

admin.site.register(Usertype)
admin.site.register(Contactus)
admin.site.register(FarmerProfile)
admin.site.register(FinancierProfile)
admin.site.register(State)
admin.site.register(District)
admin.site.register(SubDistrict)
admin.site.register(Pincode)