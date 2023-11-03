from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie, Genre
from rest_framework import status
from .serializers import MovieListSerializer, MovieSerializer, GenreSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all().order_by('-pk')
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie_genre = movie.genres.all()
    context = {
        'movie' : movie,
        'movie_genre' : movie_genre
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    pass
