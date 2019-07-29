 #from django.conf.urls import urls
from django.urls import path,include
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('index/',include('WindServer.urls_sub.urls_index')),
    path('lidar/',include('WindServer.urls_sub.urls_lidar')),
    path('fusion/',include("WindServer.urls_sub.urls_fusion")),
    path('tlogp/',include("WindServer.urls_sub.urls_tlogp")),
     ]
