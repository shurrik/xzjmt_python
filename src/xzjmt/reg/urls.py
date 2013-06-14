from django.conf.urls.defaults import *
import xzjmt.reg.views
urlpatterns = patterns('',
    url(r'^$', xzjmt.reg.views.reg),
    url(r'^save$', xzjmt.reg.views.save),
)