#Decorators
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
from django.views.decorators.http import require_http_methods
from django.core.context_processors import csrf
from django.middleware import csrf
#Render
#HTTP
from django.http import HttpResponse, HttpResponseRedirect
#AUTH and Models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from appy.models import*

from django.core import serializers

#JSON
import json

@csrf_exempt
def login(request):
	response = {}
	data = getData(request)
	user = authenticate(username=data['username'], password=data['password'])

	if user:
		base = BaseDevice.objects.filter(name=data['device'])[0]
		device = Device.objects.get(user=user, baseDevice=base)
		appyDevices = AppyDevice.objects.filter(device=device)

		inputs = {}
		for input in base.inputs.all():
			inputs[input.name] = ''

		for appyDev in appyDevices:
			for input in appyDev.inputs.all():
				inputs[input.name] += str(appyDev.appy.id)+','

		outputs = {}
		for output in base.outputs.all():
			outputs[output.name] = ''

		for appyDev in appyDevices:
			for output in appyDev.outputs.all():
				outputs[output.name] += str(appyDev.appy.id)+','

		response = {}
		response['username'] = user.username

		response['device'] = {}
		response['device']['name'] = base.name
		response['device']['inputs'] = inputs
		response['device']['outputs'] = outputs

		response = json.dumps(response)

		print response

	return HttpResponse(response, mimetype="application/json")

def getData(request):
	try:
		data = json.loads(request.body)
	except:
		data = request.REQUEST 
	return data