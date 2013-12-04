from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from appy import views

urlpatterns = patterns('',
	url(r'^$', views.app, name='app'),

    #JSON API
    url(r'^api/', include('api.urls')),

    url(r'^devices/', include('devices.urls')),

    #Admin
    url(r'^admin/', include(admin.site.urls)),

)