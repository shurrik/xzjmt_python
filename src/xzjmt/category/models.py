# coding=utf-8
from django.db import models
from django.contrib import admin

class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_name = models.CharField('名称', max_length=150, blank=True)
    cat_order = models.IntegerField('顺序', null=True, blank=True)
    class Meta:
        db_table = u'xz_category'
    def __unicode__(self):
        return self.cat_name

class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('cat_name', 'cat_order')
    
admin.site.register(Category, CategoryAdmin)    
