from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def LVA (request):
    return HttpResponse('you are looking like pig')
def Rishi(request):
    return HttpResponse('<h1><marquee>hi hello rishi this is ur frnd jinjaa from chilakaluripeta</h1></marquee>')