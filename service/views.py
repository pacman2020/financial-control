from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Service
from .forms import Serviceform
from django.contrib.auth.decorators import login_required

@login_required
def services(request):
    service_list = Service.objects.all()

    paginator = Paginator(service_list, 10)
    page = request.GET.get('page')
    data = {
        'services': paginator.get_page(page)
    }

    return render(request, 'service/list_service.html', data)

@login_required
def detail_service(request, pk):
    try:
        service = get_object_or_404(Service,pk=pk)
        data = {
            'service': service
        }
        return render(request, 'service/detail_service.html',data)
    except:
        return redirect('services')

@login_required
def new_service(request):
    if request.method == 'POST':
        form = Serviceform(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user_id = request.user
            service.save()
            return redirect('detail_service', pk=service.pk)
    else:
        form = Serviceform()
    return render(request, 'service/new_update_service.html', {'form':form})

@login_required
def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk, user_id=request.user)

    if request.method == 'POST':
        form = Serviceform(request.POST, instance=service)
        if form.is_valid():
            service.save()
            return redirect('detail_service', pk=service.pk)
    else:
        form = Serviceform(instance=service)
        data = {
            'form':form,
            'service': service
        }
        return render(request, 'service/new_update_service.html',data)

@login_required
def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk, user_id=request.user)
    service.active = False
    service.save()
    return redirect('services')
