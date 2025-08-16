from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.all()
    last_posts = posts.order_by('-id')[:5]
    return render(request, 'home.html', {'posts': last_posts})

def posts(request):
    return render(request, 'posts.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})