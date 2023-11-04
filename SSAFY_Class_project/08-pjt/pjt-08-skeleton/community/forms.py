from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    rank = forms.DecimalField(
        label="score",
        max_value=10,
        min_value=0,
        widget=forms.NumberInput(attrs={"step":0.5})
    )
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['review', 'user']


class ReCommentForm(forms.ModelForm):
    content = forms.CharField(
        label="대댓글",
        widget=forms.TextInput(attrs={'style': 'width: 80%;'}),

    )
    class Meta:
        model = Comment
        fields = ('content',)



        # 대댓글 view까지 완. html 수정 , recommended 뷰함수 , html , 리드미