CREATE TABLE User (
  _id VARCHAR(12) PRIMARY KEY,
  password VARCHAR(20) NOT NULL
);

CREATE TABLE Agency (
  agencyName VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Artist (
  agencyName VARCHAR(30),
  artistName VARCHAR(30),
  isSolo boolean DEFAULT true,
  debutedAt datetime,
  PRIMARY KEY (agencyName, artistName),
  foreign key (agencyName) references Agency(agencyName) ON DELETE CASCADE
);

CREATE TABLE Member (
  artistName VARCHAR(30),
  memberName VARCHAR(30),
  PRIMARY KEY (artistName, memberName),
  foreign key (artistName) references Artist(artistName) ON DELETE CASCADE
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
  albumId int,
  categoryId int,
  PRIMARY KEY (albumId, categoryId),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (categoryId) references Category(categoryId) ON DELETE CASCADE
);

CREATE TABLE Song (
  albumId int,
  songName VARCHAR(30) NOT NULL,
  category int,
  lyrics TEXT,
  createdAt datetime,
  PRIMARY KEY (albumId, songName, category),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (category) references Category(category) ON DELETE CASCADE
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
  albumId int,
  songName VARCHAR(30),
  LyricistId int,
  PRIMARY KEY (albumId, songName, LyricistId),
  foreign key (albumId) references Song(albumId) ON DELETE CASCADE,
  foreign key (songName) references Song(SongName) ON DELETE CASCADE,
  foreign key (LyricistId) references Lyricist(LyricistId) ON DELETE CASCADE
);

CREATE TABLE SongComposer (
  albumId int,
  songName VARCHAR(30),
  composerId int,
  PRIMARY KEY (albumId, songName, composerId),
  foreign key (albumId) references Song(albumId) ON DELETE CASCADE,
  foreign key (songName) references Song(SongName) ON DELETE CASCADE,
  foreign key (composerId) references Composer(composerId) ON DELETE CASCADE
);

CREATE TABLE AlbumReview (
  userId VARCHAR(12),
  albumId int,
  star int DEFAULT 1,
  content TEXT,
  PRIMARY KEY (userId, albumId),
  foreign key (albumId) references Album(albumId) ON DELETE CASCADE,
  foreign key (userId) references User(_id) ON DELETE CASCADE
);

CREATE TABLE SongReview (
  userId VARCHAR(12),
  albumId int,
  songName VARCHAR(30),
  star int DEFAULT 1,
  content TEXT,
  PRIMARY KEY (userId, albumId, songName),
  foreign key (albumId) references Song(albumId) ON DELETE CASCADE,
  foreign key (songName) references Song(SongName) ON DELETE CASCADE,
  foreign key (userId) references User(_id) ON DELETE CASCADE
);