from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import PPI,CAPPI,WINDTHI,RHI

###################################ppi views#######################################
def ppi(request):
    ppis = PPI.objects.order_by('-date_time')[:4]
    ppis = ppis[::-1]
    return render(request, 'lidar/ppi.html',{'ppis':ppis})

def ppi_update(request,ele,station):
    if(station == '全站'):
        ppis = PPI.objects.filter(ele=ele).order_by('-date_time')[:4]
    else:
        ppis = PPI.objects.filter(ele=ele,station=station).order_by('-date_time')[:4]
    ppis = ppis[::-1]
    return render(request, 'lidar/ppi.html',{'ppis':ppis})

def ppi_search(request,ele,station,dt):
    if(station == '全站'):
        ppis = PPI.objects.filter(ele=ele,date_time__gte = dt).order_by('date_time')[:4]
    else:
        ppis = PPI.objects.filter(ele=ele,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'lidar/ppi.html',{'ppis':ppis})

def ppi_last(request,ele,station,dt):
    if station == '全站':
        ppis = PPI.objects.filter(ele=ele,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        ppis = PPI.objects.filter(ele=ele,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    ppis = ppis[::-1]
    return render(request,'lidar/ppi.html',{'ppis':ppis})

def ppi_next(request,ele,station,dt):
    if station == '全站':
        ppis = PPI.objects.filter(ele=ele,date_time__gt = dt).order_by('date_time')[:4]
    else:
        ppis = PPI.objects.filter(ele=ele,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'lidar/ppi.html',{'ppis':ppis})
    
def ppi_auto(request,ele,station,start_dt,end_dt):
    if station == '全站':
        ppis = PPI.objects.filter(ele=ele,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        ppis = PPI.objects.filter(ele=ele,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'lidar/ppi.html',{'ppis':ppis})
###################################################################################


###################################cappi views#######################################
def cappi(request):
    cappis = CAPPI.objects.order_by('-date_time')[:4]
    cappis = cappis[::-1]
    return render(request, 'lidar/cappi.html',{'cappis':cappis})

def cappi_update(request,hei,station):
    if(station == '全站'):
        cappis = CAPPI.objects.filter(hei=hei).order_by('-date_time')[:4]
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time')[:4]
    cappis = cappis[::-1]
    return render(request, 'lidar/cappi.html',{'cappis':cappis})

def cappi_search(request,hei,station,dt):
    if(station == '全站'):
        cappis = CAPPI.objects.filter(hei=hei,date_time__gte = dt).order_by('date_time')[:4]
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'lidar/cappi.html',{'cappis':cappis})

def cappi_last(request,hei,station,dt):
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    cappis = cappis[::-1]
    return render(request,'lidar/cappi.html',{'cappis':cappis})

def cappi_next(request,hei,station,dt):
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__gt = dt).order_by('date_time')[:4]
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'lidar/cappi.html',{'cappis':cappis})
    
def cappi_auto(request,hei,station,start_dt,end_dt):
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'lidar/cappi.html',{'cappis':cappis})
###################################################################################

###################################windthi views#######################################
def windthi(request):
    windthis = WINDTHI.objects.order_by('-date_time')[:4]
    windthis = windthis[::-1]
    return render(request, 'lidar/wind_thi.html',{'windthis':windthis})

def windthi_update(request,direction,station):
    if(station == '全站'):
        windthis = WINDTHI.objects.filter(direction=direction).order_by('-date_time')[:4]
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time')[:4]
    windthis = windthis[::-1]
    return render(request, 'lidar/wind_thi.html',{'windthis':windthis})

def windthi_search(request,direction,station,dt):
    if(station == '全站'):
        windthis = WINDTHI.objects.filter(direction=direction,date_time__gte = dt).order_by('date_time')[:4]
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'lidar/wind_thi.html',{'windthis':windthis})

def windthi_last(request,direction,station,dt):
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    windthis = windthis[::-1]
    return render(request,'lidar/wind_thi.html',{'windthis':windthis})

def windthi_next(request,direction,station,dt):
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__gt = dt).order_by('date_time')[:4]
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'lidar/wind_thi.html',{'windthis':windthis})
    
def windthi_auto(request,direction,station,start_dt,end_dt):
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'lidar/wind_thi.html',{'windthis':windthis})
###################################################################################

###################################rhi views#######################################
def rhi(request):
    rhis = RHI.objects.order_by('-date_time')[:4]
    rhis = rhis[::-1]
    return render(request, 'lidar/rhi.html',{'rhis':rhis})

def rhi_update(request,azi,station):
    if(station == '全站'):
        rhis = RHI.objects.filter(azi=azi).order_by('-date_time')[:4]
    else:
        rhis = RHI.objects.filter(azi=azi,station=station).order_by('-date_time')[:4]
    rhis = rhis[::-1]
    return render(request, 'lidar/rhi.html',{'rhis':rhis})

def rhi_search(request,azi,station,dt):
    if(station == '全站'):
        rhis = RHI.objects.filter(azi=azi,date_time__gte = dt).order_by('date_time')[:4]
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'lidar/rhi.html',{'rhis':rhis})

def rhi_last(request,azi,station,dt):
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    rhis = rhis[::-1]
    return render(request,'lidar/rhi.html',{'rhis':rhis})

def rhi_next(request,azi,station,dt):
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__gt = dt).order_by('date_time')[:4]
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'lidar/rhi.html',{'rhis':rhis})
    
def rhi_auto(request,azi,station,start_dt,end_dt):
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'lidar/rhi.html',{'rhis':rhis})
###################################################################################