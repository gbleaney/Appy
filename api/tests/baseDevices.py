from django.test.client import Client
from django.test import TestCase
from appy.models import*

import json
from api.serializers import*

class BaseDeviceAPITestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_get_base_devices(self):
		print 'GET --> /api/baseDevices'
		c = Client()
		response = c.get('/api/baseDevices/').content
		expected = json.dumps(BaseSerializer(BaseDevice.objects.all()).data)
		self.assertEqual(response, expected)
		print 'Success'

	def test_get_specific_base_device(self):
		print 'GET --> /api/baseDevices/1'
		c = Client()
		response = c.get('/api/baseDevices/1/').content
		expected = json.dumps(BaseSerializer(BaseDevice.objects.get(id=1)).data)
		self.assertEqual(response, expected)
		print 'Success'