from django.urls import path
from . import views

urlpatterns = [
    path('',views.loginView,name="login"),
    path('afterlogin/',views.afterLogin, name="after")
]