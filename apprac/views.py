from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')