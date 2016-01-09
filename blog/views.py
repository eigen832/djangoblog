from django.shortcuts import render
#from django.http import HttpResponse



# Create your views here.
#def index(request):
#	return HttpResponse("Hello world from my blog")

def index(request):
	data = {'mydata': "Hello world from my blog !"}
	return render(request, 'blog/index.html', data)
