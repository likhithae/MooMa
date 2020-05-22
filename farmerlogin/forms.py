from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import FarmerProfile,District,SubDistrict,Pincode
from phonenumber_field.formfields import PhoneNumberField


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
    #Phone_number = PhoneNumberField(widget=forms.TextInput())
    #Installed_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2017,2030)))
    #subdistrict = forms.ForeignKey(widget=forms.TextInput())

    class Meta:
        model = FarmerProfile
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
