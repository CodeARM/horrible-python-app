from django.urls import path
from web import views

urlpatterns = [
    path("", views.home),
    path("create_task", views.create_task, name="create_task"),
    #     path("tasks/create/", views.create_task, name="create_task"), this is suggested by chippy but i don't know what create is


]