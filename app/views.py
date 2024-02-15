from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
import csv

# Create your views here.

def bank_details(self):
    with open('C:\\Users\\USER\\OneDrive\\Desktop\\django projects\\Akhil\\Scripts\\project38\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BN=Bank(bank_name=bn)
            BN.save()

    return HttpResponse('Bank data is Uploaded successfully......')

def branch_details(self):
    with open('C:\\Users\\USER\\OneDrive\\Desktop\\django projects\\Akhil\\Scripts\\project38\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifs=i[1]
                br=i[2]
                ad=i[3]
                co=i[4]
                c=i[5]
                di=i[6]
                st=i[7]
                BRO=Branch(bank_name=BO[0],ifsc=ifs,branch=br,address=ad,contact=co,city=c,district=di,state=st)    
                BRO.save()
    return HttpResponse('Branch data is Uploaded succesfully.....')


              