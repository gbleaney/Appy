from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods

#Render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from appy.models import*

import ap

import json

#SERIALIZER
from api.serializers import*

@csrf_protect
def userAppys(request):
	#Initialize response and get user and data from request
	response = {}

	user = ap.getUser(request)
	data = ap.getData(request)
	method = request.method

	if user.is_anonymous():
		return HttpResponse(status=401)

	#Create
	if(method == "POST"):
		response = createAppy(request, response, user, data)

	#READ
	elif(method == "GET"):
		response = getAppys(response, user)
	return response

@csrf_protect
def userAppy(request, appyId):
	response = {}

	user = ap.getUser(request)
	method = request.method

	if user.is_anonymous():
		return HttpResponse(status=401)
		
	responseAppy = {}
	responseDevices = []

	try:
		appy = Appy.objects.get(id=appyId)
		devices = AppyDevice.objects.filter(appy=appy)

		for device in devices:
			responseDevices.append(AppyDeviceSerializer(device).data)

		responseAppy['appy'] = AppySerializer(appy).data
		responseAppy['appyId'] = appy.id
		responseAppy['appyDevices'] = responseDevices
	except:
		return HttpResponse('Appy not found', status=404)

	if not user == appy.user:
		return HttpResponse(status=401)

	print method
	#READ
	if (method == "GET"):
		print responseAppy
		return ap.JSONResponse(responseAppy)
	elif(method == "PUT"):
		response = updateAppy(request, response, appy)
	elif(method == "DELETE"):
		appy.delete()
		return HttpResponse('Appy Deleted', status=200)
	else:
		return HttpResponse('Unknown Request', status=404)

	return HttpResponse(response, mimetype="application/json")

def createAppy(request, response, user, data):
	appy = Appy.objects.create()
	print data

	appy.user = user
	appy.name = data['appy']['name']
	appy.description = data['appy']['description']
	appy.save()


	for device in data['appyDevices']:
		print device
		userDevice = Device.objects.get(id=device['device']['id'])
		outputs = []
		inputs = []

		try:
			inputs = device['inputs']
		except:
			print "No inputs on appy device"

		try:
			outputs = device['outputs']
		except:
			print "No outputs on appy device"

		newDevice = AppyDevice.objects.create(device=userDevice, appy=appy)
		if inputs:
			for inputAction in inputs:
				try:
					newDevice.inputs.add(Input.objects.get(id=inputAction['value']['id']))
				except:
					print "Missing input action"
		if outputs:
			for outputAction in outputs:
				try:
					newDevice.outputs.add(Output.objects.get(id=outputAction['value']['id']))
				except:
					print "Missing output action"

		newDevice.save()

	appy.save()

	return ap.JSONResponse(AppySerializer(appy).data)

def getAppys(response, user):
	try:
		appy = Appy.objects.filter(user=user)
		return ap.JSONResponse(AppySerializer(appy).data)
	except:
		return HttpResponse('Appy does not exist')

def updateAppy(request, response, appy):

	data = ap.getData(request)
	appy.name = data['appy']['name']
	appy.description = data['appy']['description']
	appy.save()

	devices = Appy.getDevices(appy)
	devicesLength = devices.count()

	print "Deleted:"
	print devices
	for device in devices:
		print device.device.baseDevice.name
		device.delete();

	inputs = []
	outputs = []
	

	appyDevices = data['appyDevices']

	for device in appyDevices:

		try:
			inputs = device['inputs']
		except:
			print "No inputs on appy device" + device

		try:
			outputs = device['outputs']
		except:
			print "No outputs on appy device" + device

		userDevice = Device.objects.get(id=device['device']['id'])

		newDevice = AppyDevice.objects.create(device=userDevice, appy=appy)

		for inputAction in inputs:
			newDevice.inputs.add(Input.objects.get(id=inputAction['value']['id']))

		for outputAction in outputs:
			newDevice.outputs.add(Output.objects.get(id=outputAction['value']['id']))

		newDevice.save()

	return ap.JSONResponse(AppySerializer(appy).data)