from django.shortcuts import render
from home.models import Contactus
from .forms import Contactusform

# Create your views here.
#def maps(request):
#   return render(request, 'contactus/contactus.html')

def showform(request):
    form = Contactusform(request.POST)
    if form.is_valid():
        form.save()
        #temp = Contactus.objects.create(name=name, email=email, phonenumber=number, message=message)
    
    context = {'form':form}

    return render(request,'contactus/contactus.html',context)