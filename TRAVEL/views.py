from django.shortcuts import render
from POST.models import Post


def home(request):
    return render(request, 'home.html',{
        'posts':Post.objects.all()
    })