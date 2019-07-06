 #from django.conf.urls import urls
from django.urls import path
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('index/',views.index,name='index'),
    path('lidar/',views.lidar_ppi,name='lidar_ppi'),
    path('lidar/ppi/',views.lidar_ppi,name='lidar_ppi'),
    path('lidar/ppi/<int:ele>/<station>/<start_dt>/<end_dt>/',views.lidar_ppi_search,name='lidar_ppi_search'),
    path('lidar/cappi/',views.lidar_cappi,name='lidar_cappi'),
    path('lidar/cappi/<int:hei>/<station>/<start_dt>/<end_dt>/',views.lidar_cappi_search,name='lidar_cappi_search'),
    path('lidar/wind_thi/',views.lidar_wind_thi,name='lidar_wind_thi'),
    path('lidar/wind_thi/<direction>/<station>/<start_dt>/<end_dt>/',views.lidar_wind_thi_search,name='lidar_wind_thi_search'),
    path('lidar/rhi/',views.lidar_rhi,name='lidar_rhi'),
    path('lidar/rhi/<int:azi>/<station>/<start_dt>/<end_dt>/',views.lidar_rhi_search,name='lidar_rhi_search'),
     ]
