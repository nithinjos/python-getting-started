from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context,Template,RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from .models import Greeting
from hello.forms import *

import requests
import os
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #template = get_template('main_page.html')
    #variables = Context({ 'user': request.user })
    #output = template.render(variables)
    #return HttpResponse(output)
    return render_to_response('main_page.html',RequestContext(request))
    #return render(request, 'main_page.html')
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def nithin(request):
	print 'awesome!'
	return HttpResponse('kidilan')

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], email = form.cleaned_data['email'])
			return HttpResponseRedirect('/')
	form = RegistrationForm()
	variables= RequestContext(request,{'form':form})
	return render_to_response('registration/register.html', variables)