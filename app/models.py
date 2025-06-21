from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    due_time = models.TimeField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title