from rest_framework import serializers
from .models import Movie, Review, Actor


# 영화 전체
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title','overview',)




# 영화 세부내용
class MovieSerializer(serializers.ModelSerializer):
    class ActorNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors = ActorNameSerializer(many = True, read_only=True)

    class ReveiwSetSerializer(serializers.ModelSerializer): 
        class Meta:
            model = Review
            fields = ('title', 'content',)

    review_set = ReveiwSetSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'





# 리뷰 전체
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)





# 리뷰 세부내용
class ReviewSerializer(serializers.ModelSerializer):
    class MovieTextSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    movie = MovieTextSerializer(read_only = True)

    class Meta: 
        model = Review
        fields = '__all__'








# 배우 전체
class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name',)



# 배우 세부내용
class ActorSerializer(serializers.ModelSerializer):
    class MovieTextSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieTextSerializer(many=True, read_only = True)

    class Meta:
        model = Actor
        fields = '__all__'