# coding=utf-8
from django.contrib import admin
from django.db import models

class ItemPic(models.Model):
    id = models.IntegerField(primary_key=True)
    itemid = models.IntegerField('闲置Id',db_column='itemId') # Field name made lowercase.
    pic_url = models.CharField('图地址',max_length=600, blank=True)
    pic_url_small = models.CharField('小图地址',max_length=600, blank=True)
    create_date = models.DateTimeField('创建日期',null=True, blank=True)
    class Meta:
        db_table = u'xz_item_pic'
        
class ItemPicAdmin(admin.ModelAdmin):  
    list_display = ('itemid','pic_url','create_date')
    
admin.site.register(ItemPic, ItemPicAdmin)        
