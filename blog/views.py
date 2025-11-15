from django.shortcuts import render, get_object_or_404
from .models import Post
from home.models import Profile

def post_list(request):
    posts = Post.objects.all()
    profile = Profile.objects.first()
    return render(request, 'blog/post_list.html', {'posts': posts, 'profile': profile})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = Profile.objects.first()
    posts = Post.objects.exclude(pk=pk)  # برای مقالات مرتبط
    return render(request, 'blog/post_detail.html', {'post': post, 'profile': profile, 'posts': posts})