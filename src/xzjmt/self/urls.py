from django.conf.urls.defaults import *
import xzjmt.self.views
urlpatterns = patterns('',
    url(r'^$', xzjmt.self.views.index),
    url(r'^item/new$', xzjmt.self.views.newItem),
    url(r'^item/list$', xzjmt.self.views.listItem),
    url(r'^item/del/(?P<id>\d)$', xzjmt.self.views.delItem),
    url(r'^item/add$', xzjmt.self.views.addItem),
    url(r'^profile$', xzjmt.self.views.profile),
    url(r'^save$', xzjmt.self.views.save),
    url(r'^message/write/(?P<id>\d)$', xzjmt.self.views.write),
    url(r'^message/send$', xzjmt.self.views.send),
    url(r'^message/list$', xzjmt.self.views.listMessage),
    url(r'^message/(?P<id>\d)$', xzjmt.self.views.messageDetail),
    url(r'^message/reply/(?P<id>\d)$', xzjmt.self.views.replyMessage),
    url(r'^follow/(?P<id>\d)$', xzjmt.self.views.follow),
    url(r'^collect/(?P<id>\d)$', xzjmt.self.views.collect),
    url(r'^collection$', xzjmt.self.views.collection),
)