from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'Patrick',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 9, 2021'
    },
    {
        'author': 'Patrick',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 9, 2021'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
