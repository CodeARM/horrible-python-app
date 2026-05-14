from django.db import models

class Task(models.Model):
    CONTEXT_CHOICES = [
        ("---", "---"),
        ("out|side", "out|side"),
        ("home", "home"),
        ("office", "office"),
        ("computer", "computer"),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    context = models.CharField(max_length=10, choices=CONTEXT_CHOICES, blank=False, default="---")
    project = models.CharField(max_length=50)

    class Meta:
        db_table = "tasks"
    def __str__(self):
        return self.title