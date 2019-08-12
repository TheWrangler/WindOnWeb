from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import DBS5,Profile,Radio

###################################DBS5 views#######################################
def dbs5(request):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        dbs5 = DBS5.objects.filter(fusion='水平+垂直风',station=city).order_by('-date_time')[:1]
        if len(dbs5) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = dbs5
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    return render(request, 'fusion/dbs5.html',product_obj)

def dbs5_update(request,fusion,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            dbs5 = DBS5.objects.filter(fusion=fusion,station=city).order_by('-date_time')[:1]
            if len(dbs5) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = dbs5
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/dbs5.html',product_obj)
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:3]
        dbs5s = dbs5s[::-1]
        return render(request, 'fusion/dbs5.html',{'dbs5s':dbs5s,'product_type':'单站'})

def dbs5_search(request,fusion,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            dbs5 = DBS5.objects.filter(fusion=fusion,station=city,date_time__gte = dt).order_by('date_time')[:1]
            if len(dbs5) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = dbs5
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/dbs5.html',product_obj)
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:3]
    return render(request, 'fusion/dbs5.html',{'dbs5s':dbs5s,'product_type':'单站'})

def dbs5_last(request,fusion,station,dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:3]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:3]
    dbs5s = dbs5s[::-1]
    return render(request,'fusion/dbs5.html',{'dbs5s':dbs5s})

def dbs5_next(request,fusion,station,dt):
    if station == '全站':
        dbs5s = DBS5.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:3]
    else:
        dbs5s = DBS5.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:3]
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
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        profile = Profile.objects.filter(fusion='激光雷达+风廓线',station=city).order_by('-date_time')[:1]
        if len(profile) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = profile
            product_sum += 1
    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    return render(request, 'fusion/profile.html',product_obj)

def profile_update(request,fusion,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            profile = Profile.objects.filter(fusion=fusion,station=city).order_by('-date_time')[:1]
            if len(profile) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = profile
                product_sum += 1
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/profile.html',product_obj)
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:3]
        profiles = profiles[::-1]
        return render(request, 'fusion/profile.html',{'profiles':profiles,'product_type':'单站'})

def profile_search(request,fusion,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            profile = Profile.objects.filter(fusion=fusion,station=city,date_time__gte = dt).order_by('date_time')[:1]
            if len(profile) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = profile
                product_sum += 1
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/profile.html',product_obj)
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:3]
        return render(request, 'fusion/profile.html',{'profiles':profiles,'product_type':'单站'})

def profile_last(request,fusion,station,dt):
    if station == '全站':
        profiles = Profile.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:3]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:3]
    profiles = profiles[::-1]
    return render(request,'fusion/profile.html',{'profiles':profiles})

def profile_next(request,fusion,station,dt):
    if station == '全站':
        profiles = Profile.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:3]
    else:
        profiles = Profile.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:3]
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
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        radio = Radio.objects.filter(fusion='整层风+温度',station=city).order_by('-date_time')[:1]
        if len(radio) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = radio
            product_sum += 1
    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    return render(request, 'fusion/radio.html',product_obj)

def radio_update(request,fusion,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            radio = Radio.objects.filter(fusion=fusion,station=city).order_by('-date_time')[:1]
            if len(radio) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = radio
                product_sum += 1
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/radio.html',product_obj)
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station).order_by('-date_time')[:3]
        radios = radios[::-1]
        return render(request, 'fusion/radio.html',{'radios':radios,'product_type':'单站'})

def radio_search(request,fusion,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            radio = Radio.objects.filter(fusion=fusion,station=city,date_time__gte = dt).order_by('date_time')[:1]
            if len(radio) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = radio
                product_sum += 1
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        return render(request, 'fusion/radio.html',product_obj)
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gte = dt).order_by('date_time')[:3]
    return render(request, 'fusion/radio.html',{'radios':radios,'product_type':'单站'})

def radio_last(request,fusion,station,dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__lt = dt).order_by('-date_time')[:3]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__lt = dt).order_by('-date_time')[:3]
    radios = radios[::-1]
    return render(request,'fusion/radio.html',{'radios':radios})

def radio_next(request,fusion,station,dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__gt = dt).order_by('date_time')[:3]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gt = dt).order_by('date_time')[:3]
    return render(request,'fusion/radio.html',{'radios':radios})
    
def radio_auto(request,fusion,station,start_dt,end_dt):
    if station == '全站':
        radios = Radio.objects.filter(fusion=fusion,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    else:
        radios = Radio.objects.filter(fusion=fusion,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    return render(request,'fusion/radio.html',{'radios':radios})
###################################################################################