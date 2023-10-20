from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_safe, require_http_methods
from .models import Movie, Comment, Recomment
from .forms import MovieModelForm, CommentForm , RecommentForm
from django.contrib.auth import get_user_model
# Create your views here.
@login_required
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@login_required
@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            movie = form.save(commit= False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk )
    else:
        form = MovieModelForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'movies/form.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    recomment_form = RecommentForm()
    recomments = movie.recomment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments' : comments,
        'recomment_form' : recomment_form,
        'recomments' : recomments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(['GET','POST'])
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.user == movie.user:
        if request.method == 'POST':
            form = MovieModelForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieModelForm(instance = movie)
    else:
        return redirect('movies:index')
    
    context = {
        'movie': movie,
        'form': form,
    }
    
    return render(request, 'movies/form.html', context)



@require_POST
def delete(request, movie_id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, id=movie_id)
        
        if movie.user == request.user:
            movie.delete()
        
    return redirect('movies:index')


@login_required
def comments_create(request,pk):
    movie = Movie.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit = False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
        return redirect('movies:detail', movie.pk)
    context = {
        'movie' : movie,
        'comment_form' : comment_form
    }
    return render(request, 'movies/detail.html', context)

@require_POST
def comments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)



@login_required
def likes(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    return redirect('movies:index')

@login_required
@require_POST
def recomments_create(request, pk, comment_pk):
    movie = Movie.objects.get(pk = pk)
    comment = Comment.objects.get(pk = comment_pk)
    form = RecommentForm(request.POST)
    if form.is_valid():
        recomment = form.save(commit = False)
        recomment.user = request.user
        recomment.movie = movie
        recomment.comment = comment
        recomment.save()
        return redirect('movies:detail' , movie.pk)
    context = {
            'movie' : movie,
            'form' : form,
            'comment' : comment
        }
    return render(request, 'movies/detail.html', context)


@require_POST
def recomments_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('movies:detail', movie_pk)