from django.urls import path
from WindServer.views_sub import views_index
 
urlpatterns = [
    path('',views_index.lidar,name='lidar'),
    path('lidar/',views_index.lidar,name='lidar'),
    path('lidar/<hei>/<station>/update/',views_index.lidar_update,name='lidar_update'),
    path('lidar/<hei>/<station>/<dt>/',views_index.lidar_search,name='lidar_search'),
    path('lidar/<hei>/<station>/<dt>/last/',views_index.lidar_last,name='lidar_last'),
    path('lidar/<hei>/<station>/<dt>/next/',views_index.lidar_next,name='lidar_next'),
    path('lidar/<hei>/<station>/<start_dt>/<end_dt>/auto/',views_index.lidar_auto,name='lidar_auto'),
]