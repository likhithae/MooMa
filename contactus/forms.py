from django import forms
#from django.forms import ModelForm
from home.models import Contactus


class Contactusform(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = ["name","email","phonenumber","message"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'nameclass','placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'emailclass','placeholder': 'Your Email'}),
            'phonenumber': forms.TextInput(attrs={'class': 'phoneclass','placeholder': 'Your Number'}),
            'message': forms.TextInput(attrs={'class': 'msgclass','placeholder': 'Your Message'}),
        }



