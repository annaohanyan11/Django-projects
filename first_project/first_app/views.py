from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse("Hello Django world!")

def last_name(request):
	return HttpResponse("I'm Anna Ohanyan")
