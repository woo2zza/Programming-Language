from rest_framework import serializers
from .models import Comment, Review



# 리뷰 전체
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)


# 리뷰 세부내용
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




# 영화 세부내용
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'





