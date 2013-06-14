# coding=utf-8
from django.contrib import admin
from django.db import models

class Item(models.Model):
    item_id = models.IntegerField('闲置Id',primary_key=True)
    name = models.CharField('闲置名',max_length=300)
    item_desc = models.CharField('闲置描述',max_length=1500, blank=True)
    user_id = models.IntegerField()
    email = models.CharField(max_length=150, blank=True)
    nick_name = models.CharField('昵称',max_length=150, blank=True)
    pic_cover = models.CharField(max_length=600, blank=True)
    cat_id = models.IntegerField(null=True, blank=True)
    cat_name = models.CharField('分类名',max_length=150, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    city_name = models.CharField('城市名',max_length=60, blank=True)
    visited = models.IntegerField('访问数',null=True, blank=True)
    collected = models.IntegerField('收藏数',null=True, blank=True)
    create_date = models.DateTimeField('创建日期',null=True, blank=True)
    update_date = models.DateTimeField('更新日期',null=True, blank=True)
    sold = models.IntegerField('是否出手',null=True, blank=True)
    class Meta:
        db_table = u'xz_item'
        
class ItemAdmin(admin.ModelAdmin):  
    list_display = ('item_id','name','nick_name','cat_name','city_name','visited','collected','create_date','update_date','sold')
    
admin.site.register(Item, ItemAdmin)        
