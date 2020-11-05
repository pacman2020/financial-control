from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

@login_required
def employees(request):
    list_employees = Employee.objects.all()
    paginator = Paginator(list_employees, 10)
    page = request.GET.get('page')
    data = {
        'employees': paginator.get_page(page)
    }
    return render(request,'employee/list_employee.html', data)

@login_required
def detail_employee(request, pk):
    try:
        employee = get_object_or_404(Employee,pk=pk)
        data = {
            'employee': employee
        }
        return render(request, 'employee/detail_employee.html',data)
    except:
        return redirect('employees')

@login_required
def new_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            task= form.save(commit=False)
            task.user_id = request.user
            task.save()
            return redirect('detail_employee', pk=task.pk)
    else:
        form = EmployeeForm()
    return render(request, 'employee/new_update_employee.html', {'form':form})

@login_required
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk, user_id=request.user)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee.save()
            return redirect('detail_employee', pk=employee.pk)
    else:
        form = EmployeeForm(instance=employee)
        data = {
            'form':form,
            'employee': employee
        }
        return render(request, 'employee/new_update_employee.html',data)

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk, user_id=request.user)
    employee.active = False
    employee.save()
    return redirect('employees')