from django.shortcuts import render

# Create your views here.
def loginView(request):
	return render(request,'index.html')

def afterLogin(request):
	return render(request,'afterlogin.html')