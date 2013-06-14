# coding=utf-8
from django.contrib import admin
from django.db import models

class Message(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField('标题',max_length=150, blank=True)
    content = models.CharField('内容',max_length=2400, blank=True)
    sender = models.IntegerField('发送者Id',null=True, blank=True)
    receiver = models.IntegerField('接受者Id')
    sender_email = models.CharField('发送者邮箱',max_length=150, blank=True)
    receiver_email = models.CharField('接受者邮箱',max_length=150, blank=True)
    sender_name = models.CharField('发送者昵称',max_length=150, blank=True)
    receiver_name = models.CharField('接受者昵称',max_length=150, blank=True)
    create_date = models.DateTimeField('创建日期',null=True, blank=True)
    read_date = models.DateTimeField('阅读日期',null=True, blank=True)
    read_flag = models.IntegerField('是否已读',null=True, blank=True)
    class Meta:
        db_table = u'xz_message'
        
class MessageAdmin(admin.ModelAdmin):  
    list_display = ('title','sender_name','receiver_name','create_date','read_date','read_flag')
    
admin.site.register(Message, MessageAdmin)        
