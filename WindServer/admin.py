from django.contrib import admin
from .models import Lidar,Lidar_Admin
from .models import PPI,PPI_Admin,CAPPI,CAPPI_Admin,WINDTHI,WINDTHI_Admin,RHI,RHI_Admin
from .models import DBS5,Profile,Radio,Fusion_Admin
from .models import TlogP,TlogP_Admin

# Register your models here.
admin.site.register(Lidar,Lidar_Admin)
admin.site.register(PPI,PPI_Admin)
admin.site.register(CAPPI,CAPPI_Admin)
admin.site.register(WINDTHI,WINDTHI_Admin)
admin.site.register(RHI,RHI_Admin)

admin.site.register(DBS5,Fusion_Admin)
admin.site.register(Profile,Fusion_Admin)
admin.site.register(Radio,Fusion_Admin)

admin.site.register(TlogP,TlogP_Admin)