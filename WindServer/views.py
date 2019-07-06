from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import PPI,CAPPI,WINDTHI,RHI
# Create your views here.

def index(request):
    return render(request, 'index.html')

# lidar Views
def lidar_ppi(request):
    return render(request, 'lidar\ppi.html')

def lidar_ppi_search(request,ele,station,start_dt,end_dt):
    ppi = PPI.objects.get(ele=ele,station=station)
    return render(request,'lidar\ppi.html',{'ppi':ppi})

def lidar_cappi(request):
    return render(request, 'lidar\cappi.html')

def lidar_cappi_search(request,hei,station,start_dt,end_dt):
    cappi = CAPPI.objects.get(hei=hei,station=station)
    return render(request,'lidar\cappi.html',{'cappi':cappi})

def lidar_wind_thi(request):
    return render(request, 'lidar\wind_thi.html')

def lidar_wind_thi_search(request,direction,station,start_dt,end_dt):
    windthis = WINDTHI.objects.filter(direction=direction,station=station)
    return render(request, 'lidar\wind_thi.html',{'windthis':windthis})

def lidar_rhi(request):
    return render(request, r'lidar\rhi.html')

def lidar_rhi_search(request,azi,station,start_dt,end_dt):
    rhi = RHI.objects.get(azi=azi,station=station)
    return render(request, r'lidar\rhi.html',{'rhi':rhi})