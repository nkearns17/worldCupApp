from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am the bold font from the context"}
	return render_to_response('rugby/index.html', context_dict, context)

def coupon(request):
	return HttpResponse("coupon")

def leagueTable(Request):
	return HttpResponse("leagueTable")
