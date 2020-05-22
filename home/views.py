from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import csv
from .models import State,District,SubDistrict,Pincode
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

'''
def load(request):
    file = "/Users/emmad/Documents/Mooma/MooMaWebsite/MooMa/home/panindia.csv"
    with open(file, 'r') as file:
        reader = csv.reader(file)
        row = [r for r in reader]
    r1=''
    c1=c2=c3=c4=''
    i=39

    for i in range (1,2):
        print(row[i])
        c1 = State.objects.get_or_create(
                        name = row[i][9],
                        )
        c1_1 = State.objects.get(name=row[i][9])
        #c3 = c1.id
        c2 = District.objects.get_or_create(
                        name = row[i][8],
                        state = c1_1,
                        )
        c2_1 = District.objects.get(name = row[i][8])               
        c3 = SubDistrict.objects.get_or_create(
                        name = row[i][7],
                        district = c2_1,
                        )
        c3_1 = SubDistrict.objects.filter(name = row[i][7]) 
        c4 = Pincode.objects.get_or_create(
                        name = row[i][1],
                        subdistrict = c3_1[0],
                        )
    
    return render(request, 'home/load.html',{'r1':r1,'c1':c1,'c2':c2,'c3':c3,'c4':c4})

'''
    
