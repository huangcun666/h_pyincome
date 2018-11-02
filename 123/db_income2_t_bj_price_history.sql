-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income2
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `t_bj_price_history`
--

DROP TABLE IF EXISTS `t_bj_price_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_bj_price_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `bj_mange_id` int(11) DEFAULT NULL,
  `bj_uid` int(11) DEFAULT NULL,
  `bj_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_bj_price_history`
--

LOCK TABLES `t_bj_price_history` WRITE;
/*!40000 ALTER TABLE `t_bj_price_history` DISABLE KEYS */;
INSERT INTO `t_bj_price_history` VALUES (19,3000,'2018-07-17 02:40:55',39,118,'冯恒敏'),(20,5500,'2018-07-17 07:06:42',40,118,'冯恒敏'),(21,5500,'2018-07-18 01:27:44',41,118,'冯恒敏'),(22,12000,'2018-07-18 01:29:07',42,118,'冯恒敏'),(23,12000,'2018-07-18 01:30:03',43,118,'冯恒敏'),(24,18000,'2018-07-18 01:30:56',44,118,'冯恒敏'),(25,12000,'2018-07-18 01:32:22',45,118,'冯恒敏'),(26,17000,'2018-07-18 01:33:14',46,118,'冯恒敏'),(27,3500,'2018-07-18 01:35:06',47,118,'冯恒敏'),(28,5500,'2018-07-18 01:37:17',48,118,'冯恒敏'),(29,12000,'2018-07-18 01:37:57',49,118,'冯恒敏'),(30,4500,'2018-07-18 01:38:57',50,118,'冯恒敏'),(31,9000,'2018-07-18 01:39:57',51,118,'冯恒敏'),(32,12000,'2018-07-18 01:40:46',52,118,'冯恒敏'),(33,14000,'2018-07-18 01:41:24',53,118,'冯恒敏'),(34,3500,'2018-07-18 01:53:16',47,118,'冯恒敏'),(35,7000,'2018-07-18 02:36:50',41,118,'冯恒敏'),(36,2500,'2018-07-27 07:47:54',39,118,'冯恒敏'),(37,3500,'2018-07-27 07:48:08',50,118,'冯恒敏'),(38,9000,'2018-07-27 08:00:00',51,118,'冯恒敏'),(39,9000,'2018-08-06 01:44:54',51,118,'冯恒敏'),(40,3500,'2018-08-06 01:46:11',50,118,'冯恒敏'),(41,3500,'2018-08-09 01:56:13',47,118,'冯恒敏'),(42,2500,'2018-08-11 07:27:46',39,118,'冯恒敏');
/*!40000 ALTER TABLE `t_bj_price_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:13
