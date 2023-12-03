CREATE DATABASE  IF NOT EXISTS `musicdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `musicdb`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: musicdb
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agency`
--

DROP TABLE IF EXISTS `agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agency` (
  `agencyName` varchar(30) NOT NULL,
  PRIMARY KEY (`agencyName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agency`
--

LOCK TABLES `agency` WRITE;
/*!40000 ALTER TABLE `agency` DISABLE KEYS */;
/*!40000 ALTER TABLE `agency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `album` (
  `albumId` int NOT NULL,
  `albumName` varchar(30) NOT NULL,
  `artistName` varchar(30) NOT NULL,
  `agencyName` varchar(30) NOT NULL,
  PRIMARY KEY (`albumId`),
  KEY `agencyName` (`agencyName`),
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`agencyName`) REFERENCES `agency` (`agencyName`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albumcategory`
--

DROP TABLE IF EXISTS `albumcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albumcategory` (
  `id` int DEFAULT NULL,
  `albumId` int NOT NULL,
  `categoryId` int NOT NULL,
  PRIMARY KEY (`albumId`,`categoryId`),
  KEY `categoryId` (`categoryId`),
  CONSTRAINT `albumcategory_ibfk_1` FOREIGN KEY (`albumId`) REFERENCES `album` (`albumId`) ON DELETE CASCADE,
  CONSTRAINT `albumcategory_ibfk_2` FOREIGN KEY (`categoryId`) REFERENCES `category` (`categoryId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albumcategory`
--

LOCK TABLES `albumcategory` WRITE;
/*!40000 ALTER TABLE `albumcategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `albumcategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `albumreview`
--

DROP TABLE IF EXISTS `albumreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `albumreview` (
  `id` int DEFAULT NULL,
  `userId` varchar(12) NOT NULL,
  `albumId` int NOT NULL,
  `star` int DEFAULT '1',
  `content` text,
  PRIMARY KEY (`userId`,`albumId`),
  KEY `albumId` (`albumId`),
  CONSTRAINT `albumreview_ibfk_1` FOREIGN KEY (`albumId`) REFERENCES `album` (`albumId`) ON DELETE CASCADE,
  CONSTRAINT `albumreview_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `user` (`_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `albumreview`
--

LOCK TABLES `albumreview` WRITE;
/*!40000 ALTER TABLE `albumreview` DISABLE KEYS */;
/*!40000 ALTER TABLE `albumreview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artist` (
  `id` int DEFAULT NULL,
  `agencyName` varchar(30) NOT NULL,
  `artistName` varchar(30) NOT NULL,
  `isSolo` tinyint(1) DEFAULT '1',
  `debutedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`agencyName`,`artistName`),
  CONSTRAINT `artist_ibfk_1` FOREIGN KEY (`agencyName`) REFERENCES `agency` (`agencyName`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `categoryId` int NOT NULL,
  `category` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`categoryId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `composer`
--

DROP TABLE IF EXISTS `composer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `composer` (
  `composerId` int NOT NULL,
  `composerName` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`composerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `composer`
--

LOCK TABLES `composer` WRITE;
/*!40000 ALTER TABLE `composer` DISABLE KEYS */;
/*!40000 ALTER TABLE `composer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lyricist`
--

DROP TABLE IF EXISTS `lyricist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lyricist` (
  `lyricistId` int NOT NULL,
  `lyricistName` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`lyricistId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lyricist`
--

LOCK TABLES `lyricist` WRITE;
/*!40000 ALTER TABLE `lyricist` DISABLE KEYS */;
/*!40000 ALTER TABLE `lyricist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` int DEFAULT NULL,
  `agencyName` varchar(30) DEFAULT NULL,
  `artistName` varchar(30) NOT NULL,
  `memberName` varchar(30) NOT NULL,
  PRIMARY KEY (`artistName`,`memberName`),
  KEY `agencyName` (`agencyName`,`artistName`),
  CONSTRAINT `member_ibfk_1` FOREIGN KEY (`agencyName`, `artistName`) REFERENCES `artist` (`agencyName`, `artistName`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `song`
--

DROP TABLE IF EXISTS `song`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `song` (
  `id` int DEFAULT NULL,
  `albumId` int NOT NULL,
  `songName` varchar(30) NOT NULL,
  `categoryId` int NOT NULL,
  `lyrics` text,
  `createdAt` datetime DEFAULT NULL,
  PRIMARY KEY (`albumId`,`songName`,`categoryId`),
  KEY `categoryId` (`categoryId`),
  CONSTRAINT `song_ibfk_1` FOREIGN KEY (`albumId`) REFERENCES `album` (`albumId`) ON DELETE CASCADE,
  CONSTRAINT `song_ibfk_2` FOREIGN KEY (`categoryId`) REFERENCES `category` (`categoryId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `song`
--

LOCK TABLES `song` WRITE;
/*!40000 ALTER TABLE `song` DISABLE KEYS */;
/*!40000 ALTER TABLE `song` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songcomposer`
--

DROP TABLE IF EXISTS `songcomposer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songcomposer` (
  `id` int DEFAULT NULL,
  `albumId` int NOT NULL,
  `songName` varchar(30) NOT NULL,
  `composerId` int NOT NULL,
  PRIMARY KEY (`albumId`,`songName`,`composerId`),
  KEY `composerId` (`composerId`),
  CONSTRAINT `songcomposer_ibfk_1` FOREIGN KEY (`albumId`, `songName`) REFERENCES `song` (`albumId`, `songName`) ON DELETE CASCADE,
  CONSTRAINT `songcomposer_ibfk_2` FOREIGN KEY (`composerId`) REFERENCES `composer` (`composerId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songcomposer`
--

LOCK TABLES `songcomposer` WRITE;
/*!40000 ALTER TABLE `songcomposer` DISABLE KEYS */;
/*!40000 ALTER TABLE `songcomposer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songlyricist`
--

DROP TABLE IF EXISTS `songlyricist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songlyricist` (
  `id` int DEFAULT NULL,
  `albumId` int NOT NULL,
  `songName` varchar(30) NOT NULL,
  `LyricistId` int NOT NULL,
  PRIMARY KEY (`albumId`,`songName`,`LyricistId`),
  KEY `LyricistId` (`LyricistId`),
  CONSTRAINT `songlyricist_ibfk_1` FOREIGN KEY (`albumId`, `songName`) REFERENCES `song` (`albumId`, `songName`) ON DELETE CASCADE,
  CONSTRAINT `songlyricist_ibfk_2` FOREIGN KEY (`LyricistId`) REFERENCES `lyricist` (`lyricistId`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songlyricist`
--

LOCK TABLES `songlyricist` WRITE;
/*!40000 ALTER TABLE `songlyricist` DISABLE KEYS */;
/*!40000 ALTER TABLE `songlyricist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songreview`
--

DROP TABLE IF EXISTS `songreview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songreview` (
  `id` int DEFAULT NULL,
  `userId` varchar(12) NOT NULL,
  `albumId` int NOT NULL,
  `songName` varchar(30) NOT NULL,
  `star` int DEFAULT '1',
  `content` text,
  PRIMARY KEY (`userId`,`albumId`,`songName`),
  KEY `albumId` (`albumId`,`songName`),
  CONSTRAINT `songreview_ibfk_1` FOREIGN KEY (`albumId`, `songName`) REFERENCES `song` (`albumId`, `songName`) ON DELETE CASCADE,
  CONSTRAINT `songreview_ibfk_2` FOREIGN KEY (`userId`) REFERENCES `user` (`_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songreview`
--

LOCK TABLES `songreview` WRITE;
/*!40000 ALTER TABLE `songreview` DISABLE KEYS */;
/*!40000 ALTER TABLE `songreview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `_id` varchar(12) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-04  1:06:37
