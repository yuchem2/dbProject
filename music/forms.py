from django import forms
from .models import SongReview, AlbumReview


class SongReviewForm(forms.ModelForm):
    class Meta:
        model = SongReview
        fields = ['star', 'content']


class AlbumReviewForm(forms.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ['star', 'content']
