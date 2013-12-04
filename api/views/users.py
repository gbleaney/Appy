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

#ap.py
import ap
#JSON
import json

#SERIALIZER
from api.serializers import*



@csrf_protect
def sessions(request):
	method = request.method
	data = ap.getData(request)
	response = {}
	if (method == "GET"):
		return ap.JSONResponse(UserSerializer(ap.getUser(request)).data)
	elif (method == "POST"):
		return login_user(request, data)
	elif (method == "DELETE"):
		logout(request)
		return HttpResponse('Logged out', status=200)
	else:
		return HttpResponse(status=404)

@csrf_protect
def users(request):
	method = request.method
	data = ap.getData(request)
	response = {}
	if (method == "POST"):
		return signup_user(data)
	elif (method == "PUT"):
		return edit_user(request, data)
	else:
		return HttpResponse(status=404)

def login_user(request, data):

	name = data['username']
	password = data['password']
	user = authenticate(username=name, password=password)

	if user:
		login(request, user)
		response = UserSerializer(user).data

		return ap.JSONResponse(response)
	else:
		return HttpResponse("Incorrect username or password", status=500)


def edit_user(request, data):
	user = ap.getUser(request)

	name = data['username']
	password = data['password']

	response = UserSerializer(user).data

	return ap.JSONResponse(response)



def signup_user(data):

	username = data['username']
	password = data['password']
	email = data['email']

	try:
		user = User.objects.get(username=username)
		if user:
			return HttpResponse("User already exists with this name", status=500)
	except:
		pass

	try:
		user = User.objects.get(email=email)
		return HttpResponse("User with this email already exists", status=500)
	except:
		pass

	user = User.objects.create_user(username, email, password)
	user.save()
	response = UserSerializer(user).data

	return ap.JSONResponse(response)
