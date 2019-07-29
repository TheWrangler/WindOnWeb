from django.urls import path
from WindServer.views_sub import views_fusion
 
urlpatterns = [
    path('',views_fusion.dbs5,name='fusion'),
    path('dbs5/',views_fusion.dbs5,name='dbs5'),
    path('dbs5/<fusion>/<station>/update/',views_fusion.dbs5_update,name='dbs5_update'),
    path('dbs5/<fusion>/<station>/<dt>/',views_fusion.dbs5_search,name='dbs5_search'),
    path('dbs5/<fusion>/<station>/<dt>/last/',views_fusion.dbs5_last,name='dbs5_last'),
    path('dbs5/<fusion>/<station>/<dt>/next/',views_fusion.dbs5_next,name='dbs5_next'),
    path('dbs5/<fusion>/<station>/<start_dt>/<end_dt>/auto/',views_fusion.dbs5_auto,name='dbs5_auto'),

    path('profile/',views_fusion.profile,name='profile'),
    path('profile/<fusion>/<station>/update/',views_fusion.profile_update,name='profile_update'),
    path('profile/<fusion>/<station>/<dt>/',views_fusion.profile_search,name='profile_search'),
    path('profile/<fusion>/<station>/<dt>/last/',views_fusion.profile_last,name='profile_last'),
    path('profile/<fusion>/<station>/<dt>/next/',views_fusion.profile_next,name='profile_next'),
    path('profile/<fusion>/<station>/<start_dt>/<end_dt>/auto/',views_fusion.profile_auto,name='profile_auto'),

    path('radio/',views_fusion.radio,name='radio'),
    path('radio/<fusion>/<station>/update/',views_fusion.radio_update,name='radio_update'),
    path('radio/<fusion>/<station>/<dt>/',views_fusion.radio_search,name='radio_search'),
    path('radio/<fusion>/<station>/<dt>/last/',views_fusion.radio_last,name='radio_last'),
    path('radio/<fusion>/<station>/<dt>/next/',views_fusion.radio_next,name='radio_next'),
    path('radio/<fusion>/<station>/<start_dt>/<end_dt>/auto/',views_fusion.radio_auto,name='radio_auto'),
]