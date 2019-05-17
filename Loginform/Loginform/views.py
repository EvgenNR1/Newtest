from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('homepage')
    # страницу возвразает и показывает, но вместо этого сделаем рендер с запросом на какой темплейт пойдем, и далее пойдем в settings
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('about') # возвращаем ретурном то что импортнули, что бы перейти в абоут
    # из views переходим в урлс
    # страницу возвразает и показывает
    return render(request,'about.html')
