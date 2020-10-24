from django.shortcuts import render
from .models import Task

# Create your views here.
def tasks(request):
    tasks = Task.objects.all()
    data = {
        'tasks': tasks
    }

    return render(request, 'task/list_task.html', data)