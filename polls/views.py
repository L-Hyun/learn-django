from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
  if (request.method == "GET"):
    return HttpResponse("Hello Django World")

  data = json.loads(request.body)
  r = ""
  for k in data:
    r += data[k] + ' '
  return HttpResponse(r)
