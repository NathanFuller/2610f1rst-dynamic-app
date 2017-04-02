from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.


def index(request):
    return HttpResponse('<p>Hello, World...or something.</p><p>You accessed this page at '+time.strftime('%c')+'</p>')

def diff(request):
	return HttpResponse('<h1>This is a different page.</h1>')
