from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from django.conf import settings
from django.http import response
import logging


def index(request):
    return HttpResponse("Hello, world. You're at the index.")
