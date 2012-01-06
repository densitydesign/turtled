from django.http import HttpResponse
from django.shortcuts import render_to_response

from turtling.api import Japi

def api( request, action='' ):
	japi = Japi( action )
	return HttpResponse( japi, mimetype='application/json')

def index( request ):
	return render_to_response('turtling/index.html', {'latest_poll_list': "hello, world"})
