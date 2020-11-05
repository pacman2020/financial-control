from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm
from django.utils import timezone
from functools import reduce

def daily_value(employee_data):
    '''
        sum of the earnings of each employee to 
        return a dictionary from each of them
    '''
    new_list = {}
    for x in employee_data:
        for key,value in x.items():
            if key in new_list:
                a = (new_list[key] + value)
                new_list[key] = a
            else:
                new_list[key] = value

    return new_list

def formatting_employee_data(lista):
    '''
        organizes and returns the data in a dictionary
        list to be displayed on the screen
    '''
    chaves = []
    novo_obj = []
    for x in lista:
        chaves.append(x)
        novo_obj.append({ 
                'names': x,
                'prices': lista[x]
            })
    return novo_obj


def list_post(request):
    data_at = str(timezone.now())[:10]
    new_list_posts = []
    new_list_employees = []
    post_list = Post.objects.order_by('-create_at')

    #search for dates
    if request.method == 'POST':
        search_data = str(request.POST.get('search'))
        if search_data:
            for x in post_list:
                if str(x.create_at)[:10] == search_data:
                    new_list_employees.append({ x.employee_id.full_name : float(x.task_id.price)})
                    new_list_posts.append(x)

            employees = daily_value(new_list_employees)
            new_formatted_employees = formatting_employee_data(employees)

            paginator = Paginator(new_list_posts, 10)
            page = request.GET.get('page')

            data = {
                'posts': paginator.get_page(page),
                'data_at': search_data,
                'employees': new_formatted_employees
                }
            return render(request, 'post/list_post.html', data)
    
    for x in post_list:
        if str(x.create_at)[:10] == data_at:
            new_list_employees.append({ x.employee_id.full_name : float(x.task_id.price)})
            new_list_posts.append(x)

    employees = daily_value(new_list_employees)
    new_formatted_employees = formatting_employee_data(employees)

    paginator = Paginator(new_list_posts, 10)
    page = request.GET.get('page')

    data = {
        'posts': paginator.get_page(page),
        'data_at': data_at,
        'employees': new_formatted_employees
    }
    return render(request, 'post/list_post.html', data)

def detail_post(request, pk):
    try:
        post = get_object_or_404(Post,pk=pk)
        data = {
            'post': post
        }
        return render(request, 'post/detail_post.html',data)
    except:
        return redirect('posts')

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post/new_update_post.html', {'form':form})

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user_id=request.user)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('detail_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
        data = {
            'form':form,
            'post': post
        }
        return render(request, 'post/new_update_post.html',data)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk, user_id=request.user)
    post.delete()
    return redirect('posts')