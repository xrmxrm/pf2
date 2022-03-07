from django.shortcuts import render
from .models import Post

def all_posts(request):
    posts = Post.objects.order_by('-date')[:3]
    return render(request, 'blog/all_posts.html', {'posts':posts})
