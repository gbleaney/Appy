from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods

#Render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from appy.models import*

import ap

#JSON
import json
from django.core import serializers

from django.core.exceptions import ObjectDoesNotExist

#SERIALIZER
from api.serializers import*

#GET ALL DEVICES OR CREATE DEVICE
@csrf_protect
def devices(request):
	#Initialize response and get user and data from request
	user = ap.getUser(request)
	data = ap.getData(request)

	if user.is_anonymous():
		return HttpResponse(status=401)

	response = {}
	method = request.method

	#Create
	if(method == "POST"):
		response = createDevice(request, response, user, data)
	#READ
	elif(method == "GET"):
		response = getDevices(request, response, user, data)

	return HttpResponse(response, mimetype="application/json")

#GET, PUT OR DELETE A SPECIFIC DEVICE
@csrf_protect
def device(request, deviceId):

	method = request.method
	response = {}

	data = ap.getData(request)
	user = ap.getUser(request)
	
	if user.is_anonymous():
		return HttpResponse(status=401)

	#READ
	if(method == "GET"):
		response = getDevice(request, response, user, deviceId)
	#UPDATE
	elif(method == "PUT"):
		response = updateDevice(request, response, user, data, deviceId)
	#DELETE
	elif(method == "DELETE"):
		response = deleteDevice(request, response, user, data, deviceId)
		
	return response


#GET ALL BASE DEVICES
@csrf_exempt
@require_http_methods(["GET"])
def baseDevices(request):
	response = {}
	
	devices = BaseDevice.objects.all()

	return ap.JSONResponse(BaseSerializer(devices).data)

#GET A SPECIFIC BASE DEVICE
@csrf_exempt
@require_http_methods(["GET"])
def baseDevice(request, deviceId):

	response = {}
	data = ap.getData(request)

	try:
		device = BaseDevice.objects.get(id=deviceId)
		return ap.JSONResponse(BaseSerializer(device).data)
		
	except:
		return HttpResponse('Not found')

	return HttpResponse(response, mimetype="application/json")


####################################################
			#BEGIN CRUD FOR USER DEVICES
####################################################

def getDevices(request, response, user, data):
	return ap.JSONResponse(DeviceSerializer(Device.objects.filter(user=user)).data)

def createDevice(request, response, user, data):

	deviceName = data['deviceName']
	osVersion = data['osVersion']
	appVersion = data['appVersion']

	try:
		baseDevice = BaseDevice.objects.get(name=deviceName, osVersion=osVersion, appVersion=appVersion)
		try:
			existingDevice = Device.objects.get(baseDevice=baseDevice, user=user)
			if existingDevice:
				return HttpResponse('Device exists')

		except ObjectDoesNotExist:
			newDevice = Device.objects.create(baseDevice=baseDevice, user=user)
			newDevice.save()
			response = DeviceSerializer(newDevice).data

			return ap.JSONResponse(response)

	except ObjectDoesNotExist:
		return HttpResponse('Device not supported')

def getDevice(request, response, user, deviceId):
	try:
		print deviceId
		try:
			device = Device.objects.get(id=deviceId)
			response = DeviceSerializer(device).data

			return ap.JSONResponse(response)
		except ObjectDoesNotExist:
			return HttpResponse('Device does not exist')
	except KeyError:
		return HttpResponse('No id given')


def updateDevice(request, response, user, data, deviceId):
	return response

def deleteDevice(request, response, user, data, deviceId):

	try:
		device = Device.objects.get(id=deviceId)

		if user == device.user:
			device.delete()
		else:
			return HttpResponse('Wrong user')

	except ObjectDoesNotExist:
		return HttpResponse('Device does not exist')

####################################################
			#END CRUD FOR USER DEVICES
####################################################