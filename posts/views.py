from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, 'index.html', context)

def post(request, pk):
    context = {
        'posts': Post.objects.get(id=pk)
    }
    
    return render(request, 'post.html', context)
