from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from .models import Post
from .forms import PostForm

# Create your views here.
def list_post(request):
    post_list = Post.objects.all()

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