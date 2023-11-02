from django.shortcuts import render
from django.views.decorators.http import require_safe
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer, GenreSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import MovieForm

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
    movies = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)



@require_safe
def recommended(request):
    pass
