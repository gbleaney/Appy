from appy.models import*

from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from pprint import pprint

import json

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders it's content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# GENERAL HELPER METHODS

def getData(request):
	try:
		data = json.loads(request.body)
	except:
		data = request.REQUEST 

	return data


def getUser(request):
	try:
		sessionid = request.COOKIES.get("sessionid")
		session = Session.objects.get(pk=sessionid)
		user = session.user
	except:
		user = request.user
	return user

def getAppy(request, appyId):
	data = getData(request)
	appy = Appy.objects.get(id=appyId)

	return appy