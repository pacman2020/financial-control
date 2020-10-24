from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Task

# Create your views here.
def tasks(request):
    task_list = Task.objects.all()

    paginator = Paginator(task_list, 10)
    page = request.GET.get('page')
    data = {
        'tasks': paginator.get_page(page)
    }

    return render(request, 'task/list_task.html', data)