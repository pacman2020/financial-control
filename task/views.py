from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Task
from .forms import Taskform
from django.contrib.auth.decorators import login_required

@login_required
def tasks(request):
    task_list = Task.objects.all()

    paginator = Paginator(task_list, 10)
    page = request.GET.get('page')
    data = {
        'tasks': paginator.get_page(page)
    }

    return render(request, 'task/list_task.html', data)

@login_required
def detail_task(request, pk):
    try:
        task = get_object_or_404(Task,pk=pk)
        data = {
            'task': task
        }
        return render(request, 'task/detail_task.html',data)
    except:
        return redirect('tasks')

@login_required
def new_task(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            task= form.save(commit=False)
            task.user_id = request.user
            task.save()
            return redirect('detail_task', pk=task.pk)
    else:
        form = Taskform()
    return render(request, 'task/new_update_pet.html', {'form':form})

@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user_id=request.user)

    if request.method == 'POST':
        form = Taskform(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('detail_task', pk=task.pk)
    else:
        form = Taskform(instance=task)
        data = {
            'form':form,
            'task': task
        }
        return render(request, 'task/new_update_pet.html',data)

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user_id=request.user)
    task.active = False
    task.save()
    return redirect('tasks')
