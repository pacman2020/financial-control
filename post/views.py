from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

def list_post(request):
    post_list = Post.objects.order_by('-create_at')

    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    data = {
        'posts': paginator.get_page(page)
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