from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Album)
admin.site.register(Agency)
admin.site.register(Artist)
admin.site.register(AlbumReview)
admin.site.register(AlbumCategory)
admin.site.register(Category)
admin.site.register(Composer)
admin.site.register(Lyricist)
admin.site.register(Member)
admin.site.register(Song)
admin.site.register(SongReview)
admin.site.register(SongComposer)
admin.site.register(SongLyricist)

