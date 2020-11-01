from django import forms
# from django.db import models
from django.forms import fields
from .models import Post

class PostForm(forms.ModelForm):
    employee_id = forms.DecimalField(label='funcionario', required=True)
    task_id = forms.DecimalField(label='tarefa', required=True)

    class Meta:
        model = Post
        fields = ('employee_id','task_id',)