from django.shortcuts import render
from django.http import HttpResponse
from douban_movie.models import *
# Create your views here.

def movie_short(request):
    shorts = DoubanNew.objects.all()
    check = 3

    return render(request, 'shortslist.html', locals())
    # shorts[1].short
    # return HttpResponse('sa')
