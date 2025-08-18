from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    last_posts = posts.order_by('-id')[:5]
    return render(request, 'home.html', {'posts': last_posts})

def posts(request, page=1):
    posts = Post.objects.all().order_by('-id')
    paginator = Paginator(posts, 5)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj =  paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'posts.html', {'page_obj': page_obj})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

