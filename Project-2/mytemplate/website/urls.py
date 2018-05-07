from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name="home"),
    path('about/',views.AboutPageView.as_view(),name="about"),
    path('contact_us/',views.ContactPageView.as_view(),name="contact"),
]
