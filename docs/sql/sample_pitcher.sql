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
-- Table structure for table `pitcher`
--

DROP TABLE IF EXISTS `pitcher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `pitcher` (
  `uniform_number` int(11) NOT NULL,
  `player_name` varchar(50) NOT NULL,
  `birthday` date DEFAULT NULL,
  `position` varchar(2) NOT NULL,
  `throwing_hand` char(1) NOT NULL,
  `batting_hand` char(1) NOT NULL,
  PRIMARY KEY (`uniform_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pitcher`
--

LOCK TABLES `pitcher` WRITE;
/*!40000 ALTER TABLE `pitcher` DISABLE KEYS */;
INSERT INTO `pitcher` VALUES
(11,'東　克樹','1995-11-29','投','左','左'),
(12,'竹田　祐','1999-07-05','投','右','右'),
(13,'伊勢　大夢','1998-03-07','投','右','右'),
(14,'石田　健大','1993-03-01','投','左','左'),
(15,'徳山　壮磨','1999-06-06','投','右','右'),
(16,'大貫　晋一','1994-02-03','投','右','右'),
(17,'三嶋　一輝','1990-05-07','投','右','両'),
(18,'小園　健太','2003-04-09','投','右','右'),
(19,'山﨑　康晃','1992-10-02','投','右','右'),
(20,'坂本　裕哉','1997-07-28','投','左','左'),
(22,'入江　大生','1998-08-26','投','右','右'),
(24,'吉野　光樹','1998-07-19','投','右','右'),
(27,'藤浪　晋太郎','1994-04-12','投','右','右'),
(30,'篠木　健太郎','2002-05-07','投','右','左'),
(33,'武田　陸玖','2005-06-06','投','左','左'),
(34,'松本　凌人','2001-12-05','投','右','右'),
(35,'橋本　達弥','2000-07-18','投','右','右'),
(36,'森下　瑠大','2004-09-19','投','左','左'),
(38,'森　唯斗','1992-01-08','投','右','右'),
(39,'若松　尚輝','2000-05-10','投','右','右'),
(40,'松本　隆之介','2002-07-31','投','左','左'),
(41,'佐々木　千隼','1994-06-08','投','右','右'),
(42,'ジャクソン','1996-05-01','投','右','右'),
(43,'深沢　鳳介','2003-11-05','投','右','右'),
(45,'森原　康平','1991-12-26','投','右','左'),
(46,'坂口　翔颯','2002-09-12','投','右','右'),
(48,'京山　将弥','1998-07-04','投','右','右'),
(52,'浜地　真澄','1998-05-25','投','右','右'),
(53,'颯','1998-10-10','投','右','左'),
(54,'石田　裕太郎','2002-01-22','投','右','右'),
(59,'平良　拳太郎','1995-07-12','投','右','右'),
(62,'ウィック','1992-11-09','投','右','左'),
(64,'中川　虎大','1999-10-02','投','右','右'),
(65,'宮城　滝太','2000-07-15','投','右','右'),
(68,'岩田　将貴','1998-06-16','投','左','左'),
(69,'ケイ','1995-03-21','投','左','左'),
(91,'庄司　陽斗','2001-05-31','投','左','左'),
(92,'堀岡　隼人','1998-09-11','投','右','右'),
(93,'ディアス','1999-06-10','投','左','左'),
(96,'バウアー','1991-01-17','投','右','右'),
(98,'マルセリーノ','2002-06-16','投','右','右'),
(101,'草野　陽斗','2004-06-07','投','右','右'),
(102,'清水　麻成','2005-10-06','投','右','右'),
(103,'金渕　光希','2006-10-01','投','左','左'),
(108,'今野　瑠斗','2004-07-13','投','右','右'),
(111,'吉岡　暖','2006-08-28','投','右','右'),
(199,'笠谷　俊介','1997-03-17','投','左','左');
/*!40000 ALTER TABLE `pitcher` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-01 15:47:42
