"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from music import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main, name='main'),

    # admin
    path('admin/main', views.adminMain, name='admin_main'),
    path('admin/agency/', views.adminAgency, name='admin_agency'),
    path('admin/artist/', views.adminAritst, name='admin_artist'),
    path('admin/album/', views.adminAlbum, name='admin_album'),
    path('admin/album/<int:album_id>/song/', views.adminSong, name='admin_song'),
    path('admin/album/review/', views.adminAlbumReview, name='admin_album_review'),
    path('admin/song/review/', views.adminSongReview, name='admin_song_review'),
    path('admin/album/<int:album_id>/delete', views.adminAlbumDelete, name='admin_album_delete'),
    path('admin/song/<int:song_id>/delete', views.adminSongDelete, name='admin_song_delete'),
    path('admin/album/review/<int:review_id>/delete/', views.adminAlbumReviewDelete, name='admin_album_review_delete'),
    path('admin/song/review/<int:review_id>/delete/', views.adminSongReviewDelete, name='admin_song_review_delete'),
    path('admin/', admin.site.urls),

    # User
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

    # Album
    path('album/<int:album_id>/', views.albumDetail, name='album'),
    path('album/<int:album_id>/review/', views.albumReview, name='albumReview'),
    path('album/<int:album_id>/review/create/', views.albumReviewCreate, name='albumReview_create'),
    path('album/review/<int:review_id>/', views.albumReviewModify, name='albumReview_modify'),
    path('song/<int:song_id>/review/', views.songReview, name='songReview'),
    path('song/<int:song_id>/review/create/', views.songReviewCreate, name='songReview_create'),
    path('song/review/<int:review_id>/', views.songReviewModify, name='songReview_modify'),

    # Artist
    path('artist/<int:artist_id>', views.artistDetail, name='artist')

]
