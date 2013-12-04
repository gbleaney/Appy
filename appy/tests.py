from django.test import TestCase
from models import*

class BaseDeviceTestCase(TestCase):
	fixtures = ['appy/initial_data.json', 'users/initial_data.json']

	def test_query_base_devices(self):
		iPhone = BaseDevice.objects.get(name="iPhone5")
		self.assertEqual(iPhone.appVersion, 0.0)

	def test_query_base_device_inputs(self):
		iPhone = BaseDevice.objects.get(name="iPhone5")
		inputs = Input.objects.all()
		iInputs = iPhone.inputs.all()
		for a, b in zip(inputs,iInputs):
			self.assertEqual(a, b)