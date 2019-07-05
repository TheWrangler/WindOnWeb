from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import PPI,CAPPI
# Create your views here.

def index(request):
    return render(request, 'index.html')

def lidar(request):
    return render(request, 'lidar.html')

def lidar_ppi(request,ele,station,start_dt,end_dt):
    ppi = PPI.objects.get(ele=ele,station=station)
    return render(request,'lidar.html',{'ppi':ppi})

def lidar_cappi(request,hei,station,start_dt,end_dt):
    cappi = CAPPI.objects.get(hei=hei)
    return render(request,'lidar.html',{'cappi':cappi})