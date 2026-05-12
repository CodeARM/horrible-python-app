from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    return render(request, "home.html", {'tasks': tasks})

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_task")
    else:
       form = TaskForm()

    return render(request, "home.html", {
       "form": form 
    })