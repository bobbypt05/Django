from  django.views.generic import ListView

# Create your views here.

from .models import Cmdr

class templateView(ListView):
	model = Cmdr
	template_name = 'index.html'