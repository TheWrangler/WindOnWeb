 #from django.conf.urls import urls
from django.urls import path
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('index/',views.index,name='index'),
    path('lidar/',views.lidar,name='lidar'),
    path('lidar/ppi/<int:ele>/<station>/<start_dt>/<end_dt>/',views.lidar_ppi,name='lidar_ppi'),
     ]
