from django.db import models

# Create your models here.
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
    message = models.TextField(max_length=500)