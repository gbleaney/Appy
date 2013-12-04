from django.core.management import setup_environ
from appy_server import settings
setup_environ(settings)

from django.core.context_processors import csrf
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect

#Render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from appy.models import*

#JSON
import json

devices = BaseDevice.objects.all().delete()
inputs = Input.objects.all().delete()
outputs = Output.objects.all().delete()

baseDevice0 = BaseDevice.objects.create(name="iPhone5", osVersion="5.0", appVersion="0.0")
baseDevice1 = BaseDevice.objects.create(name="NexusS", osVersion="5.0", appVersion="0.0")
baseDevice2 = BaseDevice.objects.create(name="GalaxyS3", osVersion="5.0", appVersion="0.0")
baseDevice3 = BaseDevice.objects.create(name="GalaxyS2", osVersion="5.0", appVersion="0.0")

input0 = Input.objects.create(name="Shake")
input1 = Input.objects.create(name="Slide")

output2 = Output.objects.create(name="TurnOn")
output3 = Output.objects.create(name="TurnOf")

devices = BaseDevice.objects.all()
inputs = Input.objects.all()
outputs = Output.objects.all()

for d in devices:
    device = BaseDevice.objects.get(id=d.id)
    device.inputs = inputs
    device.outputs = outputs
    device.save()