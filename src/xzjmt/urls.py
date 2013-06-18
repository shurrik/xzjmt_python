from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'xzjmt.views.home', name='home'),
    url(r'^about$', 'xzjmt.views.about', name='about'),
    url(r'^login$', 'xzjmt.views.login', name='login'),
    url(r'^logout$', 'xzjmt.views.logout', name='logout'),
    url(r'^login$', 'xzjmt.views.login', name='login'),
    
    url(r'^accounts/login/$', 'xzjmt.views.accountLogin', name='loginView'),
    url(r'^accounts/auth$', 'xzjmt.views.accountAuth', name='auth'),

    url(r'^item/', include('xzjmt.item.urls')),
    url(r'^reg/', include('xzjmt.reg.urls')),
    url(r'^self/', include('xzjmt.self.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

