from django.urls import path
from WindServer.views_sub import views_history

urlpatterns = [
    path('',views_history.history,name='history'),

    path('daily/<products>/<station>/<dt>/<hei>/',views_history.windrose_daily,name='windrose_daily'),
    path('month/<products>/<station>/<from_dt>/<to_dt>/',views_history.history_month,name='history_month'),
    path('month/<products>/<station>/<from_dt>/<to_dt>/<hei>/',views_history.history_month_hei,name='history_month_hei'),  
]