from django.conf.urls.defaults import *
import xzjmt.item.views
urlpatterns = patterns('',
    url(r'^$', xzjmt.item.views.list),
    url(r'^(?P<id>\d)/$', xzjmt.item.views.detail),
    
)