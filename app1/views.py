from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Welcome to webwing")


def about(request):
    return HttpResponse("About Page")


def courses(request):
    return HttpResponse("courses page")
