from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("tasks/create/", views.create_task, name="create_task"),
]