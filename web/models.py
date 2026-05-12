from django.db import models

class Task(models.Model):
    CONTEXT_CHOICES = [
        ("_____", "_____"),
        ("out", "out"),
        ("home", "home"),
        ("office", "office"),
        ("computer", "computer"),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    context = models.CharField(max_length=25, choices=CONTEXT_CHOICES, blank=False, default="_____")
    project = models.CharField(max_length=100)

    class Meta:
        db_table = "tasks"
    def __str__(self):
        return self.title