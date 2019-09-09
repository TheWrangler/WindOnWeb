from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from WindServer.models import WindRoseDaily,WindRoseMonth,WindCurveMonth,TempMonth,HumidityMonth

###################################History views#######################################
def history(request):
    return render(request, 'history/history.html')

def windrose_daily(request,products,station,hei,dt):
    product_obj = {}
    product_sum = 0
    if(station == '全站'):
        windrose = WindRoseDaily.objects.filter(hei=hei,date=dt)
    else:
        windrose = WindRoseDaily.objects.filter(station=station,hei=hei,date=dt)
    
    if len(windrose) != 0:
        for wind in windrose:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = wind
            product_sum += 1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '日平均'
    return render(request, 'history/history.html',product_obj)

def history_month(request,products,station,from_dt,to_dt):
    product_obj = {}
    product_sum = 0
    product_list = products.split('+')
    if 'windcurve' in product_list:
        if station == '全站':
            windcurve = WindCurveMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: windcurve = WindCurveMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(windcurve) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = windcurve
            product_sum+=1
    
    if 'temp' in product_list:
        if station == '全站':
            temp = TempMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: temp = TempMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(temp) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = temp
            product_sum+=1

    if 'humidity' in product_list:
        if station == '全站':
            humidity = HumidityMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: humidity = HumidityMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(humidity) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = humidity
            product_sum+=1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '月平均'
    return  render(request, 'history/history.html',product_obj)

def history_month_hei(request,products,station,hei,from_dt,to_dt):
    product_obj = {}
    product_list = products.split('+')
    product_sum = 0

    if 'windrose' in product_list:
        if station == '全站':
            windrose = WindRoseMonth.objects.filter(hei = hei,date_from = from_dt, date_to = to_dt)
        else: windrose = WindRoseMonth.objects.filter(station = station, hei = hei,date_from = from_dt, date_to = to_dt)

        if len(windrose) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = windrose
            product_sum+=1
        
    if 'windcurve' in product_list:
        if station == '全站':
            windcurve = WindCurveMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: windcurve = WindCurveMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(windcurve) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = windcurve
            product_sum+=1
    
    if 'temp' in product_list:
        if station == '全站':
            temp = TempMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: temp = TempMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(temp) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = temp
            product_sum+=1

    if 'humidity' in product_list:
        if station == '全站':
            humidity = HumidityMonth.objects.filter(date_from = from_dt, date_to = to_dt)
        else: humidity = HumidityMonth.objects.filter(station = station, date_from = from_dt, date_to = to_dt)

        if len(humidity) != 0:
            key = 'product_sum_%d' % product_sum
            product_obj[key] = humidity
            product_sum+=1

    product_obj['product_sum'] = len(product_obj)
    product_obj['product_type'] = '月平均'
    return  render(request, 'history/history.html',product_obj)
