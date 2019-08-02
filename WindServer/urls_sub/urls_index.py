from django.urls import path
from WindServer.views_sub import views_index
 
urlpatterns = [
    path('',views_index.lidar,name='lidar'),
    path('lidars/',views_index.lidar,name='lidar'),
    path('lidars/<hei>/<station>/update/',views_index.lidar_update,name='lidar_update'),
    path('lidars/<hei>/<station>/<dt>/',views_index.lidar_search,name='lidar_search'),
    path('lidars/<hei>/<station>/<dt>/last/',views_index.lidar_last,name='lidar_last'),
    path('lidars/<hei>/<station>/<dt>/next/',views_index.lidar_next,name='lidar_next'),
    path('lidars/<hei>/<station>/<start_dt>/<end_dt>/auto/',views_index.lidar_auto,name='lidar_auto'),
]