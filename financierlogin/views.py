from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import Signup,FinancierProfileForm
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
from home.models import FinancierProfile,State,District,SubDistrict,Pincode,Usertype


@login_required
def userlogout(request):
    logout(request)
    return redirect("home:home")
    

def signup(request):
    msg1=''
    if request.method == 'POST':
        form = Signup(request.POST)
        financierform = FinancierProfileForm(request.POST)
        if form.is_valid() and financierform.is_valid():
            user = form.save()
            user.is_active = False
            user.is_financier = True
            user.save()
            profile = financierform.save(commit=False)
            profile.user=user
            profile.save()
            
            temp = Usertype.objects.get_or_create(
                        user = user,
                        is_financier = True,
                    )

            current_site = get_current_site(request)
            mail_subject = 'Activate your MooMa account.'
            message = render_to_string('financierlogin/account_activation_email.html', {
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
            return render(request, 'financierlogin/activation.html', {'msg1': msg1})

    else:
        form = Signup()
        financierform = FinancierProfileForm()
    return render(request, 'financierlogin/signup.html', {'form': form,'financierform':financierform})



def activate(request, uidb64, token):
    msg2=''
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        financier = FinancierProfile.objects.get(user=user)
        financier.email_confirmed = True
        #financier.is_financier = True
        financier.save()
        #user.is_valid = True
        user.save()
        login(request, user)
        return redirect('visualfinancier:visual')

    else:
        msg1='Activation link is expired!'
        return render(request,'financierlogin/activation.html', {'msg1': msg1})
       

def userlogin(request):
    error=''
    if request.user.is_authenticated:
        return redirect('visualfinancier:visual')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                u = Usertype.objects.get(user=user)
                if user is not None and u.is_financier:
                    login(request, user)
                    #return HttpResponse("You are now logged in as {username}")
                    return redirect('visualfinancier:visual')
                
                else:
                    #return HttpResponse("Invalid username or password.")
                    error = "Invalid username or password."
            else:
                #return HttpResponse("Invalid username or password.")
                error = "Invalid username or password."

        form = AuthenticationForm()
        return render(request = request,
                        template_name = "financierlogin/login.html",
                        context={"form":form,"error":error})



def load_districts(request):
    state_id = request.GET.get('state')
    districts = District.objects.filter(state_id=state_id).order_by('name')

    return render(request, 'financierlogin/dropdown.html', {'districts': districts})

def load_subdistricts(request):
    district_id = request.GET.get('district')
    subdistricts = SubDistrict.objects.filter(district_id=district_id).order_by('name')

    return render(request, 'financierlogin/dropdown1.html', {'subdistricts':subdistricts})

def load_pincode(request):
    subdistrict_id = request.GET.get('subdistrict')
    pincodes = Pincode.objects.filter(subdistrict_id=subdistrict_id).order_by('name')

    return render(request, 'financierlogin/dropdown2.html', {'pincodes':pincodes})