# coding=utf-8
from django.contrib import admin
from django.db import models

class Follow(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField('关注者Id')
    email = models.CharField('关注者昵称',max_length=150, blank=True)
    nick_name = models.CharField('关注者邮箱',max_length=150, blank=True)
    follow_id = models.IntegerField('被关注者Id')
    follow_email = models.CharField('被关注者邮箱',max_length=150, blank=True)
    follow_name = models.CharField('被关注者昵称',max_length=150, blank=True)
    create_date = models.DateTimeField('创建日期',null=True, blank=True)
    class Meta:
        db_table = u'xz_user_follow'
        
class FollowAdmin(admin.ModelAdmin):  
    list_display = ('email','nick_name','follow_email','follow_name','create_date')
    
admin.site.register(Follow, FollowAdmin)         
