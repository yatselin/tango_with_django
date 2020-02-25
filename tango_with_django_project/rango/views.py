from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)
    # Chapter 3 assignment (include hyperlink),
    # in <a> use ">About<" not ">about<"!!! to pass test
    # return HttpResponse("Rango says hey there partner!<br/><a href='/rango/about/'>About</a>")


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Iar'}
    return render(request, 'rango/about.html', context=context_dict)
    # Chapter 3 assignment (include hyperlink),
    # in <a> use ">Index<" not ">index<"!!! to pass test
    # return HttpResponse("Rango says here is the about page.<br/><a href='/rango/'>Index</a>")
