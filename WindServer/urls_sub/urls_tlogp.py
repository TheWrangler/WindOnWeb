from django.urls import path
from WindServer.views_sub import views_tlogp

urlpatterns = [
    path('',views_tlogp.tlogp,name='tlogp'),
    path('tlogp/',views_tlogp.tlogp,name='tlogp'),
    path('tlogp/<station>/update/',views_tlogp.tlogp_update,name='tlogp_update'),
    path('tlogp/<station>/<dt>/',views_tlogp.tlogp_search,name='tlogp_search'),
    path('tlogp/<station>/<dt>/last/',views_tlogp.tlogp_last,name='tlogp_last'),
    path('tlogp/<station>/<dt>/next/',views_tlogp.tlogp_next,name='tlogp_next'),
    path('tlogp/<station>/<start_dt>/<end_dt>/auto/',views_tlogp.tlogp_auto,name='tlogp_auto'),
]