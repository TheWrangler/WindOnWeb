from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import PPI,CAPPI,WINDTHI,RHI

###################################ppi views#######################################
def ppi(request):
    ppis = PPI.objects.filter(ele=0,station='全站').order_by('-date_time')[:4]
    ppis = ppis[::-1]
    tlabels = PPI.objects.filter(ele=0,station='全站').order_by('-date_time').values("date_time").distinct()
    return render(request, 'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})

def ppi_update(request,ele,station):
    ppis = PPI.objects.filter(ele=ele,station=station).order_by('-date_time')[:4]
    ppis = ppis[::-1]
    tlabels = PPI.objects.filter(ele=ele,station=station).order_by('-date_time').values("date_time")
    return render(request, 'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})

def ppi_search(request,ele,station,dt):
    ppis = PPI.objects.filter(ele=ele,station=station,date_time__gte = dt).order_by('date_time')[:4]
    tlabels = PPI.objects.filter(ele=ele,station=station).order_by('-date_time').values("date_time")
    return render(request, 'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})

def ppi_last(request,ele,station,dt):
    ppis = PPI.objects.filter(ele=ele,station=station,date_time__lt = dt).order_by('-date_time')[:4]
    ppis = ppis[::-1]
    tlabels = PPI.objects.filter(ele=ele,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})

def ppi_next(request,ele,station,dt):
    ppis = PPI.objects.filter(ele=ele,station=station,date_time__gt = dt).order_by('date_time')[:4]
    tlabels = PPI.objects.filter(ele=ele,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})
    
def ppi_auto(request,ele,station,start_dt,end_dt):
    ppis = PPI.objects.filter(ele=ele,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
    tlabels = PPI.objects.filter(ele=ele,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/ppi.html',{'ppis':ppis,'tlabels':tlabels})
###################################################################################


###################################cappi views#######################################
def cappi(request):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        cappi = CAPPI.objects.filter(hei=100,station=city).order_by('-date_time')[:1]
        if len(cappi) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = cappi
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    tlabels = CAPPI.objects.filter(hei=100).order_by('-date_time').values("date_time").distinct()
    product_obj['tlabels'] = tlabels
    return render(request, 'lidar/cappi.html',product_obj)

def cappi_update(request,hei,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            cappi = CAPPI.objects.filter(hei=hei,station=city).order_by('-date_time')[:1]
            if len(cappi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = cappi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = CAPPI.objects.filter(hei=hei).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/cappi.html',product_obj)
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time')[:4]
        cappis = cappis[::-1]
        tlabels = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time').values("date_time")
        return render(request, 'lidar/cappi.html',{'cappis':cappis,'product_type':'单站','tlabels':tlabels})

def cappi_search(request,hei,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            cappi = CAPPI.objects.filter(hei=hei,station=city,date_time__gte = dt).order_by('date_time')[:1]
            if len(cappi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = cappi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = CAPPI.objects.filter(hei=hei).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/cappi.html',product_obj)
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gte = dt).order_by('date_time')[:4]
        tlabels = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time').values("date_time")
        return render(request, 'lidar/cappi.html',{'cappis':cappis,'product_type':'单站','tlabels':tlabels})

def cappi_last(request,hei,station,dt):
    tlabels = []
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = CAPPI.objects.filter(hei=hei).order_by('-date_time').values("date_time").distinct()
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time').values("date_time")
    cappis = cappis[::-1]
    return render(request,'lidar/cappi.html',{'cappis':cappis,'tlabels':tlabels})

def cappi_next(request,hei,station,dt):
    tlabels = []
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = CAPPI.objects.filter(hei=hei).order_by('-date_time').values("date_time").distinct()
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/cappi.html',{'cappis':cappis,'tlabels':tlabels})
    
def cappi_auto(request,hei,station,start_dt,end_dt):
    tlabels = []
    if station == '全站':
        cappis = CAPPI.objects.filter(hei=hei,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = CAPPI.objects.filter(hei=hei).order_by('-date_time').values("date_time").distinct()
    else:
        cappis = CAPPI.objects.filter(hei=hei,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = CAPPI.objects.filter(hei=hei,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/cappi.html',{'cappis':cappis,'tlabels':tlabels})
###################################################################################

###################################windthi views#######################################
def windthi(request):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        windthi = WINDTHI.objects.filter(direction='水平风',station=city).order_by('-date_time')[:1]
        if len(windthi) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = windthi
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    tlabels = WINDTHI.objects.filter(direction='水平风').order_by('-date_time').values("date_time").distinct()
    product_obj['tlabels'] = tlabels
    return render(request, 'lidar/wind_thi.html',product_obj)

def windthi_update(request,direction,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            windthi = WINDTHI.objects.filter(direction=direction,station=city).order_by('-date_time')[:1]
            if len(windthi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = windthi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = WINDTHI.objects.filter(direction=direction).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/wind_thi.html',product_obj)
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time')[:4]
        windthis = windthis[::-1]
        tlabels = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time').values("date_time")
        return render(request, 'lidar/wind_thi.html',{'windthis':windthis,'product_type':'单站','tlabels':tlabels})

def windthi_search(request,direction,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            windthi = WINDTHI.objects.filter(direction=direction,station=city,date_time=dt).order_by('date_time')[:1]
            if len(windthi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = windthi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = WINDTHI.objects.filter(direction=direction).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/wind_thi.html',product_obj)
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time=dt).order_by('date_time')[:4]
        tlabels = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time').values("date_time")
        return render(request, 'lidar/wind_thi.html',{'windthis':windthis,'product_type':'单站','tlabels':tlabels})

def windthi_last(request,direction,station,dt):
    tlabels = []
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = WINDTHI.objects.filter(direction=direction).order_by('-date_time').values("date_time").distinct()
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time').values("date_time")
    windthis = windthis[::-1]
    return render(request,'lidar/wind_thi.html',{'windthis':windthis,'tlabels':tlabels})

def windthi_next(request,direction,station,dt):
    tlabels = []
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = WINDTHI.objects.filter(direction=direction).order_by('-date_time').values("date_time").distinct()
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/wind_thi.html',{'windthis':windthis,'tlabels':tlabels})
    
def windthi_auto(request,direction,station,start_dt,end_dt):
    tlabels = []
    if station == '全站':
        windthis = WINDTHI.objects.filter(direction=direction,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = WINDTHI.objects.filter(direction=direction).order_by('-date_time').values("date_time").distinct()
    else:
        windthis = WINDTHI.objects.filter(direction=direction,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = WINDTHI.objects.filter(direction=direction,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/wind_thi.html',{'windthis':windthis,'tlabels':tlabels})
###################################################################################

###################################rhi views#######################################
def rhi(request):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    for city in citys:
        rhi = RHI.objects.filter(azi='0',station=city).order_by('-date_time')[:1]
        if len(rhi) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = rhi
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '全站'
    tlabels = RHI.objects.filter(azi='0').order_by('-date_time').values("date_time").distinct()
    product_obj['tlabels'] = tlabels
    return render(request, 'lidar/rhi.html',product_obj)

def rhi_update(request,azi,station):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            rhi = RHI.objects.filter(azi=azi,station=city).order_by('-date_time')[:1]
            if len(rhi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = rhi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = RHI.objects.filter(azi=azi).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/rhi.html',product_obj)
    else:
        rhis = RHI.objects.filter(azi=azi,station=station).order_by('-date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi,station=station).order_by('-date_time').values("date_time")
        rhis = rhis[::-1]
        return render(request, 'lidar/rhi.html',{'rhis':rhis,'product_type':'单站','tlabels':tlabels})

def rhi_search(request,azi,station,dt):
    product_obj = {}
    product_sum = 0
    citys = ['翔安','湖里','集美','海沧','同安']
    if(station == '全站'):
        for city in citys:
            rhi = RHI.objects.filter(azi=azi,station=city,date_time=dt).order_by('date_time')[:1]
            if len(rhi) != 0:
                key = 'product_sum_%d' % product_sum
                product_obj[key] = rhi
                product_sum += 1

        product_obj['product_sum'] = len(product_obj)
        product_obj['product_type'] = '全站'
        tlabels = RHI.objects.filter(azi=azi).order_by('-date_time').values("date_time").distinct()
        product_obj['tlabels'] = tlabels
        return render(request, 'lidar/rhi.html',product_obj)
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time=dt).order_by('date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi,station=station).order_by('-date_time').values("date_time")
        return render(request, 'lidar/rhi.html',{'rhis':rhis,'product_type':'单站','tlabels':tlabels})

def rhi_last(request,azi,station,dt):
    tlabels = []
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi).order_by('-date_time').values("date_time").distinct()
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__lt = dt).order_by('-date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi,station=station).order_by('-date_time').values("date_time")
    rhis = rhis[::-1]
    return render(request,'lidar/rhi.html',{'rhis':rhis,'tlabels':tlabels})

def rhi_next(request,azi,station,dt):
    tlabels = []
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi).order_by('-date_time').values("date_time").distinct()
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__gt = dt).order_by('date_time')[:4]
        tlabels = RHI.objects.filter(azi=azi,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/rhi.html',{'rhis':rhis,'tlabels':tlabels})
    
def rhi_auto(request,azi,station,start_dt,end_dt):
    tlabels = []
    if station == '全站':
        rhis = RHI.objects.filter(azi=azi,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = RHI.objects.filter(azi=azi).order_by('-date_time').values("date_time").distinct()
    else:
        rhis = RHI.objects.filter(azi=azi,station=station,date_time__gt=start_dt,date_time__lt=end_dt).order_by('date_time')[:1]
        tlabels = RHI.objects.filter(azi=azi,station=station).order_by('-date_time').values("date_time")
    return render(request,'lidar/rhi.html',{'rhis':rhis,'tlabels':tlabels})
###################################################################################