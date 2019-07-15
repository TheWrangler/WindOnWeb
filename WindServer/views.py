from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Lidar
from .models import PPI,CAPPI,WINDTHI,RHI
from .models import DBS5,Profile,Radio
from .models import TlogP
# Create your views here.

# index views
def index_lidar(request):
    lidars = Lidar.objects.filter().order_by('-id')[:4]
    cur_lidar = lidars[0]
    return render(request, 'index\lidar.html',{'lidars':lidars,'cur_lidar':cur_lidar})

# lidar Views
def lidar_ppi(request):
    return render(request, 'lidar\ppi.html')

def lidar_ppi_search(request,ele,station,start_dt,end_dt):
    if station == '全站':
        ppis = PPI.objects.filter(ele=ele)
        return render(request,'lidar\ppi.html',{'ppis':ppis})
    else:
        ppis = PPI.objects.filter(ele=ele,station=station)
        return render(request,'lidar\ppi.html',{'ppis':ppis})

def lidar_cappi(request):
    return render(request, 'lidar\cappi.html')

def lidar_cappi_search(request,hei,station,start_dt,end_dt):
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei)
        return render(request,'lidar\cappi.html',{'cappis':cappis})
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station)
        return render(request,'lidar\cappi.html',{'cappis':cappis})

def lidar_wind_thi(request):
    return render(request, 'lidar\wind_thi.html')

def lidar_wind_thi_search(request,direction,station,start_dt,end_dt):
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction)
        return render(request, 'lidar\wind_thi.html',{'windthis':windthis})
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station)
        return render(request, 'lidar\wind_thi.html',{'windthis':windthis})

def lidar_rhi(request):
    return render(request, r'lidar\rhi.html')

def lidar_rhi_search(request,azi,station,start_dt,end_dt):
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi)
        return render(request, r'lidar\rhi.html',{'rhis':rhis})
    else:
        rhis = RHI.objects.filter(azi=azi,station=station)
        return render(request, r'lidar\rhi.html',{'rhis':rhis})


# fusion views
def fusion_dbs5(request):
    return render(request, r'fusion\dbs5.html')

def fusion_dbs5_search(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion)
        return render(request,r'fusion\dbs5.html',{'dbs5s':dbs5s})
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station)
        return render(request,r'fusion\dbs5.html',{'dbs5s':dbs5s})

def fusion_profile(request):
    return render(request, r'fusion\profile.html')

def fusion_profile_search(request,fusion,station,start_dt,end_dt):
    if station == '全站': 
        profiles = Profile.objects.filter(fusion=fusion)
        return render(request,r'fusion\profile.html',{'profiles':profiles})
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station)
        return render(request,r'fusion\profile.html',{'profiles':profiles})

def fusion_radio(request):
    return render(request, r'fusion\radio.html')

def fusion_radio_search(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion)
        return render(request,r'fusion\radio.html',{'radios':radios})
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station)
        return render(request,r'fusion\radio.html',{'radios':radios})

#T-logP views
def tlogp(request):
    return render(request, r'tlogp\tlogp.html')

def tlogp_search(request,station,start_dt,end_dt):
    if station == '全站':
        tlogps = TlogP.objects.filter()
        return render(request,r'tlogp\tlogp.html',{'tlogps':tlogps})
    else:
        tlogps = TlogP.objects.filter(station=station)
        return render(request,r'tlogp\tlogp.html',{'tlogps':tlogps})