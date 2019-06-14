-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test3
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
-- Table structure for table `t_trade`
--

DROP TABLE IF EXISTS `t_trade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_trade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `trade_name` varchar(555) DEFAULT NULL,
  `trade_number` varchar(255) DEFAULT NULL,
  `trade_reg_at` datetime DEFAULT NULL,
  `trade_by` varchar(255) DEFAULT NULL,
  `trade_regtype` varchar(255) DEFAULT NULL,
  `trade_color` varchar(255) DEFAULT NULL,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `curr_mile_id` int(11) NOT NULL DEFAULT '0',
  `curr_mile_id_name` varchar(255) DEFAULT NULL,
  `curr_mile_uid` int(11) NOT NULL DEFAULT '0',
  `curr_mile_uid_name` varchar(255) DEFAULT NULL,
  `created_uid` int(11) NOT NULL DEFAULT '0',
  `created_uid_name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `is_close` tinyint(1) NOT NULL DEFAULT '0',
  `trade_remark` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_trade`
--

LOCK TABLES `t_trade` WRITE;
/*!40000 ALTER TABLE `t_trade` DISABLE KEYS */;
INSERT INTO `t_trade` VALUES (2,'大大大','',NULL,'','','',1233,0,NULL,0,NULL,0,NULL,NULL,0,''),(3,'大大大','',NULL,'反倒是发达的散发士大夫士大夫','','',1233,0,NULL,0,NULL,0,NULL,NULL,0,''),(4,'大大大','',NULL,'反倒是发达的散发士大夫士大夫','','',1233,0,NULL,0,NULL,0,NULL,NULL,0,''),(5,'大大大','dsfsd',NULL,'fsdsfdfd','dfsfsd','fds',2133,0,NULL,0,NULL,116,'陈太智','2019-06-05 18:07:00',0,''),(6,'fdsf','fdsfsd',NULL,'fsdf','sdfsdffsd','fds',3432,0,NULL,0,NULL,116,'陈太智','2019-06-05 18:08:13',0,'sdf'),(7,'fdsf','fdsfsd',NULL,'fsdf','sdfsdffsd','fds',3432,0,NULL,0,NULL,116,'陈太智','2019-06-05 18:09:23',0,'sdf'),(8,'ff','ff',NULL,'ff','f','ff',120,0,NULL,0,NULL,116,'陈太智','2019-06-11 15:30:36',0,''),(9,'ff','f',NULL,'fffffffff','f','ff',234,0,NULL,0,NULL,116,'陈太智','2019-06-11 15:31:26',0,''),(10,'ddd','',NULL,'ddd','dd','ddd',3242,0,NULL,0,NULL,116,'陈太智','2019-06-11 16:02:43',0,''),(11,'发发发','',NULL,'冉冉','冉冉','冉冉',234,0,NULL,0,NULL,116,'陈太智','2019-06-11 16:40:41',0,''),(12,'大大大','',NULL,'等待','dsfsd','dfsf',1123,0,NULL,0,NULL,116,'陈太智','2019-06-11 16:48:08',0,''),(13,'dd','ddd',NULL,'dssds','ds','sd',343,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:02:39',0,''),(14,'dd','dd',NULL,'dd','dd','d',324,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:08:18',0,''),(15,'ddd','1221',NULL,'2121','2121','212',21221,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:33:06',0,''),(16,'sadsad','sadasd',NULL,'sadsad','sadasd','sada',3243,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:42:27',0,''),(17,'fdsf','sdsfdfs',NULL,'fds','dsffds','dfs',3432,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:43:54',0,''),(18,'ddd','dd',NULL,'dd','ddd','dd',323,0,NULL,0,NULL,116,'陈太智','2019-06-11 17:49:58',0,''),(19,'33','333',NULL,'33','33','333',2121,0,NULL,0,NULL,116,'陈太智','2019-06-12 10:31:17',0,''),(20,'dddd','dddddd',NULL,'dd','ddd','ddd',2314,0,NULL,0,NULL,116,'陈太智','2019-06-12 13:51:14',0,''),(21,'dsf','dsfsd',NULL,'sdfsdf','sfsd','sfdsdf',324,0,NULL,0,NULL,116,'陈太智','2019-06-12 13:51:40',0,''),(22,'fds','fdsf',NULL,'fsds','sdf','fdsfsd',324,0,NULL,0,NULL,116,'陈太智','2019-06-12 13:54:16',0,''),(23,'fd','dfdf',NULL,'dfdf','dfdf','dfdf',342,0,NULL,0,NULL,116,'陈太智','2019-06-12 13:59:39',0,''),(24,'发业','',NULL,'','','',112,0,NULL,0,NULL,116,'陈太智','2019-06-12 14:21:26',0,''),(25,'1654','',NULL,'','','',654,0,NULL,0,NULL,116,'陈太智','2019-06-12 14:23:50',0,''),(26,'sadasd','asd',NULL,'sadsad','','sadsad',34223,0,NULL,0,NULL,116,'陈太智','2019-06-12 15:37:03',0,''),(27,'ddd','ddd',NULL,'dddd','','',21321,0,NULL,0,NULL,116,'陈太智','2019-06-13 10:36:00',0,''),(28,'ddd','dd',NULL,'ddd','dd','',3242,0,NULL,0,NULL,116,'陈太智','2019-06-13 11:16:14',0,''),(29,'fds','sdg',NULL,'','','',4534,0,NULL,0,NULL,116,'陈太智','2019-06-13 11:16:40',0,''),(30,'dsad','asdsda',NULL,'','','',342,0,NULL,0,NULL,116,'陈太智','2019-06-13 14:36:32',0,''),(31,'dsdffsd','',NULL,'','','',3324,0,NULL,0,NULL,116,'陈太智','2019-06-13 14:39:10',0,''),(32,'gfdgdf','',NULL,'','','',4534,0,NULL,0,NULL,116,'陈太智','2019-06-13 18:51:47',0,''),(33,'ww','',NULL,'','','',2134,0,NULL,0,NULL,116,'陈太智','2019-06-13 18:55:28',0,'');
/*!40000 ALTER TABLE `t_trade` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:06:47
