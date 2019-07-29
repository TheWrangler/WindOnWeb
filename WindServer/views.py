from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TlogP

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