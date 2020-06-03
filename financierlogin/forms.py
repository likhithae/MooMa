from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from home.models import FinancierProfile,District,ACity,bank,branch,ifsc
from phonenumber_field.formfields import PhoneNumberField


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
    Mooma_user_id = forms.IntegerField(widget=forms.TextInput())

    class Meta:
        model = FinancierProfile
        fields = [ 
            'Mooma_user_id',
            'first_name', 
            'last_name',
            'state',
            'district',
            'city',
            'Phone_number',
            'bank',
            'branch',
            'ifsccode',
            ]

        widgets = {
            'Phone_number': forms.TextInput(attrs={'class': 'phoneclass'}),
            'state': forms.Select(attrs={'class': 'myclass'}),
            'district': forms.Select(attrs={'class': 'myclass'}),
            'city': forms.Select(attrs={'class': 'myclass'}),
            'bank': forms.Select(attrs={'class': 'myclass'}),
            'branch': forms.Select(attrs={'class': 'myclass'}),
            'ifsccode': forms.Select(attrs={'class': 'myclass'}),
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
        self.fields['city'].queryset = ACity.objects.none()
     
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['city'].queryset = ACity.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.district.city_set.order_by('name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bank'].queryset = bank.objects.none()
     
        if 'city' in self.data:
            try:
                city_id = int(self.data.get('city'))
                self.fields['bank'].queryset = bank.objects.filter(city_id=city_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['bank'].queryset = self.instance.city.bank_set.order_by('name')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = branch.objects.none()
     
        if 'bank' in self.data:
            try:
                bank_id = int(self.data.get('bank'))
                self.fields['branch'].queryset = branch.objects.filter(bank_id=bank_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.bank.branch_set.order_by('name')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ifsccode'].queryset = ifsc.objects.none()
    
        if 'branch' in self.data:
            try:
                branch_id = int(self.data.get('branch'))
                self.fields['ifsccode'].queryset = ifsc.objects.filter(branch_id=branch_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['ifsccode'].queryset = self.instance.branch.ifsccode_set.order_by('name')
