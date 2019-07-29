from django.urls import path
from WindServer.views_sub import views_lidar
 
urlpatterns = [
    path('',views_lidar.ppi,name='ppi'),
    path('ppi/',views_lidar.ppi,name='ppi'),
    path('ppi/<ele>/<station>/update/',views_lidar.ppi_update,name='ppi_update'),
    path('ppi/<ele>/<station>/<dt>/',views_lidar.ppi_search,name='ppi_search'),
    path('ppi/<ele>/<station>/<dt>/last/',views_lidar.ppi_last,name='ppi_last'),
    path('ppi/<ele>/<station>/<dt>/next/',views_lidar.ppi_next,name='ppi_next'),
    path('ppi/<ele>/<station>/<start_dt>/<end_dt>/auto/',views_lidar.ppi_auto,name='ppi_auto'),

    path('cappi/',views_lidar.cappi,name='cappi'),
    path('cappi/<hei>/<station>/update/',views_lidar.cappi_update,name='cappi_update'),
    path('cappi/<hei>/<station>/<dt>/',views_lidar.cappi_search,name='cappi_search'),
    path('cappi/<hei>/<station>/<dt>/last/',views_lidar.cappi_last,name='cappi_last'),
    path('cappi/<hei>/<station>/<dt>/next/',views_lidar.cappi_next,name='cappi_next'),
    path('cappi/<hei>/<station>/<start_dt>/<end_dt>/auto/',views_lidar.cappi_auto,name='cappi_auto'),

    path('wind_thi/',views_lidar.windthi,name='windthi'),
    path('wind_thi/<direction>/<station>/update/',views_lidar.windthi_update,name='windthi_update'),
    path('wind_thi/<direction>/<station>/<dt>/',views_lidar.windthi_search,name='windthi_search'),
    path('wind_thi/<direction>/<station>/<dt>/last/',views_lidar.windthi_last,name='windthi_last'),
    path('wind_thi/<direction>/<station>/<dt>/next/',views_lidar.windthi_next,name='windthi_next'),
    path('wind_thi/<direction>/<station>/<start_dt>/<end_dt>/auto/',views_lidar.windthi_auto,name='windthi_auto'),

    path('rhi/',views_lidar.rhi,name='rhi'),
    path('rhi/<azi>/<station>/update/',views_lidar.rhi_update,name='rhi_update'),
    path('rhi/<azi>/<station>/<dt>/',views_lidar.rhi_search,name='rhi_search'),
    path('rhi/<azi>/<station>/<dt>/last/',views_lidar.rhi_last,name='rhi_last'),
    path('rhi/<azi>/<station>/<dt>/next/',views_lidar.rhi_next,name='rhi_next'),
    path('rhi/<azi>/<station>/<start_dt>/<end_dt>/auto/',views_lidar.rhi_auto,name='rhi_auto'),
]