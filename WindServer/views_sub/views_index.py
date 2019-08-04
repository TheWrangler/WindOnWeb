from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import Lidar

def lidar(request):
    lidars = Lidar.objects.filter(station='全站').order_by('-date_time')[:4]
    lidars = lidars[::-1]
    return render(request, 'index/lidar.html',{'lidars':lidars})

def lidar_update(request,hei,station):
    lidars = Lidar.objects.filter(hei=hei,station=station).order_by('-date_time')[:4]
    lidars = lidars[::-1]
    return render(request,'index/lidar.html',{'lidars':lidars})

def lidar_search(request,hei,station,dt):
    lidars = Lidar.objects.filter(hei=hei,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request,'index/lidar.html',{'lidars':lidars})

def lidar_last(request,hei,station,dt):
    lidars = Lidar.objects.filter(hei=hei,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    lidars = lidars[::-1]
    return render(request,'index/lidar.html',{'lidars':lidars})

def lidar_next(request,hei,station,dt):
    lidars = Lidar.objects.filter(hei=hei,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'index/lidar.html',{'lidars':lidars})
    
def lidar_auto(request,hei,station,start_dt,end_dt):
    lidars = Lidar.objects.filter(hei=hei,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'index/lidar.html',{'lidars':lidars})