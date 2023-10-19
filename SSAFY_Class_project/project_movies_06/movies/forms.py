from django import forms
from .models import Movie


class MovieModelForm(forms.ModelForm):
   
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'What are you doing?',
            }
        )
    )

    class Meta:
        model = Movie
        fields = ['content']