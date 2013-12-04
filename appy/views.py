#CSRF
from django.core.context_processors import csrf
from django.middleware import csrf
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt, csrf_protect
#Render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import messages
#JSON
import json

@csrf_protect
def app(request):

	response = render(request, 'index.html')

	response.set_cookie('csrftoken', csrf.get_token(request))
	return response