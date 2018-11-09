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
-- Table structure for table `t_projects_events`
--

DROP TABLE IF EXISTS `t_projects_events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_events` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `event_type` varchar(255) NOT NULL,
  `txt` varchar(2550) NOT NULL DEFAULT '',
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_events`
--

LOCK TABLES `t_projects_events` WRITE;
/*!40000 ALTER TABLE `t_projects_events` DISABLE KEYS */;
INSERT INTO `t_projects_events` VALUES (1,2124,'流转取消','陈勇极请求取消订单','2018-08-09 09:33:47',139,'陈勇极'),(2,2124,'流转取消','罗文波同意取消订单','2018-08-09 09:36:13',119,'罗文波'),(3,2124,'流转取消','罗文波恢复订单','2018-08-09 09:36:29',119,'罗文波'),(4,2124,'流转取消','陈勇极请求取消订单','2018-08-10 01:27:27',139,'陈勇极'),(5,2124,'流转取消','罗文波同意取消订单','2018-08-10 01:29:45',119,'罗文波'),(6,1973,'流转取消','王坚请求取消订单','2018-08-14 01:09:49',138,'王坚'),(7,1973,'流转取消','罗文波同意取消订单','2018-08-14 01:13:39',119,'罗文波'),(8,1952,'流转取消','钟东梅请求取消订单','2018-08-14 02:04:22',136,'钟东梅'),(9,1952,'流转取消','罗文波同意取消订单','2018-08-14 03:36:34',119,'罗文波'),(10,564,'流转取消','陈莹莹请求取消订单','2018-08-14 09:09:38',338,'陈莹莹'),(11,564,'流转取消','罗文波同意取消订单','2018-08-14 09:14:27',119,'罗文波'),(12,1758,'流转取消','李佳欣请求取消订单','2018-08-16 02:21:37',268,'李佳欣'),(13,1758,'流转取消','罗文波同意取消订单','2018-08-16 03:17:12',119,'罗文波'),(14,1593,'流转取消','钟明霞请求取消订单','2018-08-16 06:41:00',137,'钟明霞'),(15,1643,'流转取消','李杰请求取消订单','2018-08-16 06:56:57',239,'李杰'),(16,636,'流转取消','刘建光请求取消订单','2018-08-16 06:59:32',141,'刘建光'),(17,1582,'流转取消','刘建光请求取消订单','2018-08-16 07:00:07',141,'刘建光'),(18,1643,'流转取消','罗文波同意取消订单','2018-08-16 07:51:18',119,'罗文波'),(19,1593,'流转取消','罗文波同意取消订单','2018-08-16 07:53:02',119,'罗文波'),(20,636,'流转取消','罗文波同意取消订单','2018-08-16 08:45:06',119,'罗文波'),(21,1593,'流转取消','刘建光请求取消订单','2018-08-17 00:57:12',141,'刘建光'),(22,1582,'流转取消','罗文波同意取消订单','2018-08-17 06:43:49',119,'罗文波'),(23,1593,'流转取消','罗文波同意取消订单','2018-08-17 06:44:44',119,'罗文波'),(24,973,'流转取消','刘建光请求取消订单','2018-08-20 01:56:38',141,'刘建光'),(25,973,'流转取消','罗文波同意取消订单','2018-08-20 02:18:38',119,'罗文波'),(26,1543,'流转取消','莫诗域请求取消订单','2018-08-22 01:10:29',140,'莫诗域'),(27,2080,'流转取消','陈勇极请求取消订单','2018-08-22 03:28:42',139,'陈勇极'),(28,1980,'流转取消','王坚请求取消订单','2018-08-23 01:33:38',138,'王坚'),(29,1991,'流转取消','王坚请求取消订单','2018-08-23 02:40:38',138,'王坚'),(30,1148,'流转取消','钟明霞请求取消订单','2018-08-23 04:10:26',137,'钟明霞'),(31,1148,'流转取消','罗文波同意取消订单','2018-08-23 04:25:48',119,'罗文波'),(32,2080,'流转取消','罗文波同意取消订单','2018-08-23 05:44:05',119,'罗文波'),(33,1991,'流转取消','罗文波同意取消订单','2018-08-23 05:44:46',119,'罗文波'),(34,1980,'流转取消','罗文波同意取消订单','2018-08-23 05:45:24',119,'罗文波'),(35,1543,'流转取消','罗文波同意取消订单','2018-08-23 05:46:04',119,'罗文波'),(36,491,'流转取消','梁倩请求取消订单','2018-08-23 06:24:17',296,'梁倩'),(37,1153,'流转取消','梁倩请求取消订单','2018-08-23 06:27:35',296,'梁倩'),(38,1510,'流转取消','梁倩请求取消订单','2018-08-23 08:13:22',296,'梁倩'),(39,1510,'流转取消','罗文波同意取消订单','2018-08-23 08:34:07',119,'罗文波'),(40,1153,'流转取消','罗文波同意取消订单','2018-08-23 08:34:51',119,'罗文波'),(41,491,'流转取消','罗文波同意取消订单','2018-08-23 08:37:06',119,'罗文波'),(42,1643,'流转取消','陈月娇请求取消订单','2018-08-24 02:33:55',210,'陈月娇'),(43,600,'流转取消','钟明霞请求取消订单','2018-08-24 07:42:48',137,'钟明霞'),(44,1643,'流转取消','罗文波同意取消订单','2018-08-24 08:11:09',119,'罗文波'),(45,777,'流转取消','梁倩请求取消订单','2018-08-24 08:12:48',296,'梁倩'),(46,777,'流转取消','罗文波同意取消订单','2018-08-24 08:13:27',119,'罗文波'),(47,600,'流转取消','罗文波同意取消订单','2018-08-24 08:20:06',119,'罗文波'),(48,1818,'流转取消','陈勇极请求取消订单','2018-08-27 01:40:53',139,'陈勇极'),(49,519,'流转取消','刘建光请求取消订单','2018-08-27 01:52:43',141,'刘建光'),(50,519,'流转取消','罗文波同意取消订单','2018-08-27 01:57:19',119,'罗文波'),(51,1818,'流转取消','罗文波同意取消订单','2018-08-27 01:58:00',119,'罗文波'),(52,1982,'流转取消','王坚请求取消订单','2018-08-27 02:09:12',138,'王坚'),(53,1982,'流转取消','罗文波同意取消订单','2018-08-27 02:12:08',119,'罗文波'),(54,1606,'流转取消','莫诗域请求取消订单','2018-08-27 07:25:44',140,'莫诗域'),(55,1606,'流转取消','罗文波同意取消订单','2018-08-28 01:03:38',119,'罗文波'),(56,1606,'流转取消','梁倩请求取消订单','2018-08-28 01:21:59',296,'梁倩'),(57,1606,'流转取消','罗文波同意取消订单','2018-08-28 01:23:03',119,'罗文波'),(58,325,'流转取消','莫诗域请求取消订单','2018-08-28 01:52:14',140,'莫诗域'),(59,1848,'流转取消','刘建光请求取消订单','2018-11-05 10:19:10',141,'刘建光'),(60,1848,'流转取消','刘建光请求取消订单','2018-11-06 01:01:53',141,'刘建光'),(61,1848,'流转取消','刘建光请求取消订单','2018-11-06 01:01:58',141,'刘建光'),(62,1848,'流转取消','刘建光请求取消订单','2018-11-06 01:02:55',141,'刘建光');
/*!40000 ALTER TABLE `t_projects_events` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:55
