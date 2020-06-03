from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import csv
from .models import State,District,SubDistrict,Pincode,ACity,bank,branch,ifsc
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

'''
def load(request):
    file = "/Users/emmad/Documents/Mooma/panindia.csv"
    with open(file, 'r') as file:
        reader = csv.reader(file)
        row = [r for r in reader]
    r1=''
    c1=c2=c3=c4=c5=c6=''
    

    for i in range (130001,154798):
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
    
    return render(request, 'home/load.html',{'r1':r1,'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'c6':c6})



def load(request):

    file = "/Users/emmad/Documents/Mooma/banks.csv"
    with open(file, 'r',encoding="utf8") as file:
        reader = csv.reader(file,delimiter=',')
        row = [r for r in reader]

    i = 2
    c1=c2=c3=c4=c5=c6=''
    
    for i in range (70001,72000):
        c1_1 = State.objects.get_or_create(
                            name = row[i][7],
                            )
        c1 = State.objects.filter(name__icontains = row[i][7],)

        c2 = District.objects.get_or_create(
                            name = row[i][6],
                            state = c1[0],
                            )
        c2_1 = District.objects.filter(
                            name__icontains = row[i][6],)
         
        c3 = ACity.objects.get_or_create(
                        name = row[i][5],
                        district = c2_1[0],
                        )
        c3_1 = ACity.objects.filter(name__icontains = row[i][5]) 

        c4 = bank.objects.get_or_create(
                        name = row[i][0],
                        city = c3_1[0],
                        )
        c4_1 = bank.objects.filter(name__icontains = row[i][0]) 

        c5 = branch.objects.get_or_create(
                        name = row[i][2],
                        bank = c4_1[0],
                        )
        c5_1 = branch.objects.filter(name__icontains = row[i][2])          

        c6 = ifsc.objects.get_or_create(
                        name = row[i][1],
                        branch = c5_1[0],
                        )
                        
    return render(request, 'home/load.html',{'c1':c1,'c2':c2,'c3':c2_1,'c4':c4,'c5':c5,'c6':c6})

'''