from django import forms
from django.forms import fields
from .models import Employee

class Taskform(forms.ModelForm):
    full_name = forms.CharField(label='nome completo', max_length=100, required=True)
    active = forms.BooleanField(label='funcionario ativo' ,required=True)
    class Meta:
        model = Employee
        fields = ('full_name','active',)