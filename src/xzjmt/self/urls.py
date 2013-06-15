from django.conf.urls.defaults import *
import xzjmt.self.views
urlpatterns = patterns('',
    url(r'^$', xzjmt.self.views.index),
)