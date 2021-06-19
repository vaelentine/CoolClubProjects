"""
views do the following
 1. pass a request object as an argument,
 2. transform some data based on the request,
 3. and return
   - a request,
   - an html page and
   - a dictionary object (data)

views must be routed via urls - these can take object ids or other data names to pull objects

"""
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'message': 'hello, world'}
    return render(request, 'index.html', context)
