from django.test.client import Client
from django.test import TestCase
from appy.models import*

import json

from api.serializers import*

class AppyAPITestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_get_appys(self):
		print 'GET --> /api/appys'
		c = Client()
		c.login(username='farhan', password='foobar')
		response = c.get('/api/appys/').content

		user = User.objects.get(username='farhan')
		appys = Appy.objects.filter(user=user)

		expected = json.dumps(AppySerializer(appys).data)

		self.assertEqual(response, expected)
		print 'Success'

	def test_get_appy(self):
		print 'GET --> /api/appys/1'
		c = Client()
		c.login(username='farhan', password='foobar')
		response = c.get('/api/appys/1').content
		print response

		user = User.objects.get(username='farhan')
		appy = Appy.objects.get(id=1)

		expected = json.dumps(AppySerializer(appy).data)
		
		self.assertEqual(response, expected)
		print 'Success'
