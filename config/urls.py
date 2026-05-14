from django.urls import path
from web import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_task/", views.create_task, name="create_task"),
]