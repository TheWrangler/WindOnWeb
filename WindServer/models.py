from django.db import models
from django.contrib import admin
# Create your models here.

#lidar data models
class PPI(models.Model):
    ele = models.IntegerField()
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class PPI_Admin(admin.ModelAdmin):
    list_display = ('ele','station','date_time','img_src')

class CAPPI(models.Model):
    hei = models.IntegerField()
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class CAPPI_Admin(admin.ModelAdmin):
    list_display = ('hei','station','date_time','img_src')

class WINDTHI(models.Model):
    direction = models.CharField(max_length=10)
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class WINDTHI_Admin(admin.ModelAdmin):
    list_display = ('direction','station','date_time','img_src')

class RHI(models.Model):
    azi = models.IntegerField()
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class RHI_Admin(admin.ModelAdmin):
    list_display = ('azi','station','date_time','img_src')
