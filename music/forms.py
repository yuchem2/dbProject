from django import forms
from .models import *


class SongReviewForm(forms.ModelForm):
    class Meta:
        model = SongReview
        fields = ['star', 'content']


class AlbumReviewForm(forms.ModelForm):
    class Meta:
        model = AlbumReview
        fields = ['star', 'content']


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['agencyName']


class ArtistForm(forms.Form):
    agencyName = forms.CharField(max_length=30)
    artistName = forms.CharField(max_length=30)
    isSolo = forms.IntegerField()
    members = forms.CharField(max_length=100)
    debutedAt = forms.DateTimeField()


class AlbumForm(forms.Form):
    albumId = forms.IntegerField()
    albumName = forms.CharField(max_length=30)
    artistName = forms.CharField(max_length=30)
    agencyName = forms.CharField(max_length=30)
    categories = forms.CharField(max_length=100)


class SongForm(forms.Form):
    songName = forms.CharField(max_length=30)
    category = forms.IntegerField()
    lyrics = forms.CharField(widget=forms.Textarea)
    lyricists = forms.CharField(max_length=100, required=False)
    composers = forms.CharField(max_length=100, required=False)
    createdAt = forms.DateTimeField()

