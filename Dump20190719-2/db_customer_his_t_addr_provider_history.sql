-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_his
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
-- Table structure for table `t_addr_provider_history`
--

DROP TABLE IF EXISTS `t_addr_provider_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_provider_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `price` float DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `addr_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_provider_history`
--

LOCK TABLES `t_addr_provider_history` WRITE;
/*!40000 ALTER TABLE `t_addr_provider_history` DISABLE KEYS */;
INSERT INTO `t_addr_provider_history` VALUES (4,2000,'2018-08-07 08:12:56',17,118,'冯恒敏'),(5,3500,'2018-08-07 08:23:50',18,118,'冯恒敏'),(6,3500,'2018-08-07 08:28:14',18,118,'冯恒敏'),(7,3500,'2018-08-07 08:32:16',18,118,'冯恒敏'),(8,3500,'2018-08-24 01:37:15',18,118,'冯恒敏'),(9,1000,'2018-08-24 01:38:10',19,118,'冯恒敏'),(10,4000,'2018-09-11 06:54:17',20,118,'冯恒敏'),(11,7000,'2018-09-11 06:56:46',21,118,'冯恒敏'),(12,4000,'2018-09-11 06:57:09',20,118,'冯恒敏'),(13,6000,'2018-09-11 06:58:46',22,118,'冯恒敏'),(14,3500,'2018-09-11 07:06:44',23,118,'冯恒敏');
/*!40000 ALTER TABLE `t_addr_provider_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:39
