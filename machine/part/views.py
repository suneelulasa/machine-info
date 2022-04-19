from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def newpart(request):
    return render(request, 'home.html')


# return HttpResponse('it is a new part')
def anotherpart(request):
    return HttpResponse('it is another part')


# def about(request):
#     return render(request, 'home.html')
