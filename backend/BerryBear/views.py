# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    return HttpResponse("Berry Bear")


@csrf_exempt
def move(request):
	data = json.loads(request.body)
	#TODO make function for moving the bear
	return HttpResponse(data["direction"])
	#return JsonResponse(data)