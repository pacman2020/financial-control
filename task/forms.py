from django import forms
from django.db import models
from django.forms import fields
from .models import Task

class Taskform(forms.ModelForm):
    name = forms.CharField(label='nome da tarefa', max_length=100, required=True)
    price = forms.DecimalField(label='preço da tarefa', required=True)
    active = forms.BooleanField(label='tarefa ativa' ,required=True)
    class Meta:
        model = Task
        fields = ('name','price','active',)