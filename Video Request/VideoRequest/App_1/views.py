from django.shortcuts import render, redirect
from .models import video
from .forms import videoForm 
# Create your views here.

def index(request):
	model = video.objects.order_by('date_added')
	context = {'model': model}
	return render(request, 'index.html',context)



def vrform(request): 
	if request.method == "POST":
		form = videoForm(request.POST)

		if form.is_valid():
			new_req = video(title=request.POST['videoName'],description=request.POST['videoDescription'])
			new_req.save()
			return redirect('index')
	else:
		form = videoForm()		

	context = {'form' : form}

	return render(request, 'videorequest.html',context)