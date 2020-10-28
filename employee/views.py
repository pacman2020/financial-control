from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Employee

# Create your views here.
def employees(request):
    list_employees = Employee.objects.all()
    paginator = Paginator(list_employees, 10)
    page = request.GET.get('page')
    data = {
        'employees': paginator.get_page(page)
    }
    return render(request,'employee/list_employee.html', data)