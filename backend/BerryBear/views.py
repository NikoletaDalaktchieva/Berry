# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Program
from django.core import serializers

# Create your views here.


def index(request):
    return HttpResponse("Berry Bear")


@csrf_exempt
def move(request):
    data = json.loads(request.body)
    print data["direction"]
    #TODO make function for moving the bear
    return HttpResponse(data["direction"])
    #return JsonResponse(data)



def get_programs_name(request):
    programs = Program.objects.all()

    response = []
    for p in programs:
        response.append({
                    "id": p.id,
                    "name" : p.name
                })
    return JsonResponse(response, safe = False)


@csrf_exempt
def get_program_info(request):
    id = json.loads(request.body)
    info = Program.objects.get(id = id["id"])

    data = {
        "id" : info.id,
        "name" : info.name,
        "commands" : info.commands
    }

    return JsonResponse(data)




@csrf_exempt
def update_program_info(request):
    new_info = json.loads(request.body)

    Program.objects.filter(id = new_info["id"]).update(name = new_info["name"])
    Program.objects.filter(id = new_info["id"]).update(commands = new_info["commands"])    

    return HttpResponse("update")

@csrf_exempt
def run(request):
    id = (json.loads(request.body))["id"]
    commands = Program.objects.get(id= id).commands.split(" ")
    for c in commands:
        print c
    return HttpResponse(id)
