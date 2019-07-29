 #from django.conf.urls import urls
from django.urls import path,include
from . import views
 
app_name='myapp'
 
urlpatterns = [
    path('index/',include('WindServer.urls_sub.urls_index')),
    path('lidar/',include('WindServer.urls_sub.urls_lidar')),
    path('fusion/',include("WindServer.urls_sub.urls_fusion")),
    
    # path('fusion/',views.fusion_dbs5,name='fusion_dbs5'),
    # path('fusion/dbs5/',views.fusion_dbs5,name='fusion_dbs5'),
    # path('fusion/dbs5/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_dbs5_search,name='fusion_dbs5_search'),
    # path('fusion/profile/',views.fusion_profile,name='fusion_profile'),
    # path('fusion/profile/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_profile_search,name='fusion_profile_search'),
    # path('fusion/radio/',views.fusion_radio,name='fusion_radio'),
    # path('fusion/radio/<fusion>/<station>/<start_dt>/<end_dt>/',views.fusion_radio_search,name='fusion_radio_search'),
    
    path('tlogp/',views.tlogp,name='tlogp'),
    path('tlogp/<station>/<start_dt>/<end_dt>/',views.tlogp_search,name='tlogp_search'),
     ]
