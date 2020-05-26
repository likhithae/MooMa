from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import FinancierProfile,District,SubDistrict,Pincode
from phonenumber_field.formfields import PhoneNumberField
#from home.models import CustomUser

class Signup(UserCreationForm):
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


class FinancierProfileForm(forms.ModelForm):
    Size_of_farm = forms.IntegerField(widget=forms.TextInput())
    Mooma_user_id = forms.IntegerField(widget=forms.TextInput())

    class Meta:
        model = FinancierProfile
        fields = [ 
            'Mooma_user_id',
            'first_name', 
            'last_name',
            'state',
            'district',
            'subdistrict',
            'pincode',
            'Address',
            'Phone_number',
            'Size_of_farm',
            'Equipment_used',
            'Installed_date',
            'Jersey',
            'Holstein_Friesian',
            'Sahiwal',
            'Khillar',
            'Gir',
            'Other_breed',
            'Mixed_breed'
            ]

        widgets = {
            'Phone_number': forms.TextInput(attrs={'class': 'phoneclass'}),
            'Installed_date': forms.SelectDateWidget(years=range(2017,2030),attrs={'class': 'dateclass'}),
            'state': forms.Select(attrs={'class': 'myclass'}),
            'district': forms.Select(attrs={'class': 'myclass'}),
            'subdistrict': forms.Select(attrs={'class': 'myclass'}),
            'pincode': forms.Select(attrs={'class': 'myclass'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].queryset = District.objects.none()
    
    
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['district'].queryset = District.objects.filter(state_id=state_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['district'].queryset = self.instance.state.district_set.order_by('name')
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subdistrict'].queryset = SubDistrict.objects.none()
     
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['subdistrict'].queryset = SubDistrict.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subdistrict'].queryset = self.instance.district.subdistrict_set.order_by('name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pincode'].queryset = Pincode.objects.none()
     
        if 'subdistrict' in self.data:
            try:
                subdistrict_id = int(self.data.get('subdistrict'))
                self.fields['pincode'].queryset = Pincode.objects.filter(subdistrict_id=subdistrict_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['pincode'].queryset = self.instance.subdistrict.pincode_set.order_by('name')
