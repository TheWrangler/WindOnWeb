from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import DBS5,Profile,Radio

###################################DBS5 views#######################################
def dbs5(request):
    dbs5s = DBS5.objects.order_by('-date_time')[:4]
    dbs5s = dbs5s[::-1]
    return render(request, 'fusion/dbs5.html',{'dbs5s':dbs5s})

def dbs5_update(request,fusion,station):
    if(station == '全站'):
        dbs5s = DBS5.objects.filter(fusion=fusion).order_by('-date_time')[:4]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:4]
    dbs5s = dbs5s[::-1]
    return render(request, 'fusion/dbs5.html',{'dbs5s':dbs5s})

def dbs5_search(request,fusion,station,dt):
    if(station == '全站'):
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__gte = dt).order_by('date_time')[:4]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'fusion/dbs5.html',{'dbs5s':dbs5s})

def dbs5_last(request,fusion,station,dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    dbs5s = dbs5s[::-1]
    return render(request,'fusion/dbs5.html',{'dbs5s':dbs5s})

def dbs5_next(request,fusion,station,dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:4]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'fusion/dbs5.html',{'dbs5s':dbs5s})
    
def dbs5_auto(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'fusion/dbs5.html',{'dbs5s':dbs5s})
###################################################################################

###################################Profile views#######################################
def profile(request):
    profiles = Profile.objects.order_by('-date_time')[:4]
    profiles = profiles[::-1]
    return render(request, 'fusion/profile.html',{'profiles':profiles})

def profile_update(request,fusion,station):
    if(station == '全站'):
        profiles = Profile.objects.filter(fusion=fusion).order_by('-date_time')[:4]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:4]
    profiles = profiles[::-1]
    return render(request, 'fusion/profile.html',{'profiles':profiles})

def profile_search(request,fusion,station,dt):
    if(station == '全站'):
        profiles = Profile.objects.filter(fusion=fusion,date_time__gte = dt).order_by('date_time')[:4]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'fusion/profile.html',{'profiles':profiles})

def profile_last(request,fusion,station,dt):
    if station == '全站':
        profiles = Profile.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    profiles = profiles[::-1]
    return render(request,'fusion/profile.html',{'profiles':profiles})

def profile_next(request,fusion,station,dt):
    if station == '全站':
        profiles = Profile.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:4]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'fusion/profile.html',{'profiles':profiles})
    
def profile_auto(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        profiles = Profile.objects.filter(fusion=fusion,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'fusion/profile.html',{'profiles':profiles})
###################################################################################

###################################Radio views#######################################
def radio(request):
    radios = Radio.objects.order_by('-date_time')[:4]
    radios = radios[::-1]
    return render(request, 'fusion/radio.html',{'radios':radios})

def radio_update(request,fusion,station):
    if(station == '全站'):
        radios = Radio.objects.filter(fusion=fusion).order_by('-date_time')[:4]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:4]
    radios = radios[::-1]
    return render(request, 'fusion/radio.html',{'radios':radios})

def radio_search(request,fusion,station,dt):
    if(station == '全站'):
        radios = Radio.objects.filter(fusion=fusion,date_time__gte = dt).order_by('date_time')[:4]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:4]
    return render(request, 'fusion/radio.html',{'radios':radios})

def radio_last(request,fusion,station,dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:4]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    radios = radios[::-1]
    return render(request,'fusion/radio.html',{'radios':radios})

def radio_next(request,fusion,station,dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:4]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:4]
    return render(request,'fusion/radio.html',{'radios':radios})
    
def radio_auto(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'fusion/radio.html',{'radios':radios})
###################################################################################