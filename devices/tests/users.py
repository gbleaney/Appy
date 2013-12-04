from django.test.client import Client
from django.test import TestCase
from appy.models import*

import json
from django.core import serializers

class UserAPITestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_login(self):
		print 'POST --> /api/login'
		c = Client()
		response = c.post('/api/login/', {'username': 'farhan', 'password': 'foobar'}).content

		user = User.objects.get(username='farhan')

		expected = serializers.serialize('json', [user], relations=('inputs', 'outputs'))
		expected = expected[1:-1]
		
		self.assertEqual(response, expected)
		print 'Success'