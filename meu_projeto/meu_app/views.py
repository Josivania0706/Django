from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,  v1, v2):
    soma  = v1 + v2
    return HttpResponse('<h1>soma {}</h1>'.format(v1 + v2))