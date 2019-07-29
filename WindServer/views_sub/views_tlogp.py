from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import TlogP

###################################TlogP views#######################################
def tlogp(request):
    tlogps = TlogP.objects.order_by('-date_time')[:4]
    tlogps = tlogps[::-1]
    return render(request, 'tlogp/tlogp.html',{'tlogps':tlogps})

def tlogp_update(request,station):
    if(station == '全站'):
        tlogps = TlogP.objects.order_by('-date_time')[:4]
    else:
        tlogps = TlogP.objects.filter(station=station).order_by('-date_time')[:4]
    tlogps = tlogps[::-1]
    return render(request, 'tlogp/tlogp.html',{'tlogps':tlogps})

def tlogp_search(request,station,dt):
    if(station == '全站'):
        tlogps = TlogP.objects.filter(date_time__gte = dt).order_by('date_time')[:4]
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'tlogp/tlogp.html',{'tlogps':tlogps})

def tlogp_last(request,station,dt):
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__lt = dt).order_by('-date_time')[:4]
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__lt = dt).order_by('-date_time')[:4]
    tlogps = tlogps[::-1]
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps})

def tlogp_next(request,station,dt):
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__gt = dt).order_by('date_time')[:4]
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps})
    
def tlogp_auto(request,station,start_dt,end_dt):
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps})
###################################################################################