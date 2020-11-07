from service.models import Service
from employee.models import Employee
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    #vai lista apenas as tarefas ativas
    list_employee = Employee.objects.filter(active=True)

    employee_id = forms.ModelChoiceField(
        queryset=list_employee,
        label='funcionario',
        required=True
        )

    #vai lista apenas as servicos ativas
    list_service = Service.objects.filter(active=True)

    service_id = forms.ModelChoiceField(
        queryset=list_service,
        label='nome da tarefa',
        required=True
        )

    class Meta:
        model = Post
        fields = ('employee_id','service_id',)