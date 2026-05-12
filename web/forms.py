from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "context", "project"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Task title"
            }),
            "context": forms.Select(attrs={
                "class": "form-control",
                "placeholder": "",
            }),
            "project": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project name"
            }),
        }