from django.shortcuts import render, redirect, get_object_or_404,  resolve_url
from django.contrib import messages
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


@login_required(login_url='login')
def albumReviewModify(request, review_id):
    review = get_object_or_404(AlbumReview, pk=review_id)

    if review.userId._id != request.user.username:
        messages.error(request, '수정권한이 없습니다')
        return redirect('albumReview', album_id=review.albumId.albumId)
    if request.method == "POST":
        form = AlbumReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            review.save()
            return redirect("albumReview", album_id=review.albumId.albumId)
    else:
        form = AlbumReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'reviewForm.html', context)


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


@login_required(login_url='login')
def songReviewModify(request, review_id):
    review = get_object_or_404(SongReview, pk=review_id)

    if review.userId._id != request.user.username:
        messages.error(request, '수정권한이 없습니다')
        return redirect('songReview', song_id=review.songName.id)
    if request.method == "POST":
        form = SongReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            review.save()
            return redirect("songReview", song_id=review.songName.id)
    else:
        form = SongReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'reviewForm.html', context)


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
            user = User.objects.create(userId=username, password=raw_password)
            user.save()
            user = authenticate(username=username, password=raw_password)   # 사용자 인증
            login(request, user)    # 로그인
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def adminMain(request):
    if request.user.username != 'admin':
        return redirect('main')
    return render(request, 'admin/adminPage.html')


@login_required(login_url='login')
def adminAgency(request):
    if request.user.username != 'admin':
        return redirect('main')

    if request.method == 'POST':
        form = AgencyForm(request.POST)
        if form.is_valid():
            agency = form.save(commit=False)
            agency.save()
            return redirect(adminAgency)
    else:
        form = AgencyForm()

    agency_list = Agency.objects.all()
    context = {'agency_list': agency_list, 'form': form}
    return render(request, 'admin/adminAgency.html', context)


@login_required(login_url='login')
def adminAritst(request):
    if request.user.username != 'admin':
        return redirect('main')
    agency_list = Agency.objects.all()
    artist_list = Artist.objects.all().order_by('id')
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            agencyName = form.cleaned_data.get('agencyName')
            agency = Agency.objects.filter(agencyName=agencyName).all()[0]
            artistName = form.cleaned_data.get('artistName')
            isSolo = form.cleaned_data.get('isSolo')
            debutedAt = form.cleaned_data.get('debutedAt')
            id = artist_list.last().id + 1
            artist = Artist.objects.create(
                id=id,
                agencyName=agency,
                artistName=artistName,
                isSolo=isSolo,
                debutedAt=debutedAt
            )
            artist.save()
            if isSolo == 0:
                member_list = form.cleaned_data.get('members').split(', ')
                id = Member.objects.order_by('id').last().id + 1
                for member in member_list:
                    Member.objects.create(
                        id=id,
                        agencyName=agency,
                        artistName=artist,
                        memberName=member
                    ).save()
                    id += 1
            return redirect('admin_artist')
    else:
        form = ArtistForm()

    context = {'agency_list': agency_list, 'artist_list': artist_list, 'form': form}
    return render(request, 'admin/adminArtist.html', context)


@login_required(login_url='login')
def adminAlbum(request):
    if request.user.username != 'admin':
        return redirect('main')

    agency_list = Agency.objects.all()
    artist_list = Artist.objects.all().order_by('id')
    album_list = Album.objects.all().order_by('albumId')
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data.get('albumId')
            agencyName = form.cleaned_data.get('agencyName')
            artistName = form.cleaned_data.get('artistName')
            albumName = form.cleaned_data.get('albumName')
            agency = Agency.objects.get(agencyName=agencyName)
            album = Album.objects.create(
                albumId=id,
                agencyName=agency,
                artistName=artistName,
                albumName=albumName,
            )
            album.save()
            id = AlbumCategory.objects.last().id + 1
            category_list = form.cleaned_data.get('categories').split(',')
            for category in category_list:
                search = Category.objects.filter(category=category)
                if not search:
                    c_id = Category.objects.last().categoryId + 1
                    search = Category.objects.create(categoryId=c_id, category=category)
                else:
                    search = search[0]
                AlbumCategory.objects.create(
                    id=id,
                    albumId=album,
                    categoryId=search
                ).save()

                id += 1
            return redirect('admin_album')
    else:
        form = AlbumForm()

    context = {'agency_list': agency_list, 'artist_list': artist_list, 'album_list': album_list, 'form': form}
    return render(request, 'admin/adminAlbum.html', context)


@login_required(login_url='login')
def adminSong(request, album_id):
    if request.user.username != 'admin':
        return redirect('main')
    album = get_object_or_404(Album, pk=album_id)
    artist = Artist.objects.get(agencyName__agencyName=album.agencyName.agencyName, artistName=album.artistName)
    song_list = Song.objects.filter(albumId=album).order_by('id')
    category_list = Category.objects.all()

    star = 0
    for review in album.albumreview_set.all():
        star += review.star
    star = 0.0 if star == 0 else round(star / album.albumreview_set.count())

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            id = Song.objects.all().order_by('id').last().id + 1
            songName = form.cleaned_data.get('songName')
            categoryId = form.cleaned_data.get('category')
            lyrics = form.cleaned_data.get('lyrics')
            createdAt = form.cleaned_data.get('createdAt')

            category = Category.objects.get(categoryId=categoryId)
            song = Song.objects.create(
                id=id,
                albumId=album,
                songName=songName,
                categoryId=category,
                lyrics=lyrics,
                createdAt=createdAt
            )
            song.save()
            composer_list = form.cleaned_data.get('composers')
            if composer_list:
                composer_list = composer_list.split(',')
                id = SongComposer.objects.last().id + 1
                for composer in composer_list:
                    search = Composer.objects.filter(composerName=composer)
                    if not search:
                        c_id = Composer.objects.last().composerId + 1
                        search = Composer.objects.create(composerId=c_id, composerName=composer)
                    else:
                        search = search[0]
                    SongComposer.objects.create(
                        id=id,
                        albumId=album,
                        songName=song,
                        composerId=search
                    ).save()

                    id += 1
            lyricist_list = form.cleaned_data.get('lyricists')
            if lyricist_list:
                lyricist_list = lyricist_list.split(',')
                id = SongLyricist.objects.last().id + 1

                for lyricist in lyricist_list:
                    search = Lyricist.objects.filter(lyricistName=lyricist)
                    if not search:
                        c_id = Lyricist.objects.last().lyricistId + 1
                        search = Lyricist.objects.create(lyricistId=c_id, lyricistName=lyricist)
                    else:
                        search = search[0]
                    SongLyricist.objects.create(
                        id=id,
                        albumId=album,
                        songName=song,
                        lyricistId=search
                    ).save()

                    id += 1
            return redirect('admin_song', album_id=album_id)
    else:
        form = SongForm()

    context = {'album': album, 'artist': artist, 'song_list': song_list, 'category_list': category_list,
               'star': star, 'form': form}
    return render(request, 'admin/adminSong.html', context)


@login_required(login_url='login')
def adminAlbumReview(request):
    if request.user.username != 'admin':
        return redirect('main')
    review_list = AlbumReview.objects.all()
    context = {'review_list': review_list, }

    return render(request, 'admin/adminAlbumReview.html', context)


@login_required(login_url='login')
def adminSongReview(request):
    if request.user.username != 'admin':
        return redirect('main')
    review_list = SongReview.objects.all()
    context = {'review_list': review_list, }

    return render(request, 'admin/adminSongReview.html', context)


@login_required(login_url='login')
def adminAlbumReviewDelete(request, review_id):
    if request.user.username != 'admin':
        return redirect('main')
    review = get_object_or_404(AlbumReview, pk=review_id)
    review.delete()
    return redirect('admin_album_review')


@login_required(login_url='login')
def adminSongReviewDelete(request, review_id):
    if request.user.username != 'admin':
        return redirect('main')
    review = get_object_or_404(SongReview, pk=review_id)
    review.delete()
    return redirect('admin_song_review')


@login_required(login_url='login')
def adminAlbumDelete(request, album_id):
    if request.user.username != 'admin':
        return redirect('main')
    album = get_object_or_404(Album, pk=album_id)
    album.delete()
    return redirect('admin_album')


@login_required(login_url='login')
def adminSongDelete(request, song_id):
    if request.user.username != 'admin':
        return redirect('main')
    song = Song.objects.get(id=song_id)
    album_id = song.albumId.albumId
    song.delete()
    return redirect('admin_song', album_id=album_id)
