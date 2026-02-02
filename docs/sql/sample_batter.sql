/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.14-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: django_baseball_playerdb
-- ------------------------------------------------------
-- Server version	10.11.14-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `batter`
--

DROP TABLE IF EXISTS `batter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `batter` (
  `uniform_number` int(11) NOT NULL,
  `player_name` varchar(50) NOT NULL,
  `birthday` date DEFAULT NULL,
  `position` varchar(2) NOT NULL,
  `batting_hand` char(1) NOT NULL,
  `throwing_hand` char(1) NOT NULL,
  PRIMARY KEY (`uniform_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `batter`
--

LOCK TABLES `batter` WRITE;
/*!40000 ALTER TABLE `batter` DISABLE KEYS */;
INSERT INTO `batter` VALUES
(0,'林　琢真','2000-08-24','内','左','右'),
(1,'桑原　将志','1993-07-21','外','右','右'),
(2,'牧　秀悟','1998-04-21','内','右','右'),
(3,'オースティン','1991-09-06','内','右','右'),
(4,'度会　隆輝','2002-10-04','外','左','右'),
(5,'松尾　汐恩','2004-07-06','捕','右','右'),
(6,'森　敬斗','2002-01-28','内','左','右'),
(7,'佐野　恵太','1994-11-28','外','左','右'),
(8,'神里　和毅','1994-01-17','外','左','右'),
(9,'京田　陽太','1994-04-20','内','左','右'),
(10,'戸柱　恭孝','1990-04-11','捕','左','右'),
(25,'筒香　嘉智','1991-11-26','外','左','右'),
(26,'三森　大貴','1999-02-21','内','左','右'),
(28,'勝又　温史','2000-05-22','外','左','右'),
(29,'伊藤　光','1989-04-23','捕','右','右'),
(31,'柴田　竜拓','1993-12-16','内','左','右'),
(32,'益子　京右','2000-12-27','捕','右','右'),
(37,'加藤　響','2002-06-15','内','右','右'),
(44,'石上　泰輝','2001-05-18','内','左','右'),
(50,'山本　祐大','1998-09-11','捕','右','右'),
(51,'宮﨑　敏郎','1988-12-12','内','右','右'),
(55,'井上　絢登','2000-02-23','内','左','右'),
(56,'田内　真翔','2007-03-06','内','右','右'),
(57,'東妻　純平','2001-07-03','捕','右','右'),
(58,'梶原　昂希','1999-09-19','外','左','右'),
(60,'知野　直人','1999-02-16','内','右','右'),
(61,'蝦名　達夫','1997-09-20','外','右','右'),
(63,'関根　大気','1995-06-28','外','左','左'),
(66,'ビシエド','1989-03-10','内','右','右'),
(95,'九鬼　隆平','1998-09-05','捕','右','右'),
(99,'フォード','1992-07-04','内','左','右'),
(100,'蓮','2004-07-18','内','右','右'),
(125,'小笠原　蒼','2005-10-20','内','左','右'),
(127,'上甲　凌大','2001-01-29','捕','左','右'),
(129,'西巻　賢二','1999-04-22','内','右','右'),
(130,'近藤　大雅','2005-09-18','捕','右','右'),
(133,'粟飯原　龍之介','2004-02-22','内','左','右'),
(155,'小針　大輝','2006-10-10','外','左','左'),
(193,'高見澤　郁魅','2006-01-18','内','左','右');
/*!40000 ALTER TABLE `batter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 15:40:53
