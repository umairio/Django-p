from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def home2(request):
  template = loader.get_template('home2.html')
  return HttpResponse(template.render())