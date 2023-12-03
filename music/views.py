from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *


def main(request):
    page = request.GET.get('page', '1')  # page
    kw = request.GET.get('kw', '')  # search
    sort = request.GET.get('sort', 'recent')

    if sort == 'hot':
        album_list = Album.objects.order_by('albumreview__star')
    else:
        album_list = Album.objects.order_by('albumId')

    if kw:
        album_list = album_list.filter(
            Q(albumName__icontains=kw) |
            Q(albumcategory__categoryId__category__icontains=kw) |
            Q(agencyName__agencyName__icontains=kw)
        ).distinct()
    paginator = Paginator(album_list, 10)
    page_obj = paginator.get_page(page)
    context = {'album_list': page_obj, 'page': page, 'kw': kw, 'sort': sort}

    return render(request, 'main.html', context)


def albumDetail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artist = Artist.objects.get(agencyName__agencyName=album.agencyName.agencyName, artistName=album.artistName)
    song_list = Song.objects.filter(albumId=album.albumId)

    star = 0
    for review in album.albumreview_set.all():
        star += review.star
    star = 0.0 if star == 0 else round(star/album.albumreview_set.count())
    context = {'album': album, 'song_list': song_list, 'artist': artist, 'star': star}

    return render(request, 'albumDetail.html', context)


def artistDetail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    if artist.isSolo:
        member_list = Member.objects.filter(agencyName__agencyName=artist.agencyName.agencyName, artistName__artistName=artist.artistName)
    else:
        member_list = []

    context = {'artist': artist, 'member_list': member_list}
    return render(request, 'artistDetail.html', context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            User.objects.create(userId=username, password=raw_password)
            user = authenticate(username=username, password=raw_password)   # 사용자 인증
            login(request, user)    # 로그인
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

