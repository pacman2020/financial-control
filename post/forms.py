from task.models import Task
from employee.models import Employee
from django import forms
# from django.db import models
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    # name = forms.CharField(label='nome da tarefa', max_length=100, required=True)
    employee_id = forms.ModelChoiceField(queryset=Employee.objects.all(),label='funcionario',required=True )
    task_id = forms.ModelChoiceField(queryset=Task.objects.all(),label='nome da tarefa',required=True )

    class Meta:
        model = Post
        fields = ('employee_id','task_id',)