from django.http import HttpResponse
from django.shortcuts import render

def home(request):
     return HttpResponse("this is home section of SOCWATCH project")
    
def about(request):
    return HttpResponse("this is about section of SOCWATCH project")

def team(request):
    return HttpResponse("this is team section of SOCWATCH project")


    