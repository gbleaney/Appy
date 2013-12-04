from django.test.client import Client
from django.test import TestCase
from appy.models import*
import json
from api.serializers import*

class UserAPITestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_login(self):
		print 'POST --> /api/login'
		c = Client()
		response = c.post('/api/login/', {'username': 'farhan', 'password': 'foobar'}).content

		expected = json.dumps(UserSerializer(User.objects.get(username='farhan')).data)
		
		self.assertEqual(response, expected)
		print 'Success'