from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, verbose_name=('userprofile'), related_name='userprofile', null=True)

	def __unicode__(self):
		if self.user:
			return self.user.username


class BaseDevice(models.Model):
	inputs = models.ManyToManyField('Input')
	outputs = models.ManyToManyField('Output')
	name = models.CharField(max_length=15, default='iPhone')
	osVersion = models.FloatField(default=1.0)
	appVersion = models.FloatField(default=1.0)

	def __unicode__(self):
		return self.name

class Input(models.Model):
	name = models.CharField(max_length=25, default='Shake')

	def __unicode__(self):
		return self.name

class Output(models.Model):
	name = models.CharField(max_length=25, default='Shake')

	def __unicode__(self):
		return self.name
			
class Device(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	baseDevice = models.ForeignKey('BaseDevice', blank=True, null=True)

	def __unicode__(self):
		return self.baseDevice.name

class Appy(models.Model):
	name = models.CharField(max_length=25, default='New Appy')
	description = models.TextField(null=True, default='')
	user = models.ForeignKey(User, blank=True, null=True)

	def getDevices(self):
		return AppyDevice.objects.filter(appy=self)

	def getOutputs(self):
		outputs = []
		for device in AppyDevice.objects.filter(appy=self):
			outputs.append(device.outputs.all())
		return outputs

	def __unicode__(self):
		return self.name

class AppyDevice(models.Model):
	appy = models.ForeignKey('Appy', blank=True, null=True)
	device = models.ForeignKey('Device', blank=True, null=True)
	inputs = models.ManyToManyField('Input', blank=True, null=True)
	outputs = models.ManyToManyField('Output', blank=True, null=True)

	def __unicode__(self):
		return self.appy.name