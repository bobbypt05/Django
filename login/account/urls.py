from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signupview.as_view(),name='signup'),
]
