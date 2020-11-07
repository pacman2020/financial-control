from product.models import Product
from task.models import Task
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
def products(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 10)
    page = request.GET.get('page')
    data = {
        'products': paginator.get_page(page)
    }

    return render(request, 'product/list_product.html', data)