from django.urls import path
from . import views

urlpatterns = [
  path('afrerone/',views.afterlogin,name='after'),
  path('basepage/',views.basePage,name='base')
]
