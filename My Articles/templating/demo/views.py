from  django.views.generic import ListView,DetailView
from .models import myArticle
# Create your views here.

class Bobby(ListView):
	model = myArticle
	template_name = 'index.html'

class DetailBobby(DetailView):
	model = myArticle
	template_name = 'home.html'
	context_object_name = 'obj'
