from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    return render(request, "home.html", {
        "tasks": tasks,
        "form": form,
        })

def create_task(request):

    if request.method == "POST": 
        form = TaskForm(request.POST)

        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
       form = TaskForm()
    
    tasks = Task.objects.all()

    return render(request, "home.html", {
       "tasks": tasks,
       "form": form 
    })