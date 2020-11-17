from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.



def home(request):
	return HttpResponse('Hello!!')

def introduction(request):
	return HttpResponse('Welcome to our website. You can find here all answers to your questions')

def dt(request):
	return HttpResponse(datetime.datetime.now())

def solution(request):
	dict_ = {}
	for i in range(16):
		dict_[i] = i*i
	return render_to_response(dict_)		
