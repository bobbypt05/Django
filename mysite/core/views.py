from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import SignUpModel

def login(request):
	return render(request,'loginpage.html')

def homepage(request):
	return render(request,'base.html')

def signup(request):
    if request.method=="POST":
    
    	form = SignUpForm(request.POST)
    	if form.is_valid():
    		new_req = SignUpModel(username = request.POST.get('Fusername',False), first_name = request.POST.get('Mfirst_name',False), last_name = request.POST.get('Mlast_name',False),
    		email = request.POST.get('Memail',False), password1 = request.POST.get('Mpassword1',False), password2 = request.POST.get('Mpassword2',False))
    		new_req.save()
    		return redirect('home')
    else:
    		form = SignUpForm()

    context = {'form': form}

    return render(request,'signup.html',context)



