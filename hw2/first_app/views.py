from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

dict_ = {
		'first': 'Hello',
		'second': 'everyone'
}
def home(request):
	content = {'name': dict_}
	return render(request, 'first_app/file.html', content)

def json_reader(request):
	with open('2homework8.json', 'r') as file:
		data = json.load(file)

		for q in data["items"]:
			a = q["job"]
			r = requests.get(a)

	return HttpResponse(r)		

def dict_(request):
	dict1 = {'a': 100, 'b': 200, 'c': 300}
	dict2 = {'a': 300, 'b': 200, 'd': 400}
	dict3 = F"{dict1}, {dict2}"

	return HttpResponse(dict3)

def check(request):
	pass	
		