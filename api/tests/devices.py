from django.test.client import Client
from django.test import TestCase
from appy.models import*

import json
from api.serializers import*

class DeviceAPITestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_get_devices(self):
		print 'GET --> /api/devices'
		c = Client()
		c.login(username='farhan', password='foobar')
		user = User.objects.get(username='farhan')
		response = c.get('/api/devices/').content
		expected = json.dumps(DeviceSerializer(Device.objects.filter(user=user)).data)
		self.assertEqual(response, expected)
		print 'Success'

	def test_get_specific_device(self):
		print 'GET --> /api/devices/1'
		c = Client()
		c.login(username='farhan', password='foobar')
		response = c.get('/api/devices/1/').content

		user = User.objects.get(username='farhan')

		expected = json.dumps(DeviceSerializer(Device.objects.get(id=1)).data)
		
		self.assertEqual(response, expected)
		print 'Success'