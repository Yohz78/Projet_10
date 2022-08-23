from django.shortcuts import render
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body  # Byte string of JSON data
    data = {}
    print(request.GET)  # URL query parameters
    print(request.POST)
    try:
        data = json.loads(body)  # String of JSON data -> Python Dict
    except:
        pass
    print(data.keys())
    data["params"] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
