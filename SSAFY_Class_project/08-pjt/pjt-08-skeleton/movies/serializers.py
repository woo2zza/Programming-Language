from rest_framework import serializers
from . models import Movie, Genre


# 영화 전체
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields= '__all__'


# 영화 세부내용
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'




# 장르 세부내용
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
