from django import forms
from .models import Movie, Comment, Recomment


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title','content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie','user')

class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ('content',)