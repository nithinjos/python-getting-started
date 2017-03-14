from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import requests
import os
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    template = get_template('main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)

    #return render(request, 'main_page.html')
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def nithin(request):
	print 'awesome!'
	return HttpResponse('kidilan')