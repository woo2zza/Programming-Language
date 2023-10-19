from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Movie
from .forms import MovieModelForm   
# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieModelForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'movies/form.html', context)

def detail(request, pk):
    pass

def update(request, pk):
    post = get_object_or_404(Movie, id=pk)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('movies:index')
    else:
        form = MovieModelForm(instance=post)
        
    context = {
        'form': form,
    }
    
    return render(request, 'movies/form.html', context)



@require_POST
def delete(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Movie, id=post_id)
        
        if post.user == request.user:
            post.delete()
        
    return redirect('movies:index')

def comments_create(request, pk):
    pass

def comments_delete(request, article_pk, comment_pk):
    pass

def likes(request, article_pk):
    pass