from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.templateView.as_view(),name="first"),
]