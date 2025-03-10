from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import TlogP

###################################TlogP views#######################################
def tlogp(request):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        tlogp = TlogP.objects.filter(station=city).order_by('-date_time')[:1]
        if len(tlogp) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = tlogp
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    tlabels = TlogP.objects.values("date_time").distinct().distinct()
    product_obj['tlabels'] = tlabels
    return render(request, 'tlogp/tlogp.html',product_obj)

def tlogp_update(request,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            tlogp = TlogP.objects.filter(station=city).order_by('-date_time')[:1]
            if len(tlogp) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = tlogp
                product_sum += 1
    
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = TlogP.objects.values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'tlogp/tlogp.html',product_obj)
    else:
        tlogps = TlogP.objects.filter(station=station).order_by('-date_time')[:4]
        tlogps = tlogps[::-1]
        tlabels = TlogP.objects.filter(station=station).values("date_time")
        return render(request, 'tlogp/tlogp.html',{'tlogps':tlogps,'product_type':'单站','tlabels':tlabels})

def tlogp_search(request,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            tlogp = TlogP.objects.filter(station=city,date_time = dt).order_by('date_time')[:1]
            if len(tlogp) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = tlogp
                product_sum += 1
    
        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = TlogP.objects.values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'tlogp/tlogp.html',product_obj)
    else:
        tlogps = TlogP.objects.filter(station=station,date_time = dt).order_by('date_time')[:4]
        tlabels = TlogP.objects.filter(station=station).values("date_time")
        return render(request, 'tlogp/tlogp.html',{'tlogps':tlogps,'product_type':'单站','tlabels':tlabels})

def tlogp_last(request,station,dt):
    tlabels = []
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = TlogP.objects.values("date_time").distinct()
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = TlogP.objects.filter(station=station).values("date_time")
    tlogps = tlogps[::-1]
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps,'tlabels':tlabels})

def tlogp_next(request,station,dt):
    tlabels = []
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__gt = dt).order_by('date_time')[:4]
        tlabels = TlogP.objects.values("date_time").distinct()
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = TlogP.objects.filter(station=station).values("date_time")
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps,'tlabels':tlabels})
    
def tlogp_auto(request,station,start_dt,end_dt):
    tlabels = []
    if station == '全站':
        tlogps = TlogP.objects.filter(date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = TlogP.objects.values("date_time").distinct()
    else:
        tlogps = TlogP.objects.filter(station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = TlogP.objects.filter(station=station).values("date_time")
    return render(request,'tlogp/tlogp.html',{'tlogps':tlogps,'tlabels':tlabels})
###################################################################################