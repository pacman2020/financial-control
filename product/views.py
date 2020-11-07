from functools import reduce

from django.contrib.auth.decorators import login_required
from product.models import Product
from django.core.paginator import Paginator
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



# Create your views here.
def products(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    data = {
        'products': paginator.get_page(page)
    }

    return render(request, 'product/list_product.html', data)

# @login_required
def detail_product(request, pk):
    try:
        product = get_object_or_404(Product,pk=pk)
        data = {
            'product': product
        }
        return render(request, 'product/detail_product.html',data)
    except:
        return redirect('products')