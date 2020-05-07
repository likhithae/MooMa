from django import forms
#from django.forms import ModelForm
from home.models import Contactus


class Contactusform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ["name","email","phonenumber","message"]


