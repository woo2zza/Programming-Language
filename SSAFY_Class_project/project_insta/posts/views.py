from .models import Post
from .forms import PostModelForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostModelForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'posts/form.html', context)


@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostModelForm(instance=post)
        
    context = {
        'form': form,
    }
    
    return render(request, 'posts/form.html', context)


@require_POST
def delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        
        if post.user == request.user:
            post.delete()
        
    return redirect('posts:index')