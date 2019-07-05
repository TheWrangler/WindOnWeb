from django.contrib import admin
from .models import PPI,PPI_Admin,CAPPI,CAPPI_Admin

# Register your models here.
admin.site.register(PPI,PPI_Admin)
admin.site.register(CAPPI,CAPPI_Admin)
