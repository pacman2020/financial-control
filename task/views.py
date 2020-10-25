from django.shortcuts import get_object_or_404, redirect, render
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

def detail_task(request, pk):
    try:
        task = get_object_or_404(Task,pk=pk)
        data = {
            'task': task
        }
        return render(request, 'task/detail_task.html',data)
    except:
        return redirect('tasks')