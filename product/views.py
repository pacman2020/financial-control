from functools import reduce
from product.models import Product
from task.models import Task
from django.core.paginator import Paginator
from django.shortcuts import render

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