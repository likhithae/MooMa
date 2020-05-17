from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import FarmerProfile
from phonenumber_field.formfields import PhoneNumberField

# Sign Up Form
'''
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')
    Address = forms.CharField(max_length=300)
    #phone_regex = RegexValidator(regex=r'^\?1?\d{9,10}$')
    #Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    Phone_number = forms.CharField(max_length=10,help_text='Enter a valid Phone number')
    Size_of_farm = forms.IntegerField()
    Equipment_used = forms.CharField(max_length=300)
    Breed_type = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'Address',
            'Phone_number',
            'Size_of_farm',
            'Equipment_used',
            'Breed_type',
            'password1', 
            'password2', 
            ]
'''

class SignupForm(UserCreationForm):
    #username = forms.CharField(max_length=50, required=True)
    #last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address',widget=forms.TextInput())    
    

    class Meta:
        model = User
        fields = [
            'username',  
            'email',
            'password1', 
            'password2', 
            ]


class FarmerProfileForm(forms.ModelForm):
    Size_of_farm = forms.IntegerField(widget=forms.TextInput())
    Mooma_user_id = forms.IntegerField(widget=forms.TextInput())
    #Phone_number = forms.BigIntegerField(widget=forms.TextInput())
    Phone_number = PhoneNumberField(widget=forms.TextInput())
    class Meta:
        model = FarmerProfile
        fields = [ 
            'Mooma_user_id',
            'first_name', 
            'last_name',
            'Address',
            'Phone_number',
            'Size_of_farm',
            'Equipment_used',
            'Jersey',
            'Holstein_Friesian',
            'Sahiwal',
            'Khillar',
            'Gir',
            'Other_breed',
            'Mixed_breed'
            ]
