from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def service(request):
    return render(request, 'service/service.html')

def about(request):
    return render(request, 'about/about.html')

