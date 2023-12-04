from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class AgencyAdmin(admin.ModelAdmin):
    list_display = ['agencyName']


class CatgoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'categoryId']


class ComposerAdmin(admin.ModelAdmin):
    list_display = ['composerName', 'composerId']


class LyricistsAdmin(admin.ModelAdmin):
    list_display = ['lyricistName', 'lyricistId']


class MemberAdmin(admin.ModelAdmin):
    list_display = ['memberName', 'artistName', 'agencyName']


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['albumName', 'artistName', 'agencyName']


class SongAdmin(admin.ModelAdmin):
    list_display = ['songName', 'id']

admin.site.register(User)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Agency, AgencyAdmin)
admin.site.register(Artist)
admin.site.register(AlbumReview)
admin.site.register(AlbumCategory)
admin.site.register(Category, CatgoryAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(Lyricist, LyricistsAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(SongReview)
admin.site.register(SongComposer)
admin.site.register(SongLyricist)

