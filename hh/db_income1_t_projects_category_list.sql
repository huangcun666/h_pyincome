-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income1
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
-- Table structure for table `t_projects_category_list`
--

DROP TABLE IF EXISTS `t_projects_category_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_category_list` (
  `project_id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `order_int` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_category_list`
--

LOCK TABLES `t_projects_category_list` WRITE;
/*!40000 ALTER TABLE `t_projects_category_list` DISABLE KEYS */;
INSERT INTO `t_projects_category_list` VALUES (180,154,9,'类型9',0,'2018-05-07 08:25:41'),(181,154,2,'类型2',0,'2018-05-07 09:52:09'),(182,97,12,'类型12',0,'2018-05-07 09:53:05'),(183,154,2,'类型2',0,'2018-05-08 01:35:40'),(184,97,13,'类型13',0,'2018-05-08 01:37:15'),(185,97,14,'最长的客户分组',0,'2018-05-08 01:43:58'),(186,97,5,'类型5',0,'2018-05-08 01:47:43'),(187,154,3,'类型3',0,'2018-05-08 01:50:59'),(201,154,1,'类型1',0,'2018-05-08 01:56:31'),(202,154,4,'类型4',0,'2018-05-08 02:16:19'),(205,154,7,'类型7',0,'2018-05-08 03:03:46'),(208,97,7,'类型7',0,'2018-05-08 06:58:15'),(209,97,8,'类型8',0,'2018-05-08 06:58:20'),(211,154,10,'类型10',0,'2018-05-09 08:41:19'),(212,154,10,'类型10',0,'2018-05-09 16:48:02'),(217,154,4,'类型4',0,'2018-05-09 02:16:19'),(405,106,9,'类型9',0,'2018-05-17 11:49:08'),(408,97,6,'类型6',0,'2018-05-11 16:24:55'),(409,97,13,'类型13',0,'2018-05-11 15:23:38'),(411,97,28,'分组6',0,'2018-05-11 15:04:47'),(412,97,24,'分组2',0,'2018-05-10 15:03:13'),(413,97,28,'分组6',0,'2018-05-10 14:57:28'),(414,106,11,'类型11',0,'2018-05-17 11:36:15'),(415,97,23,'办理中',0,'2018-05-10 14:24:30');
/*!40000 ALTER TABLE `t_projects_category_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:34
