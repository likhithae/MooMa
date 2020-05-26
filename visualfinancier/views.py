from django.shortcuts import render
import json
import time
import requests
from django.contrib.auth.decorators import login_required
from home.models import FinancierProfile

READ_API_KEY='PT8PTFESBBO4W5GK'
CHANNEL_ID= 1058265

# Create your views here.
@login_required
def visual(request):
   return render(request, 'visualfinancier/visual.html')


def quantity(request):
   return render(request, 'visualfinancier/quantity.html')

def quality(request):
   return render(request, 'visualfinancier/quality.html')

def cowhealth(request):
   return render(request, 'visualfinancier/cowhealth.html')


def profile(request):
   user = request.user
   #print(user)
   financier = FinancierProfile.objects.get(user=user)
   return render(request, 'visualfinancier/profile.html',{'user':user,'financier':financier})
