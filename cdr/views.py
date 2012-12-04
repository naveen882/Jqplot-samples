# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from apis.api import write_exception,get_request_type,remove_splchars
from django.contrib.auth import authenticate
from django.contrib.auth.views import logout_then_login
import logging
from tagging.models import Category,Taggeddata,Categorygroup,CustomerProfile,Assigntaggedcontent
from ilabs_conf import *
from content.models import Content
import csv
import re
import os
import codecs
from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.servers.basehttp import FileWrapper
from django.conf import settings
import mimetypes
from users.models import UserProfile
from django.db.models import Q
from cdr.models import Cdr
from datetime import datetime
from mx.DateTime.ISO import ParseDateTimeUTC
import pprint
from pprint import PrettyPrinter
from collections import defaultdict


def get_data(request):
	return render_to_response('cdr/get_data.html', context_instance=RequestContext(request, {})) 

def process_data(request):
	response_dict = {'cdr': '0','status':'0'}
	try:
		if request.method == 'GET':
			qd = request.GET
		elif request.method == 'POST':
			qd = request.POST
		startdate = qd.__getitem__('startdate')
		enddate = qd.__getitem__('enddate')
		ring_opt = qd.__getitem__('ring_opt')
		logging.debug(startdate)
		logging.debug(enddate)
		cdr = [([x.strftime('%Y-%m-%d'), x.hour]) for x in \
					Cdr.objects.filter(start_of_call__range=(startdate,enddate),status=ring_opt).values_list('start_of_call',flat=True)]
		if len(cdr) > 0:
			response_dict.update({'cdr' : cdr})
	except:
		response_dict.udpate({'status':'1'})
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')

def get_pie_data(request):
	return render_to_response('cdr/get_pie_data.html', context_instance=RequestContext(request, {})) 

def process_pie_data(request):
	d = defaultdict(int)
	response_dict = {'cdr': '0','status':'0'}
	new_dict={}
	try:
		if request.method == 'GET':
			qd = request.GET
		elif request.method == 'POST':
			qd = request.POST
		startdate = qd.__getitem__('startdate')
		enddate = qd.__getitem__('enddate')
		ring_opt = qd.__getitem__('ring_opt')
		logging.debug(startdate)
		logging.debug(enddate)
		#cdr = [([ new_dict({str(x.strftime('%Y-%m-%d')):0}) if str(x.strftime('%Y-%m-%d')) not in new_dict else new_dict[str(x.strftime('%Y-%m-%d'))]=new_dict[str(x.strftime('%Y-%m-%d'))]+1]) for x in Cdr.objects.filter(start_of_call__range=(startdate,enddate),status=ring_opt).values_list('start_of_call',flat=True)]
		cdr = [([x.strftime('%Y-%m-%d'), x.hour]) for x in \
					Cdr.objects.filter(start_of_call__range=(startdate,enddate),status=ring_opt).values_list('start_of_call',flat=True)]
		for i in cdr:
			d[i[0]] += 1
		cdr = [[k,d[k]] for k in d]
		if len(cdr) > 0:
			response_dict.update({'cdr' : cdr})
	except:
		response_dict.udpate({'status':'1'})
	return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')


