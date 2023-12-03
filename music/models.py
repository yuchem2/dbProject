from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.CharField(db_column='userId', primary_key=True, max_length=12)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user'


class Agency(models.Model):
    agencyName = models.CharField(db_column='agencyName', primary_key=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'Agency'


class Artist(models.Model):
    agencyName = models.OneToOneField(Agency, models.DO_NOTHING, db_column='agencyName')
    artistName = models.CharField(db_column='artistName', max_length=30)  # Field name made lowercase.
    isSolo = models.IntegerField(db_column='isSolo', blank=True, null=True)  # Field name made lowercase.
    debutedAt = models.DateTimeField(db_column='debutedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Artist'
        unique_together = (('agencyName', 'artistName'),)


class Member(models.Model):
    agencyName = models.ForeignKey(Artist, models.DO_NOTHING, db_column='agencyName', related_name='Agency_agencyName')
    artistName = models.OneToOneField(Artist, models.DO_NOTHING, db_column='artistName')
    memberName = models.CharField(db_column='memberName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Member'
        unique_together = (('artistName', 'memberName'),)


class Album(models.Model):
    albumId = models.IntegerField(db_column='albumId', primary_key=True)  # Field name made lowercase.
    albumName = models.CharField(db_column='albumName', max_length=30)  # Field name made lowercase.
    artistName = models.CharField(db_column='artistName', max_length=30)  # Field name made lowercase.
    agencyName = models.ForeignKey(Agency, models.DO_NOTHING, db_column='agencyName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Album'


class Category(models.Model):
    categoryId = models.IntegerField(db_column='categoryId', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Category'


class AlbumCategory(models.Model):
    albumId = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumId')  # Field name made lowercase.
    categoryId = models.ForeignKey('Category', models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlbumCategory'
        unique_together = (('albumId', 'categoryId'),)


class Composer(models.Model):
    composerId = models.IntegerField(db_column='composerId', primary_key=True)  # Field name made lowercase.
    composerName = models.CharField(db_column='composerName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'composer'


class Lyricist(models.Model):
    lyricistId = models.IntegerField(db_column='lyricistId', primary_key=True)  # Field name made lowercase.
    lyricistName = models.CharField(db_column='lyricistName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Lyricist'


class Song(models.Model):
    albumId = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumId')  # Field name made lowercase.
    songName = models.CharField(db_column='songName', max_length=30, unique=True)  # Field name made lowercase.
    categoryId = models.ForeignKey(Category, models.DO_NOTHING, db_column='categoryId')  # Field name made lowercase.
    lyrics = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Song'
        unique_together = (('albumId', 'songName', 'categoryId'),)


class SongComposer(models.Model):
    albumId = models.ForeignKey(Song, models.DO_NOTHING, db_column='albumId')
    songName = models.ForeignKey(Song, models.DO_NOTHING, db_column='songName', to_field='songName', related_name="+")
    composerId = models.ForeignKey(Composer, models.DO_NOTHING, db_column='composerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'songComposer'
        unique_together = (('albumId', 'songName', 'composerId'),)


class SongLyricist(models.Model):
    albumId = models.ForeignKey(Song, models.DO_NOTHING, db_column='albumId')
    songName = models.ForeignKey(Song, models.DO_NOTHING, db_column='songName', to_field='songName', related_name="+")
    lyricistId = models.ForeignKey(Lyricist, models.DO_NOTHING, db_column='LyricistId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'songLyricist'
        unique_together = (('albumId', 'songName', 'lyricistId'),)


class SongReview(models.Model):
    userId = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    albumId = models.ForeignKey(Song, models.DO_NOTHING, db_column='albumId', related_name="+")
    songName = models.ForeignKey(Song, models.DO_NOTHING, db_column='songName', to_field='songName', related_name="+")
    star = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'songReview'
        unique_together = (('userId', 'albumId', 'songName'),)


class AlbumReview(models.Model):
    userId = models.ForeignKey('User', models.DO_NOTHING, db_column='userId')  # Field name made lowercase.
    albumId = models.ForeignKey(Album, models.DO_NOTHING, db_column='albumId')  # Field name made lowercase.
    star = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AlbumReview'
        unique_together = (('userId', 'albumId'),)
