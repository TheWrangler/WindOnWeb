 #from django.conf.urls import urls
from django.urls import path
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('index/',views.index_lidar,name='index_lidar'),
    path('index/lidar',views.index_lidar,name='index_lidar'),

    path('lidar/',views.lidar_ppi,name='lidar_ppi'),
    path('lidar/ppi/',views.lidar_ppi,name='lidar_ppi'),
    path('lidar/ppi/<int:ele>/<station>/<start_dt>/<end_dt>/',views.lidar_ppi_search,name='lidar_ppi_search'),
    path('lidar/cappi/',views.lidar_cappi,name='lidar_cappi'),
    path('lidar/cappi/<int:hei>/<station>/<start_dt>/<end_dt>/',views.lidar_cappi_search,name='lidar_cappi_search'),
    path('lidar/wind_thi/',views.lidar_wind_thi,name='lidar_wind_thi'),
    path('lidar/wind_thi/<direction>/<station>/<start_dt>/<end_dt>/',views.lidar_wind_thi_search,name='lidar_wind_thi_search'),
    path('lidar/rhi/',views.lidar_rhi,name='lidar_rhi'),
    path('lidar/rhi/<int:azi>/<station>/<start_dt>/<end_dt>/',views.lidar_rhi_search,name='lidar_rhi_search'),
    
    path('fusion/',views.fusion_dbs5,name='fusion_dbs5'),
    path('fusion/dbs5/',views.fusion_dbs5,name='fusion_dbs5'),
    path('fusion/dbs5/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_dbs5_search,name='fusion_dbs5_search'),
    path('fusion/profile/',views.fusion_profile,name='fusion_profile'),
    path('fusion/profile/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_profile_search,name='fusion_profile_search'),
    path('fusion/radio/',views.fusion_radio,name='fusion_radio'),
    path('fusion/radio/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_radio_search,name='fusion_radio_search'),
    
    path('tlogp/',views.tlogp,name='tlogp'),
    path('tlogp/<station>/<start_dt>/<end_dt>/',views.tlogp_search,name='tlogp_search'),
     ]
