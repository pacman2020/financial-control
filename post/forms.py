from task.models import Task
from employee.models import Employee
from django import forms
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    #vai lista apenas as tarefas ativas
    list_employee = Employee.objects.filter(active=True)

    employee_id = forms.ModelChoiceField(
        queryset=list_employee,
        label='funcionario',
        required=True
        )

    #vai lista apenas as tarefas ativas
    list_task = Task.objects.filter(active=True)

    task_id = forms.ModelChoiceField(
        queryset=list_task,
        label='nome da tarefa',
        required=True
        )

    class Meta:
        model = Post
        fields = ('employee_id','task_id',)