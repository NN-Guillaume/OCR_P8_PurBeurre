#from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    # do something here
    template = loader.get_template('rechercher/index.html')
    return HttpResponse(template.render(request=request))
    #p8_00

def connected(request):
    template = loader.get_template('rechercher/connected.html')
    return HttpResponse(template.render(request=request))
    #p8_01

def results(request):
    template = loader.get_template('rechercher/results.html')
    return HttpResponse(template.render(request=request))
    #p8_02

def aliment(request):
    template = loader.get_template('rechercher/aliment.html')
    return HttpResponse(template.render(request=request))
    #p8_03

def user_create(request):
    template = loader.get_template('rechercher/user_create.html')
    return HttpResponse(template.render(request=request))
    #p8_04

def user_account(request):
    template = loader.get_template('rechercher/user_account.html')
    return HttpResponse(template.render(request=request))
    #p8_05