from django.shortcuts import render

# Create your views here.

def afterlogin(request):
	return render(request,'index.html')

def basePage(request):
	return render(request,'base.html')