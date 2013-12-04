from django.conf.urls import patterns, url
from views import*

urlpatterns = patterns('',
	url(r'^sessions', sessions),
	url(r'^users', users),

	url(r'^devices/(?P<deviceId>\d+)$', device),
	url(r'^devices$', devices),

	url(r'^baseDevices$',baseDevices),
	url(r'^baseDevices/(?P<deviceId>\d*)$', baseDevice),

	url(r'^appys$', userAppys),
	url(r'^appys/(?P<appyId>\d*)$', userAppy),
)