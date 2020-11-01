from task.models import Task
from employee.models import Employee
from django import forms
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    employee_id = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
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