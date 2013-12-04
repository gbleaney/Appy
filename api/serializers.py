from django.contrib.auth.models import User
from appy.models import*
from rest_framework import serializers



class InputSerializer(serializers.ModelSerializer):
	class Meta:
		model = Input

class OutputSerializer(serializers.ModelSerializer):
	class Meta:
		model = Output


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email')


class BaseSerializer(serializers.ModelSerializer):
	inputs = InputSerializer(many=True)
	outputs = OutputSerializer(many=True)

	class Meta:
		model = BaseDevice

class DeviceSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	baseDevice = BaseSerializer()

	class Meta:
		model = Device

class AppySerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Appy

class AppyDeviceSerializer(serializers.ModelSerializer):
	# appy = AppySerializer()
	inputs = InputSerializer(many=True)
	outputs = OutputSerializer(many=True)
	device = DeviceSerializer()

	class Meta:
		model = AppyDevice
