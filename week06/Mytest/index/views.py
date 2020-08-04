from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person

def index(request):
    return HttpResponse('hell django')

def year(request, year):
    return HttpResponse(year)

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

def myyear(request, year):
    return HttpResponse(year)

def person(request):
    persons = Person.objects.all()
    return render(request, 'personview.html', locals())
