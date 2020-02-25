from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about/'>About</a>")
    #return HttpResponse("Rango says hey there partner!")

def about(request):
    return HttpResponse("Rango says here is the about page.<br/><a href='/rango/'>Index</a>")
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>to main</a>")
    #return HttpResponse("<a href="/about">Rango says here is the about page.</a>")
    #(<a href='/rango/about/'>About</a>)
    #return HttpResponse("Rango says here is the about page.")
