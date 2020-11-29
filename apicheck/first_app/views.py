from django.shortcuts import render, redirect
from django.http import HttpResponse
from apiclient.discovery import build
import urllib.request
import json
import re
from pytube import YouTube


# Create your views here.

def home(request):
	
	# return HttpResponse("sdchnsidchs")
	api_key = 'AIzaSyCurwIFtb9Mv0VRgWVaNlpQZ_PwwJ326XY'
	
	# youtube = build('youtube', 'v3', developerKey=api_key)
	# request = youtube.channels().list(
	# 	part ='statistics',
	# 	forUsername='schafer5'
	# 	)
	# response = request.execute()

	content = {'name': 1}
	
	return render(request, 'first_app/home.html', content)
	