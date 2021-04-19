from django.urls import path
from myfirstpython import views

urlpatterns = [
    path("", views.home, name="home"),
]