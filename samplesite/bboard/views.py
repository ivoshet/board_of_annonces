from django.http import request
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('list of ads will be displayed here')
