# coding=utf-8
from django.contrib import admin
from django.db import models

class Collection(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    email = models.CharField('邮箱',max_length=150, blank=True)
    nick_name = models.CharField('昵称',max_length=150, blank=True)
    item_id = models.IntegerField('闲置Id')
    create_date = models.DateTimeField('创建日期',null=True, blank=True)
    class Meta:
        db_table = u'xz_user_collection'
        
class CollectionAdmin(admin.ModelAdmin):  
    list_display = ('email','nick_name','item_id','create_date')
    
admin.site.register(Collection, CollectionAdmin)        
