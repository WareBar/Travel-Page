from django.shortcuts import render
from .models import Post

# Create your views here.

def post(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'POST/post_page.html',{
        'post':post
    })