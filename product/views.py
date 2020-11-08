from functools import reduce
from django.contrib.auth.decorators import login_required
from .models import Product
from django.core.paginator import Paginator
from .forms import Productform
from django.shortcuts import get_object_or_404, redirect, render

# def daily_company_value(cashier):
#     if cashier:
#         company = reduce(lambda x, y: x+y,cashier)
#         return company
#     else:
#         return None

# cashier_company = []
# cashier_company.append(x.task_id.company)
# cashier_company = daily_company_value(cashier_company)


@login_required
def products(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    data = {
        'products': paginator.get_page(page)
    }

    return render(request, 'product/list_product.html', data)

@login_required
def detail_product(request, pk):
    try:
        product = get_object_or_404(Product,pk=pk)
        data = {
            'product': product
        }
        return render(request, 'product/detail_product.html',data)
    except:
        return redirect('products')

def new_product(request):
    if request.method == 'POST':
        form = Productform(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user_id = request.user
            service.save()
            return redirect('detail_product', pk=service.pk)
    else:
        form = Productform()
    return render(request, 'product/new_update_product.html', {'form':form})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user_id=request.user)

    if request.method == 'POST':
        form = Productform(request.POST, instance=product)
        if form.is_valid():
            product.save()
            return redirect('detail_product', pk=product.pk)
    else:
        form = Productform(instance=product)
        data = {
            'form':form,
            'product': product
        }
        return render(request, 'product/new_update_product.html',data)

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user_id=request.user)
    product.active = False
    product.save()
    return redirect('products')