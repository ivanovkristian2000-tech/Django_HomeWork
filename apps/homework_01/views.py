from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greeting(request):
    return HttpResponse("<h1>Hello, Kris!</h1>")
