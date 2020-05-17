from django.shortcuts import render
#import urllib2
import urllib.request as urllib2
import json
import time
import requests
from django.contrib.auth.decorators import login_required
from home.models import FarmerProfile

READ_API_KEY='PT8PTFESBBO4W5GK'
CHANNEL_ID= 1058265

# Create your views here.
@login_required
def visual(request):
   a=0
   b=0
   '''
   #while True:
    TS = urllib2.urlopen("http://api.thingspeak.com/channels/1058265/feeds/last.json?api_key=PT8PTFESBBO4W5GK" 
                       #% (CHANNEL_ID,READ_API_KEY))

    response = TS.read()
    data=json.loads(response)

    a = data['created_at']
    b = data['field1']
    #c = data['field2']
    #d = data['field3']
    #print a + "    " + b + "    " + c + "    " + d
    time.sleep(30)   

    TS.close()
    
    with urllib.request.urlopen("https://api.thingspeak.com/channels/1058265/feeds.json?api_key=PT8PTFESBBO4W5GK&results=2") as url:
    #print (url.read())
    a = url.read()
    
    response = requests.get("https://api.thingspeak.com/channels/1058265/feeds.json?api_key=PT8PTFESBBO4W5GK&results=2") 
    if response.status_code == 200:

     a = response.json()
'''
   return render(request, 'visual/visual.html')


def quantity(request):
   return render(request, 'visual/quantity.html')

def quality(request):
   return render(request, 'visual/quality.html')

def cowhealth(request):
   return render(request, 'visual/cowhealth.html')


def profile(request):
   user = request.user
   print(user)
   farmer = FarmerProfile.objects.get(user=user)
   #farmer = FarmerProfile.objects.all()
   return render(request, 'visual/profile.html',{'user':user,'farmer':farmer})
