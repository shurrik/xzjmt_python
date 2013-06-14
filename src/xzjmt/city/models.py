# coding=utf-8
from django.db import models
from django.contrib import admin

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField('城市名',max_length=60, blank=True)
    ip_name = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = u'xz_city'
    def __unicode__(self):
        return self.city_name        
        
class CityAdmin(admin.ModelAdmin):  
    list_display = ('city_name',)
    
admin.site.register(City, CityAdmin)        
