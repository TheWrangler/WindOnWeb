from django.db import models
from django.contrib import admin
# Create your models here.

#index data models
class Lidar(models.Model):
    hei = models.IntegerField()
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class Lidar_Admin(admin.ModelAdmin):
    list_display = ('hei','station','date_time','img_src')

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

#fusion data models
class DBS5(models.Model):
    fusion=models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)
    
class Profile(models.Model):
    fusion=models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)
    
class Radio(models.Model):
    fusion=models.CharField(max_length=50)
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)

class Fusion_Admin(admin.ModelAdmin):
    list_display = ('fusion','station','date_time','img_src')    
    
#T-logP model
class TlogP(models.Model):
    station = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    img_src = models.CharField(max_length=250)
    
class TlogP_Admin(admin.ModelAdmin):
    list_display = ('station','date_time','img_src')  

#Lookup models
class WindRoseDaily(models.Model):
    hei = models.IntegerField()
    station = models.CharField(max_length=50)
    date = models.DateField()
    img_src = models.CharField(max_length=250)

class WindRoseDaily_Admin(admin.ModelAdmin):
    list_display = ('hei','station','date','img_src')

class WindRoseMonth(models.Model):
    hei = models.IntegerField()
    station = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    img_src = models.CharField(max_length=250)

class WindRoseMonth_Admin(admin.ModelAdmin):
    list_display = ('hei','station','date_from','date_to','img_src')

class WindCurveMonth(models.Model):
    station = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    img_src = models.CharField(max_length=250)   
    
class WindCurveMonth_Admin(admin.ModelAdmin):
    list_display = ('station','date_from','date_to','img_src')

class TempMonth(models.Model):
    station = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    img_src = models.CharField(max_length=250)   

class TempMonth_Admin(admin.ModelAdmin):
    list_display = ('station','date_from','date_to','img_src')

class HumidityMonth(models.Model):
    station = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField()
    img_src = models.CharField(max_length=250)   

class HumidityMonth_Admin(admin.ModelAdmin):
    list_display = ('station','date_from','date_to','img_src')