from rest_framework import serializers
from .models import Movie, Review, Actor

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)


class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)

    class ReveiwSetSerializer(serializers.ModelSerializer): 
            model = Review
            fields = ('title', 'content',)

    actors = ActorNameSerializer(many=True, read_only=True)
    review_set = ReveiwSetSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'






class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name',)


class ActorSerializer(serializers.ModelSerializer):

    class MovieTextSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieTextSerializer(many=True, read_only = True)

    class Meta:
        model = Actor
        fields = '__all__'