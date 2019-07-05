from django.db import models
from django.contrib import admin
# Create your models here.


# # Dev model:sn,caption,comment
# class Dev(models.Model):
#     sn = models.IntegerField()
#     caption = models.CharField(max_length=20)
#     comment = models.CharField(max_length=50)
# 
# # City model:sn,caption
# class City(models.Model):
#     sn = models.IntegerField()
#     caption = models.CharField(max_length=20)
# 
# # ProductCapture model:dev,city,height,date_time,desc,save_path
# class ProductCapture(models.Model):
# 	#if Dev model be deleted,set this field NULL.
#     dev = models.ForeignKey('Dev',null=True,on_delete=models.SET_NULL)
#     #if City model be deleted,set this field NULL.
#     city = models.ForeignKey('City',null=True,on_delete=models.SET_NULL)
#     height = models.IntegerField()
#     date_time = models.DateTimeField()
#     desc = models.CharField(max_length=200)
#     save_path = models.ImageField(null=False,upload_to='upload')

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