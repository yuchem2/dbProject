CREATE DATABASE musicDB;
USE musicDB;
CREATE TABLE User (
  _id VARCHAR(12) PRIMARY KEY,
  password VARCHAR(20) NOT NULL
);

CREATE TABLE Agency (
  agencyName VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Artist (
  id int,
  agencyName VARCHAR(30),
  artistName VARCHAR(30),
  isSolo boolean DEFAULT true,
  debutedAt datetime,
  PRIMARY KEY (agencyName, artistName),
  foreign key (agencyName) references Agency(agencyName) ON DELETE CASCADE
);

CREATE TABLE Member (
  id int,
  agencyName VARCHAR(30),
  artistName VARCHAR(30),
  memberName VARCHAR(30),
  PRIMARY KEY (artistName, memberName),
  foreign key (agencyName, artistName) references Artist(agencyName, artistName) ON DELETE CASCADE
);

CREATE TABLE Album (
  albumId int PRIMARY KEY,
  albumName VARCHAR(30) NOT NULL,
  artistName VARCHAR(30) NOT NULL,
  agencyName VARCHAR(30) NOT NULL,
  foreign key (agencyName) references Agency(agencyName) ON DELETE CASCADE
);

CREATE TABLE Category (
  categoryId int PRIMARY KEY,
  category VARCHAR(10)
);

CREATE TABLE AlbumCategory (
  id int,
  albumId int,
  categoryId int,
  PRIMARY KEY (albumId, categoryId),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (categoryId) references Category(categoryId) ON DELETE CASCADE
);

CREATE TABLE Song (
  id int,
  albumId int,
  songName VARCHAR(30) NOT NULL,
  categoryId int,
  lyrics TEXT,
  createdAt datetime,
  PRIMARY KEY (albumId, songName, categoryId),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (categoryId) references Category(categoryId) ON DELETE CASCADE
);

CREATE TABLE Lyricist (
  lyricistId int PRIMARY KEY,
  lyricistName VARCHAR(30)
);

CREATE TABLE Composer (
  composerId int PRIMARY KEY,
  composerName VARCHAR(30)
);

CREATE TABLE SongLyricist (
  id int,
  albumId int,
  songName VARCHAR(30),
  LyricistId int,
  PRIMARY KEY (albumId, songName, LyricistId),
  foreign key (albumId, songName) references Song(albumId, songName) ON DELETE CASCADE,
  foreign key (LyricistId) references Lyricist(LyricistId) ON DELETE CASCADE
);

CREATE TABLE SongComposer (
  id int,
  albumId int,
  songName VARCHAR(30),
  composerId int,
  PRIMARY KEY (albumId, songName, composerId ),
  foreign key (albumId, songName) references Song(albumId, songName) ON DELETE CASCADE,
  foreign key (composerId) references Composer(composerId) ON DELETE CASCADE
);

CREATE TABLE AlbumReview (
  id int,
  userId VARCHAR(12),
  albumId int,
  star int DEFAULT 1,
  content TEXT,
  PRIMARY KEY (userId, albumId),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (userId) references User(_id) ON DELETE CASCADE
);

CREATE TABLE SongReview (
  id int,
  userId VARCHAR(12),
  albumId int,
  songName VARCHAR(30),
  star int DEFAULT 1,
  content TEXT,
  PRIMARY KEY (userId, albumId, songName),
  foreign key (albumId, songName) references Song(albumId, songName) ON DELETE CASCADE,
  foreign key (userId) references User(_id) ON DELETE CASCADE
);