from django.shortcuts import render, redirect, get_object_or_404,  resolve_url
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import *
from .forms import *


def main(request):
    page = request.GET.get('page', '1')  # page
    kw = request.GET.get('kw', '')  # search

    album_list = Album.objects.order_by('albumId')

    if kw:
        album_list = album_list.filter(
            Q(albumName__icontains=kw) |
            Q(albumcategory__categoryId__category__icontains=kw) |
            Q(agencyName__agencyName__icontains=kw)
        ).distinct()
    paginator = Paginator(album_list, 10)
    page_obj = paginator.get_page(page)
    context = {'album_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'main.html', context)


def albumDetail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    artist = Artist.objects.get(agencyName__agencyName=album.agencyName.agencyName, artistName=album.artistName)
    song_list = Song.objects.filter(albumId__albumId=album_id).order_by('id')
    albumReviews = AlbumReview.objects.filter(albumId=album.albumId)

    star = 0
    for review in albumReviews:
        star += review.star
    star = 0.0 if star == 0 else round(star/album.albumreview_set.count())

    stars = []
    i = 0
    for song in song_list.all():
        stars.append(0)
        songReviews = SongReview.objects.filter(songName=song)
        for review in songReviews:
            stars[i] += review.star
        stars[i] = 0.0 if stars[i] == 0 else round(stars[i]/song.songreview_set.count())
        i += 1

    context = {'album': album, 'song_list': song_list, 'artist': artist, 'star': star, 'stars': stars}

    return render(request, 'albumDetail.html', context)


def albumReview(request, album_id):
    page = request.GET.get('page', '1')  # page
    album = get_object_or_404(Album, pk=album_id)
    artist = Artist.objects.get(agencyName__agencyName=album.agencyName.agencyName, artistName=album.artistName)
    reviews = AlbumReview.objects.filter(albumId=album.albumId)

    star = 0
    for review in reviews:
        star += review.star
    star = 0.0 if star == 0 else round(star / album.albumreview_set.count())

    paginator = Paginator(reviews, 10)
    page_obj = paginator.get_page(page)
    context = {'album': album, 'review_list': page_obj, 'artist': artist, 'star': star, 'page': page}
    return render(request, 'albumReview.html', context)


@login_required(login_url='login')
def albumReviewCreate(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    user = User.objects.get(_id=request.user.username)

    if request.method == 'POST':
        form = AlbumReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.userId = user
            review.albumId = album
            review.id = AlbumReview.objects.order_by('id').last().id + 1
            review.save()
            return redirect('albumReview', album.albumId)
    else:
        form = AlbumReviewForm()
    return redirect('albumReview', album.albumId)


def songReview(request, song_id):
    page = request.GET.get('page', '1')  # page
    song = Song.objects.get(id=song_id)
    artist = Artist.objects.get(artistName=song.albumId.artistName)
    reviews = song.songreview_set.all()

    star = 0
    for review in reviews:
        star += review.star
    star = 0.0 if star == 0 else round(star / song.songreview_set.count())
    paginator = Paginator(reviews, 10)
    page_obj = paginator.get_page(page)
    context = {'song': song, 'review_list': page_obj, 'artist': artist, 'star': star}
    return render(request, 'songReview.html', context)


@login_required(login_url='login')
def songReviewCreate(request, song_id):
    song = Song.objects.get(id=song_id)
    user = User.objects.get(_id=request.user.username)

    if request.method == 'POST':
        form = SongReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.userId = user
            review.albumId = song.albumId
            review.songName = song
            review.id = SongReview.objects.order_by('id').last().id + 1
            review.save()
            return redirect('songReview', song.id)
    else:
        form = SongReviewForm()
    return redirect('songReview', song.id)


def artistDetail(request, artist_id):
    page = request.GET.get('page', '1')  # page

    artist = Artist.objects.get(id=artist_id)
    if artist.isSolo:
        member_list = []
    else:
        member_list = artist.member_set.all()

    album_list = Album.objects.filter(
        agencyName__agencyName=artist.agencyName.agencyName,
        artistName=artist.artistName).order_by('albumId')
    paginator = Paginator(album_list, 5)
    page_obj = paginator.get_page(page)

    context = {'artist': artist, 'member_list': member_list, 'album_list': page_obj}
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


@login_required(login_url='login')
def edit(request):
    context = {}
    return render(request, 'admin/adminPage.html', context)
