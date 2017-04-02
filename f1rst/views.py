from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.


def index(request):
	hour = int(time.strftime('%H'))*11
	minute =int(time.strftime('%M'))*4
	sec = int(time.strftime('%S'))*4
	style = "background-color:rgb("+str(hour)+","+str(minute)+","+str(sec)+ ");"
    	return HttpResponse("<div style ='"+style +"'>"+ '<p>Hello, World...or something.</p><p>You accessed this page at '+time.strftime('%c')+'</p></div>')

def diff(request):
	return HttpResponse('<h1>This is a different page.</h1>')
