from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):

    tasks = Task.objects.all()

    return render(request, 'index.html', {'tasks':tasks})

def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('index')

def delete(request, task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')