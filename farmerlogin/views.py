from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm,FarmerProfileForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from home.models import FarmerProfile
#from home.models import FarmerLogin


#@login_required
#def loggedin(request):
#    return HttpResponse("You are logged in !")

@login_required
def userlogout(request):
    logout(request)
    #messages.info(request, "Logged out successfully!")
    return redirect("home:home")
    

def signup(request):
    msg1=''
    if request.method == 'POST':
        form = SignupForm(request.POST)
        farmerform = FarmerProfileForm(request.POST)
        if form.is_valid() and farmerform.is_valid():
            user = form.save()
            user.is_active = False
            #user.refresh_from_db()
            #user.is_valid = False
            #user.set_password(user.password)
            user.save()
            #user.profile.email = form.cleaned_data.get('email')
            #user.profile.first_name = form.cleaned_data.get('first_name')
            #user.profile.last_name = form.cleaned_data.get('last_name')
            #user.profile.Address = form.cleaned_data.get('Address')
            #user.profile.Phone_number = form.cleaned_data.get('Phone_number')
            #user.profile.Size_of_farm = form.cleaned_data.get('Size_of_farm')
            #user.profile.Equipment_used = form.cleaned_data.get('Equipment_used')
            #user.profile.Breed_type = form.cleaned_data.get('Breed_type')
            profile = farmerform.save(commit=False)
            profile.user=user
            profile.save()
            
            #farmerform.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your MooMa account.'
            message = render_to_string('farmerlogin/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            msg1 = 'Please confirm your email address to complete the registration'
            email.send()
            return render(request, 'farmerlogin/activation.html', {'msg1': msg1})
            #return HttpResponse('Please confirm your email address to complete the registration')

    else:
        form = SignupForm()
        farmerform = FarmerProfileForm()
    return render(request, 'farmerlogin/signup.html', {'form': form,'farmerform':farmerform})



def activate(request, uidb64, token):
    msg2=''
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        farmer = FarmerProfile.objects.get(user=user)
        farmer.email_confirmed = True
        farmer.save()
        #user.is_valid = True
        user.save()
        login(request, user)
        return redirect('visual:visual')
        #msg2='Thank you for your email confirmation. Now you can login your account.'
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        #return HttpResponseRedirect(request, 'farmerlogin/login.html', {'msg2': msg2})
        #return render(request,'farmerlogin/login.html', {'msg2':msg2})
    else:
        msg1='Activation link is expired!'
        return render(request,'farmerlogin/activation.html', {'msg1': msg1})
       

def userlogin(request):
    error=''
    if request.user.is_authenticated:
        return redirect('visual:visual')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    #return HttpResponse("You are now logged in as {username}")
                    return redirect('visual:visual')
                
                else:
                    #return HttpResponse("Invalid username or password.")
                    error = "Invalid username or password."
            else:
                #return HttpResponse("Invalid username or password.")
                error = "Invalid username or password."

        form = AuthenticationForm()
        return render(request = request,
                        template_name = "farmerlogin/login.html",
                        context={"form":form,"error":error})


