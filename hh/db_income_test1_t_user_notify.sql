-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test1
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
-- Table structure for table `t_user_notify`
--

DROP TABLE IF EXISTS `t_user_notify`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_notify` (
  `msg_count` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `msg_type` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user_notify`
--

LOCK TABLES `t_user_notify` WRITE;
/*!40000 ALTER TABLE `t_user_notify` DISABLE KEYS */;
INSERT INTO `t_user_notify` VALUES (1,0,'2018-04-19 10:20:07',1),(1,93,'2018-04-19 10:20:38',2),(0,94,'2018-04-19 10:20:07',1),(0,95,'2018-04-19 09:10:49',1),(0,96,'2018-04-19 10:20:38',2),(0,97,'2018-04-19 09:10:49',1),(0,99,'2018-04-09 06:02:13',1),(0,100,'2018-04-18 09:44:07',2),(1,101,'2018-04-19 10:20:38',2),(1,102,'2018-04-19 10:20:38',2),(1,103,'2018-04-19 10:20:38',2),(1,104,'2018-04-02 09:49:28',1),(0,106,'2018-04-19 01:14:07',1),(0,107,'2018-04-19 01:46:33',1),(1,108,'2018-04-11 06:16:43',2),(1,109,'2018-04-11 06:16:43',2),(0,117,'2018-04-11 01:14:19',1),(0,118,'2018-04-08 06:15:23',1),(0,119,'2018-04-18 01:41:01',1),(0,121,'2018-04-19 10:20:06',1),(0,122,'2018-04-19 03:45:44',1),(0,123,'2018-04-19 09:55:16',1),(1,124,'2018-04-09 05:54:47',1),(1,125,'2018-04-19 07:18:28',1),(0,126,'2018-04-19 07:44:08',1),(0,127,'2018-04-19 10:20:07',1),(1,128,'2018-04-19 09:39:23',1),(0,129,'2018-04-18 03:52:58',1),(0,130,'2018-04-19 04:51:27',1),(0,131,'2018-04-11 06:23:45',1),(0,132,'2018-04-03 05:59:58',1),(0,135,'2018-04-19 01:15:06',1),(0,136,'2018-04-19 06:52:53',1),(0,137,'2018-04-18 08:46:19',1),(0,138,'2018-04-17 03:40:19',1),(0,139,'2018-04-19 06:54:49',1),(0,140,'2018-04-19 09:13:48',1),(0,141,'2018-04-19 02:22:28',1),(0,142,'2018-04-19 01:15:21',1),(1,143,'2018-04-18 10:01:26',1),(1,144,'2018-04-19 10:04:49',1),(1,145,'2018-04-18 09:44:07',2),(1,146,'2018-04-18 09:44:07',2),(1,147,'2018-04-18 09:44:07',2),(1,148,'2018-04-18 09:44:07',2),(1,149,'2018-04-18 09:44:07',2);
/*!40000 ALTER TABLE `t_user_notify` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:58
