from django.urls import path

from . import views

urlpatterns = [
   
    path('',views.Bobby.as_view(),name="bobby"),
    path('page/<int:pk>',views.DetailBobby.as_view(),name="detail_bobby"),
]