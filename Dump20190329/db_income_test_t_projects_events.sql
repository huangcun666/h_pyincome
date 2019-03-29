-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test
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
  `project_id` int(11) NOT NULL DEFAULT '0',
  `event_type` varchar(255) NOT NULL,
  `txt` varchar(2550) NOT NULL DEFAULT '',
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(100) DEFAULT NULL,
  `ext_id` int(11) NOT NULL DEFAULT '0',
  `customer_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=475 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_events`
--

LOCK TABLES `t_projects_events` WRITE;
/*!40000 ALTER TABLE `t_projects_events` DISABLE KEYS */;
INSERT INTO `t_projects_events` VALUES (1,2124,'流转取消','陈勇极请求取消订单','2018-08-09 09:33:47',139,'陈勇极',0,0),(2,2124,'流转取消','罗文波同意取消订单','2018-08-09 09:36:13',119,'罗文波',0,0),(3,2124,'流转取消','罗文波恢复订单','2018-08-09 09:36:29',119,'罗文波',0,0),(4,2124,'流转取消','陈勇极请求取消订单','2018-08-10 01:27:27',139,'陈勇极',0,0),(5,2124,'流转取消','罗文波同意取消订单','2018-08-10 01:29:45',119,'罗文波',0,0),(6,1973,'流转取消','王坚请求取消订单','2018-08-14 01:09:49',138,'王坚',0,0),(7,1973,'流转取消','罗文波同意取消订单','2018-08-14 01:13:39',119,'罗文波',0,0),(8,1952,'流转取消','钟东梅请求取消订单','2018-08-14 02:04:22',136,'钟东梅',0,0),(9,1952,'流转取消','罗文波同意取消订单','2018-08-14 03:36:34',119,'罗文波',0,0),(10,564,'流转取消','陈莹莹请求取消订单','2018-08-14 09:09:38',338,'陈莹莹',0,0),(11,564,'流转取消','罗文波同意取消订单','2018-08-14 09:14:27',119,'罗文波',0,0),(12,1758,'流转取消','李佳欣请求取消订单','2018-08-16 02:21:37',268,'李佳欣',0,0),(13,1758,'流转取消','罗文波同意取消订单','2018-08-16 03:17:12',119,'罗文波',0,0),(14,1593,'流转取消','钟明霞请求取消订单','2018-08-16 06:41:00',137,'钟明霞',0,0),(15,1643,'流转取消','李杰请求取消订单','2018-08-16 06:56:57',239,'李杰',0,0),(16,636,'流转取消','刘建光请求取消订单','2018-08-16 06:59:32',141,'刘建光',0,0),(17,1582,'流转取消','刘建光请求取消订单','2018-08-16 07:00:07',141,'刘建光',0,0),(18,1643,'流转取消','罗文波同意取消订单','2018-08-16 07:51:18',119,'罗文波',0,0),(19,1593,'流转取消','罗文波同意取消订单','2018-08-16 07:53:02',119,'罗文波',0,0),(20,636,'流转取消','罗文波同意取消订单','2018-08-16 08:45:06',119,'罗文波',0,0),(21,1593,'流转取消','刘建光请求取消订单','2018-08-17 00:57:12',141,'刘建光',0,0),(22,1582,'流转取消','罗文波同意取消订单','2018-08-17 06:43:49',119,'罗文波',0,0),(23,1593,'流转取消','罗文波同意取消订单','2018-08-17 06:44:44',119,'罗文波',0,0),(24,973,'流转取消','刘建光请求取消订单','2018-08-20 01:56:38',141,'刘建光',0,0),(25,973,'流转取消','罗文波同意取消订单','2018-08-20 02:18:38',119,'罗文波',0,0),(26,1543,'流转取消','莫诗域请求取消订单','2018-08-22 01:10:29',140,'莫诗域',0,0),(27,2080,'流转取消','陈勇极请求取消订单','2018-08-22 03:28:42',139,'陈勇极',0,0),(28,1980,'流转取消','王坚请求取消订单','2018-08-23 01:33:38',138,'王坚',0,0),(29,1991,'流转取消','王坚请求取消订单','2018-08-23 02:40:38',138,'王坚',0,0),(30,1148,'流转取消','钟明霞请求取消订单','2018-08-23 04:10:26',137,'钟明霞',0,0),(31,1148,'流转取消','罗文波同意取消订单','2018-08-23 04:25:48',119,'罗文波',0,0),(32,2080,'流转取消','罗文波同意取消订单','2018-08-23 05:44:05',119,'罗文波',0,0),(33,1991,'流转取消','罗文波同意取消订单','2018-08-23 05:44:46',119,'罗文波',0,0),(34,1980,'流转取消','罗文波同意取消订单','2018-08-23 05:45:24',119,'罗文波',0,0),(35,1543,'流转取消','罗文波同意取消订单','2018-08-23 05:46:04',119,'罗文波',0,0),(36,491,'流转取消','梁倩请求取消订单','2018-08-23 06:24:17',296,'梁倩',0,0),(37,1153,'流转取消','梁倩请求取消订单','2018-08-23 06:27:35',296,'梁倩',0,0),(38,1510,'流转取消','梁倩请求取消订单','2018-08-23 08:13:22',296,'梁倩',0,0),(39,1510,'流转取消','罗文波同意取消订单','2018-08-23 08:34:07',119,'罗文波',0,0),(40,1153,'流转取消','罗文波同意取消订单','2018-08-23 08:34:51',119,'罗文波',0,0),(41,491,'流转取消','罗文波同意取消订单','2018-08-23 08:37:06',119,'罗文波',0,0),(42,1643,'流转取消','陈月娇请求取消订单','2018-08-24 02:33:55',210,'陈月娇',0,0),(43,600,'流转取消','钟明霞请求取消订单','2018-08-24 07:42:48',137,'钟明霞',0,0),(44,1643,'流转取消','罗文波同意取消订单','2018-08-24 08:11:09',119,'罗文波',0,0),(45,777,'流转取消','梁倩请求取消订单','2018-08-24 08:12:48',296,'梁倩',0,0),(46,777,'流转取消','罗文波同意取消订单','2018-08-24 08:13:27',119,'罗文波',0,0),(47,600,'流转取消','罗文波同意取消订单','2018-08-24 08:20:06',119,'罗文波',0,0),(48,1818,'流转取消','陈勇极请求取消订单','2018-08-27 01:40:53',139,'陈勇极',0,0),(49,519,'流转取消','刘建光请求取消订单','2018-08-27 01:52:43',141,'刘建光',0,0),(50,519,'流转取消','罗文波同意取消订单','2018-08-27 01:57:19',119,'罗文波',0,0),(51,1818,'流转取消','罗文波同意取消订单','2018-08-27 01:58:00',119,'罗文波',0,0),(52,1982,'流转取消','王坚请求取消订单','2018-08-27 02:09:12',138,'王坚',0,0),(53,1982,'流转取消','罗文波同意取消订单','2018-08-27 02:12:08',119,'罗文波',0,0),(54,1606,'流转取消','莫诗域请求取消订单','2018-08-27 07:25:44',140,'莫诗域',0,0),(55,1606,'流转取消','罗文波同意取消订单','2018-08-28 01:03:38',119,'罗文波',0,0),(56,1606,'流转取消','梁倩请求取消订单','2018-08-28 01:21:59',296,'梁倩',0,0),(57,1606,'流转取消','罗文波同意取消订单','2018-08-28 01:23:03',119,'罗文波',0,0),(58,325,'流转取消','莫诗域请求取消订单','2018-08-28 01:52:14',140,'莫诗域',0,0),(59,325,'流转取消','罗文波同意取消订单','2018-08-28 02:29:18',119,'罗文波',0,0),(60,1545,'流转取消','王坚请求取消订单','2018-08-28 06:29:29',138,'王坚',0,0),(61,1545,'流转取消','罗文波同意取消订单','2018-08-28 06:33:22',119,'罗文波',0,0),(62,771,'流转取消','陈勇极请求取消订单','2018-08-29 01:44:14',139,'陈勇极',0,0),(63,819,'流转取消','陈勇极请求取消订单','2018-08-29 02:20:53',139,'陈勇极',0,0),(64,771,'流转取消','罗文波同意取消订单','2018-08-29 03:19:16',119,'罗文波',0,0),(65,819,'流转取消','罗文波同意取消订单','2018-08-29 03:20:17',119,'罗文波',0,0),(66,1898,'流转取消','陈勇极请求取消订单','2018-08-29 07:07:29',139,'陈勇极',0,0),(67,1898,'流转取消','罗文波同意取消订单','2018-08-29 08:11:17',119,'罗文波',0,0),(68,2042,'流转取消','莫诗域请求取消订单','2018-08-30 07:58:37',140,'莫诗域',0,0),(69,2042,'流转取消','罗文波同意取消订单','2018-08-30 08:11:03',119,'罗文波',0,0),(70,2042,'流转取消','陈月娇请求取消订单','2018-08-30 08:20:42',210,'陈月娇',0,0),(71,2042,'流转取消','罗文波同意取消订单','2018-08-30 08:30:56',119,'罗文波',0,0),(72,1799,'流转取消','陶君怡请求取消订单','2018-08-31 03:23:11',269,'陶君怡',0,0),(73,1781,'流转取消','陶君怡请求取消订单','2018-08-31 03:59:56',269,'陶君怡',0,0),(74,1799,'流转取消','罗文波同意取消订单','2018-08-31 06:02:18',119,'罗文波',0,0),(75,1781,'流转取消','罗文波同意取消订单','2018-08-31 06:03:04',119,'罗文波',0,0),(76,779,'流转取消','钟明霞请求取消订单','2018-08-31 07:46:59',137,'钟明霞',0,0),(77,779,'流转取消','罗文波同意取消订单','2018-08-31 08:30:16',119,'罗文波',0,0),(78,2307,'流转取消','李佳欣请求取消订单','2018-08-31 08:42:11',268,'李佳欣',0,0),(79,1999,'流转取消','王坚请求取消订单','2018-08-31 08:48:33',138,'王坚',0,0),(80,2307,'流转取消','罗文波同意取消订单','2018-08-31 08:49:07',119,'罗文波',0,0),(81,1999,'流转取消','罗文波同意取消订单','2018-08-31 08:49:28',119,'罗文波',0,0),(82,1999,'流转取消','陈月娇请求取消订单','2018-08-31 08:53:23',210,'陈月娇',0,0),(83,1999,'流转取消','罗文波同意取消订单','2018-08-31 08:55:55',119,'罗文波',0,0),(84,1723,'流转取消','陈勇极请求取消订单','2018-09-03 05:39:54',139,'陈勇极',0,0),(85,1723,'流转取消','罗文波同意取消订单','2018-09-03 06:05:20',119,'罗文波',0,0),(86,1545,'流转取消','陈月娇请求取消订单','2018-09-04 04:04:37',210,'陈月娇',0,0),(87,1545,'流转取消','罗文波同意取消订单','2018-09-04 04:04:48',119,'罗文波',0,0),(88,2124,'流转取消','陈月娇请求取消订单','2018-09-04 05:54:29',210,'陈月娇',0,0),(89,2124,'流转取消','罗文波同意取消订单','2018-09-04 05:55:16',119,'罗文波',0,0),(90,2090,'流转取消','陶君怡请求取消订单','2018-09-05 09:05:10',269,'陶君怡',0,0),(91,2090,'流转取消','罗文波同意取消订单','2018-09-06 01:00:42',119,'罗文波',0,0),(92,2631,'流转取消','梁倩请求取消订单','2018-09-11 02:47:52',296,'梁倩',0,0),(93,2631,'流转取消','罗文波同意取消订单','2018-09-11 08:44:41',119,'罗文波',0,0),(94,2584,'流转取消','梁倩请求取消订单','2018-09-13 06:36:31',296,'梁倩',0,0),(95,2584,'流转取消','罗文波同意取消订单','2018-09-13 06:57:34',119,'罗文波',0,0),(96,1959,'流转取消','钟明霞请求取消订单','2018-09-13 07:10:21',137,'钟明霞',0,0),(97,1959,'流转取消','罗文波同意取消订单','2018-09-13 07:11:30',119,'罗文波',0,0),(98,325,'流转取消','罗文波恢复订单','2018-09-13 08:27:16',119,'罗文波',0,0),(99,592,'流转取消','陈月娇请求取消订单','2018-09-13 08:34:10',210,'陈月娇',0,0),(100,592,'流转取消','罗文波同意取消订单','2018-09-13 08:34:32',119,'罗文波',0,0),(101,2221,'流转取消','陶君怡请求取消订单','2018-09-14 02:43:31',269,'陶君怡',0,0),(102,1010,'流转取消','莫诗域请求取消订单','2018-09-14 07:42:12',140,'莫诗域',0,0),(103,2221,'流转取消','罗文波同意取消订单','2018-09-17 02:25:51',119,'罗文波',0,0),(104,1010,'流转取消','罗文波同意取消订单','2018-09-17 02:26:43',119,'罗文波',0,0),(105,2718,'流转取消','陈勇极请求取消订单','2018-09-17 03:46:14',139,'陈勇极',0,0),(106,2718,'流转取消','罗文波同意取消订单','2018-09-18 00:39:24',119,'罗文波',0,0),(107,2385,'流转取消','王坚请求取消订单','2018-09-18 08:34:58',138,'王坚',0,0),(108,2299,'流转取消','刘建光请求取消订单','2018-09-19 00:27:32',141,'刘建光',0,0),(109,2385,'流转取消','罗文波同意取消订单','2018-09-19 03:03:07',119,'罗文波',0,0),(110,2299,'流转取消','罗文波同意取消订单','2018-09-19 03:08:59',119,'罗文波',0,0),(111,1587,'流转取消','莫诗域请求取消订单','2018-09-19 09:28:04',140,'莫诗域',0,0),(112,1587,'流转取消','罗文波同意取消订单','2018-09-19 09:45:58',119,'罗文波',0,0),(113,1950,'流转取消','梁倩请求取消订单','2018-09-21 01:06:14',296,'梁倩',0,0),(114,536,'流转取消','莫诗域请求取消订单','2018-09-21 01:08:10',140,'莫诗域',0,0),(115,1412,'流转取消','梁倩请求取消订单','2018-09-21 01:59:05',296,'梁倩',0,0),(116,686,'流转取消','陈勇极请求取消订单','2018-09-21 06:17:56',139,'陈勇极',0,0),(117,1414,'流转取消','陈勇极请求取消订单','2018-09-21 06:19:05',139,'陈勇极',0,0),(118,1114,'流转取消','陈勇极请求取消订单','2018-09-21 06:19:56',139,'陈勇极',0,0),(119,1950,'流转取消','罗文波同意取消订单','2018-09-22 03:30:28',119,'罗文波',0,0),(120,1414,'流转取消','罗文波同意取消订单','2018-09-22 03:31:09',119,'罗文波',0,0),(121,1412,'流转取消','罗文波同意取消订单','2018-09-22 03:31:33',119,'罗文波',0,0),(122,1114,'流转取消','罗文波同意取消订单','2018-09-22 03:31:51',119,'罗文波',0,0),(123,686,'流转取消','罗文波同意取消订单','2018-09-22 03:32:12',119,'罗文波',0,0),(124,536,'流转取消','罗文波同意取消订单','2018-09-22 03:32:37',119,'罗文波',0,0),(125,2124,'流转取消','罗文波恢复订单','2018-09-25 02:14:53',119,'罗文波',0,0),(126,2124,'流转取消','罗文波恢复订单','2018-09-25 02:14:57',119,'罗文波',0,0),(127,2016,'流转取消','莫诗域请求取消订单','2018-09-25 07:57:16',140,'莫诗域',0,0),(128,2017,'流转取消','莫诗域请求取消订单','2018-09-25 07:58:05',140,'莫诗域',0,0),(129,921,'流转取消','梁倩请求取消订单','2018-09-25 08:06:34',296,'梁倩',0,0),(130,2017,'流转取消','罗文波同意取消订单','2018-09-25 08:08:56',119,'罗文波',0,0),(131,2016,'流转取消','罗文波同意取消订单','2018-09-25 08:09:07',119,'罗文波',0,0),(132,921,'流转取消','罗文波同意取消订单','2018-09-25 08:09:27',119,'罗文波',0,0),(133,2598,'流转取消','梁倩请求取消订单','2018-09-26 04:28:55',296,'梁倩',0,0),(134,3036,'流转取消','叶梓英请求取消订单','2018-09-26 06:14:25',380,'叶梓英',0,0),(135,2598,'流转取消','罗文波同意取消订单','2018-09-26 06:48:02',119,'罗文波',0,0),(136,3036,'流转取消','罗文波同意取消订单','2018-09-26 06:50:06',119,'罗文波',0,0),(137,1430,'流转取消','刘建光请求取消订单','2018-09-27 03:31:44',141,'刘建光',0,0),(138,1430,'流转取消','罗文波同意取消订单','2018-09-27 03:34:42',119,'罗文波',0,0),(139,2429,'流转取消','陈勇极请求取消订单','2018-09-29 02:06:28',139,'陈勇极',0,0),(140,2429,'流转取消','罗文波同意取消订单','2018-09-29 02:23:43',119,'罗文波',0,0),(141,2505,'流转取消','刘建光请求取消订单','2018-10-08 00:59:15',141,'刘建光',0,0),(142,2505,'流转取消','罗文波同意取消订单','2018-10-08 01:52:17',119,'罗文波',0,0),(143,2729,'流转取消','莫诗域请求取消订单','2018-10-08 09:11:22',140,'莫诗域',0,0),(144,2729,'流转取消','罗文波同意取消订单','2018-10-08 10:09:21',119,'罗文波',0,0),(145,2008,'流转取消','陈勇极请求取消订单','2018-10-11 02:18:59',139,'陈勇极',0,0),(146,2008,'流转取消','罗文波同意取消订单','2018-10-11 05:38:04',119,'罗文波',0,0),(147,3139,'流转取消','陈小银请求取消订单','2018-10-11 08:47:13',106,'陈小银',0,0),(148,3139,'流转取消','罗文波同意取消订单','2018-10-12 06:57:34',119,'罗文波',0,0),(149,3116,'流转取消','陶君怡请求取消订单','2018-10-15 02:08:20',269,'陶君怡',0,0),(150,969,'流转取消','刘建光请求取消订单','2018-10-15 03:21:35',141,'刘建光',0,0),(151,664,'流转取消','刘建光请求取消订单','2018-10-15 03:22:18',141,'刘建光',0,0),(152,3116,'流转取消','罗文波同意取消订单','2018-10-15 03:27:55',119,'罗文波',0,0),(153,969,'流转取消','罗文波同意取消订单','2018-10-15 03:29:39',119,'罗文波',0,0),(154,664,'流转取消','罗文波同意取消订单','2018-10-15 03:31:38',119,'罗文波',0,0),(155,1848,'流转取消','刘建光请求取消订单','2018-10-15 08:39:49',141,'刘建光',0,0),(156,1848,'流转取消','罗文波同意取消订单','2018-10-16 02:19:29',119,'罗文波',0,0),(157,2044,'流转取消','莫诗域请求取消订单','2018-10-16 02:59:17',140,'莫诗域',0,0),(158,2044,'流转取消','罗文波同意取消订单','2018-10-16 06:07:39',119,'罗文波',0,0),(159,2141,'流转取消','陈勇极请求取消订单','2018-10-18 06:49:04',139,'陈勇极',0,0),(160,2142,'流转取消','陈勇极请求取消订单','2018-10-18 06:49:16',139,'陈勇极',0,0),(161,3562,'流转取消','陈小银请求取消订单','2018-10-19 02:24:13',106,'陈小银',0,0),(162,3477,'流转取消','梁倩请求取消订单','2018-10-19 07:39:56',296,'梁倩',0,0),(163,3562,'流转取消','罗文波同意取消订单','2018-10-19 09:11:46',119,'罗文波',0,0),(164,3477,'流转取消','罗文波同意取消订单','2018-10-19 09:12:38',119,'罗文波',0,0),(165,2142,'流转取消','罗文波同意取消订单','2018-10-19 09:21:45',119,'罗文波',0,0),(166,2141,'流转取消','罗文波同意取消订单','2018-10-19 09:22:06',119,'罗文波',0,0),(167,3292,'流转取消','刘建光请求取消订单','2018-10-22 01:25:15',141,'刘建光',0,0),(168,3292,'流转取消','罗文波同意取消订单','2018-10-22 02:48:13',119,'罗文波',0,0),(169,2175,'流转取消','钟明霞请求取消订单','2018-10-22 08:24:10',137,'钟明霞',0,0),(170,2175,'流转取消','罗文波同意取消订单','2018-10-23 00:57:10',119,'罗文波',0,0),(171,3544,'流转取消','莫诗域请求取消订单','2018-10-23 06:27:02',140,'莫诗域',0,0),(172,3544,'流转取消','罗文波同意取消订单','2018-10-23 08:34:59',119,'罗文波',0,0),(173,3456,'流转取消','莫诗域请求取消订单','2018-10-24 06:25:11',140,'莫诗域',0,0),(174,3456,'流转取消','罗文波同意取消订单','2018-10-24 07:02:31',119,'罗文波',0,0),(175,2754,'流转取消','李佳欣请求取消订单','2018-10-25 02:52:16',268,'李佳欣',0,0),(176,3403,'流转取消','梁倩请求取消订单','2018-10-25 08:01:22',296,'梁倩',0,0),(177,3402,'流转取消','梁倩请求取消订单','2018-10-25 08:02:01',296,'梁倩',0,0),(178,3403,'流转取消','刘建光请求取消订单','2018-10-25 08:02:20',141,'刘建光',0,0),(179,3402,'流转取消','刘建光请求取消订单','2018-10-25 08:02:32',141,'刘建光',0,0),(180,3403,'流转取消','罗文波同意取消订单','2018-10-26 00:48:21',119,'罗文波',0,0),(181,3402,'流转取消','罗文波同意取消订单','2018-10-26 00:49:13',119,'罗文波',0,0),(182,2754,'流转取消','罗文波同意取消订单','2018-10-26 00:49:36',119,'罗文波',0,0),(183,3403,'流转取消','罗文波同意取消订单','2018-10-26 00:49:50',119,'罗文波',0,0),(184,3402,'流转取消','罗文波同意取消订单','2018-10-26 00:50:05',119,'罗文波',0,0),(185,3379,'流转取消','陈勇极请求取消订单','2018-10-26 03:12:24',139,'陈勇极',0,0),(186,3379,'流转取消','罗文波同意取消订单','2018-10-29 08:40:59',119,'罗文波',0,0),(187,3624,'流转取消','陈勇极请求取消订单','2018-10-30 07:31:29',139,'陈勇极',0,0),(188,3882,'流转取消','刘建光请求取消订单','2018-10-30 07:32:23',141,'刘建光',0,0),(189,3024,'流转取消','陈勇极请求取消订单','2018-10-30 07:35:53',139,'陈勇极',0,0),(190,3624,'流转取消','罗文波同意取消订单','2018-10-30 09:29:15',119,'罗文波',0,0),(191,2979,'流转取消','陈静玲请求取消订单','2018-10-31 01:06:52',381,'陈静玲',0,0),(192,3769,'流转取消','刘建光请求取消订单','2018-10-31 01:16:07',141,'刘建光',0,0),(193,3769,'流转取消','罗文波同意取消订单','2018-10-31 09:11:54',119,'罗文波',0,0),(194,3024,'流转取消','罗文波同意取消订单','2018-10-31 09:12:34',119,'罗文波',0,0),(195,2979,'流转取消','罗文波同意取消订单','2018-10-31 10:24:36',119,'罗文波',0,0),(196,3883,'流转取消','梁倩请求取消订单','2018-11-02 05:41:09',296,'梁倩',0,0),(197,456,'流转取消','刘建光请求取消订单','2018-11-02 07:54:25',141,'刘建光',0,0),(198,3883,'流转取消','罗文波同意取消订单','2018-11-05 01:45:21',119,'罗文波',0,0),(199,456,'流转取消','罗文波同意取消订单','2018-11-05 02:41:42',119,'罗文波',0,0),(200,1029,'流转取消','莫诗域请求取消订单','2018-11-06 01:55:49',140,'莫诗域',0,0),(201,4127,'流转取消','陈静玲请求取消订单','2018-11-06 02:55:12',381,'陈静玲',0,0),(202,4127,'流转取消','陈静玲请求取消订单','2018-11-06 02:55:26',381,'陈静玲',0,0),(203,1029,'流转取消','罗文波同意取消订单','2018-11-06 06:17:29',119,'罗文波',0,0),(204,4127,'流转取消','罗文波同意取消订单','2018-11-06 06:19:12',119,'罗文波',0,0),(205,4127,'流转取消','罗文波同意取消订单','2018-11-06 06:19:16',119,'罗文波',0,0),(206,1053,'流转取消','陈勇极请求取消订单','2018-11-08 01:34:19',139,'陈勇极',0,0),(207,1053,'流转取消','陈勇极请求取消订单','2018-11-08 01:34:23',139,'陈勇极',0,0),(208,1053,'流转取消','罗文波同意取消订单','2018-11-09 01:09:00',119,'罗文波',0,0),(209,1053,'流转取消','罗文波同意取消订单','2018-11-09 01:09:03',119,'罗文波',0,0),(210,4256,'流转取消','陈小银请求取消订单','2018-11-09 05:56:47',106,'陈小银',0,0),(211,1516,'流转取消','梁倩请求取消订单','2018-11-12 05:54:27',296,'梁倩',0,0),(212,1516,'流转取消','罗文波同意取消订单','2018-11-13 01:34:46',119,'罗文波',0,0),(213,4193,'流转取消','陈小银请求取消订单','2018-11-14 03:10:01',106,'陈小银',0,0),(214,4193,'流转取消','罗文波同意取消订单','2018-11-14 03:17:22',119,'罗文波',0,0),(215,4193,'流转取消','罗文波同意取消订单','2018-11-14 03:17:22',119,'罗文波',0,0),(216,4193,'流转取消','罗文波同意取消订单','2018-11-14 03:17:23',119,'罗文波',0,0),(217,4050,'流转取消','陈月娇请求取消订单','2018-11-14 09:16:02',210,'陈月娇',0,0),(218,1575,'流转取消','钟明霞请求取消订单','2018-11-14 09:42:39',137,'钟明霞',0,0),(219,1572,'流转取消','钟明霞请求取消订单','2018-11-14 09:43:00',137,'钟明霞',0,0),(220,1575,'流转取消','罗文波同意取消订单','2018-11-14 09:43:48',119,'罗文波',0,0),(221,1572,'流转取消','罗文波同意取消订单','2018-11-14 09:44:05',119,'罗文波',0,0),(222,3443,'流转取消','钟明霞请求取消订单','2018-11-14 09:46:11',137,'钟明霞',0,0),(223,4050,'流转取消','李杰请求取消订单','2018-11-14 09:46:55',239,'李杰',0,0),(224,4050,'流转取消','罗文波同意取消订单','2018-11-14 09:47:35',119,'罗文波',0,0),(225,4050,'流转取消','罗文波同意取消订单','2018-11-14 09:47:52',119,'罗文波',0,0),(226,3443,'流转取消','罗文波同意取消订单','2018-11-14 09:48:13',119,'罗文波',0,0),(227,504,'流转取消','钟明霞请求取消订单','2018-11-15 07:25:40',137,'钟明霞',0,0),(228,504,'流转取消','罗文波同意取消订单','2018-11-15 07:26:17',119,'罗文波',0,0),(229,428,'流转取消','钟明霞请求取消订单','2018-11-15 07:41:37',137,'钟明霞',0,0),(230,428,'流转取消','罗文波同意取消订单','2018-11-15 07:42:02',119,'罗文波',0,0),(231,4186,'流转取消','叶梓英请求取消订单','2018-11-15 08:06:20',380,'叶梓英',0,0),(232,4186,'流转取消','罗文波同意取消订单','2018-11-15 08:07:38',119,'罗文波',0,0),(233,2622,'流转取消','莫诗域请求取消订单','2018-11-15 08:11:12',140,'莫诗域',0,0),(234,2622,'流转取消','罗文波同意取消订单','2018-11-15 08:23:19',119,'罗文波',0,0),(235,4108,'流转取消','陈小银请求取消订单','2018-11-15 08:48:39',106,'陈小银',0,0),(236,4108,'流转取消','罗文波同意取消订单','2018-11-15 08:55:15',119,'罗文波',0,0),(237,4278,'流转取消','王坚请求取消订单','2018-11-15 09:00:52',138,'王坚',0,0),(238,4278,'流转取消','罗文波同意取消订单','2018-11-15 09:03:42',119,'罗文波',0,0),(239,2049,'流转取消','刘建光请求取消订单','2018-11-16 02:59:26',141,'刘建光',0,0),(240,2050,'流转取消','刘建光请求取消订单','2018-11-16 02:59:49',141,'刘建光',0,0),(241,2050,'流转取消','罗文波同意取消订单','2018-11-16 04:03:14',119,'罗文波',0,0),(242,2049,'流转取消','罗文波同意取消订单','2018-11-16 04:03:26',119,'罗文波',0,0),(243,1736,'流转取消','梁倩请求取消订单','2018-11-16 07:22:39',296,'梁倩',0,0),(244,1736,'流转取消','罗文波同意取消订单','2018-11-16 07:23:25',119,'罗文波',0,0),(245,2083,'流转取消','陈勇极请求取消订单','2018-11-16 09:23:16',139,'陈勇极',0,0),(246,2083,'流转取消','罗文波同意取消订单','2018-11-16 09:24:40',119,'罗文波',0,0),(247,3213,'流转取消','李杰请求取消订单','2018-11-20 02:17:54',239,'李杰',0,0),(248,3213,'流转取消','罗文波同意取消订单','2018-11-20 02:19:32',119,'罗文波',0,0),(249,3360,'流转取消','莫诗域请求取消订单','2018-11-21 09:15:29',140,'莫诗域',0,0),(250,3360,'流转取消','莫诗域请求取消订单','2018-11-21 09:24:57',140,'莫诗域',0,0),(251,456,'流转取消','陈月娇请求取消订单','2018-11-22 06:01:36',210,'陈月娇',0,0),(252,456,'流转取消','罗文波同意取消订单','2018-11-22 06:04:20',119,'罗文波',0,0),(253,3330,'流转取消','梁倩请求取消订单','2018-11-23 01:28:42',296,'梁倩',0,0),(254,1452,'流转取消','梁倩请求取消订单','2018-11-23 01:30:12',296,'梁倩',0,0),(255,3213,'流转取消','陈月娇请求取消订单','2018-11-23 01:38:34',210,'陈月娇',0,0),(256,3330,'流转取消','罗文波同意取消订单','2018-11-23 02:09:43',119,'罗文波',0,0),(257,3213,'流转取消','罗文波同意取消订单','2018-11-23 02:10:04',119,'罗文波',0,0),(258,1452,'流转取消','罗文波同意取消订单','2018-11-23 02:10:21',119,'罗文波',0,0),(259,2024,'流转取消','李杰请求取消订单','2018-11-23 02:22:47',239,'李杰',0,0),(260,2024,'流转取消','李杰请求取消订单','2018-11-23 02:22:49',239,'李杰',0,0),(261,2024,'流转取消','罗文波同意取消订单','2018-11-23 02:24:06',119,'罗文波',0,0),(262,2024,'流转取消','陈月娇请求取消订单','2018-11-23 02:24:58',210,'陈月娇',0,0),(263,2024,'流转取消','罗文波同意取消订单','2018-11-23 02:28:39',119,'罗文波',0,0),(264,1867,'流转取消','刘建光请求取消订单','2018-11-23 03:29:41',141,'刘建光',0,0),(265,1867,'流转取消','罗文波同意取消订单','2018-11-23 03:30:34',119,'罗文波',0,0),(266,2212,'流转取消','陈月娇请求取消订单','2018-11-23 06:02:51',210,'陈月娇',0,0),(267,2390,'流转取消','李杰请求取消订单','2018-11-28 01:56:45',239,'李杰',0,0),(268,2390,'流转取消','罗文波同意取消订单','2018-11-28 02:31:41',119,'罗文波',0,0),(269,4188,'流转取消','陈月娇请求取消订单','2018-11-28 03:28:02',210,'陈月娇',0,0),(270,4188,'流转取消','罗文波同意取消订单','2018-11-28 03:30:22',119,'罗文波',0,0),(271,4188,'流转取消','李杰请求取消订单','2018-11-28 03:39:01',239,'李杰',0,0),(272,4188,'流转取消','罗文波同意取消订单','2018-11-28 03:50:59',119,'罗文波',0,0),(273,2212,'流转取消','罗文波同意取消订单','2018-11-28 07:44:03',119,'罗文波',0,0),(274,2212,'流转取消','罗文波恢复订单','2018-11-28 07:44:06',119,'罗文波',0,0),(275,4345,'流转取消','陈小银请求取消订单','2018-11-30 02:37:57',106,'陈小银',0,0),(276,4952,'流转取消','梁倩请求取消订单','2018-11-30 06:28:02',296,'梁倩',0,0),(277,4952,'流转取消','罗文波同意取消订单','2018-11-30 06:47:28',119,'罗文波',0,0),(278,4345,'流转取消','罗文波同意取消订单','2018-11-30 06:48:02',119,'罗文波',0,0),(279,2991,'流转取消','梁倩请求取消订单','2018-11-30 07:23:40',296,'梁倩',0,0),(280,2991,'流转取消','罗文波同意取消订单','2018-11-30 07:25:34',119,'罗文波',0,0),(281,4164,'流转取消','陈静玲请求取消订单','2018-11-30 07:39:25',381,'陈静玲',0,0),(282,4164,'流转取消','陈静玲请求取消订单','2018-11-30 07:39:35',381,'陈静玲',0,0),(283,4164,'流转取消','罗文波同意取消订单','2018-11-30 08:58:05',119,'罗文波',0,0),(284,4164,'流转取消','罗文波同意取消订单','2018-11-30 09:05:55',119,'罗文波',0,0),(285,4947,'流转取消','陈月娇请求取消订单','2018-12-01 03:43:50',210,'陈月娇',0,0),(286,4945,'流转取消','陈月娇请求取消订单','2018-12-01 03:44:28',210,'陈月娇',0,0),(287,4947,'流转取消','罗文波同意取消订单','2018-12-01 06:19:26',119,'罗文波',0,0),(288,4945,'流转取消','罗文波同意取消订单','2018-12-01 06:19:52',119,'罗文波',0,0),(289,4952,'流转取消','罗文波恢复订单','2018-12-03 03:40:38',119,'罗文波',0,0),(290,4952,'流转取消','罗文波恢复订单','2018-12-03 03:40:39',119,'罗文波',0,0),(291,2991,'流转取消','刘建光请求取消订单','2018-12-03 04:02:48',141,'刘建光',0,0),(292,2991,'流转取消','刘建光请求取消订单','2018-12-03 04:02:52',141,'刘建光',0,0),(293,2991,'流转取消','罗文波同意取消订单','2018-12-03 04:04:47',119,'罗文波',0,0),(294,2991,'流转取消','罗文波同意取消订单','2018-12-03 04:04:51',119,'罗文波',0,0),(295,4945,'流转取消','罗文波恢复订单','2018-12-03 10:20:20',119,'罗文波',0,0),(296,4947,'流转取消','罗文波恢复订单','2018-12-03 10:22:03',119,'罗文波',0,0),(297,2390,'流转取消','陈月娇请求取消订单','2018-12-03 11:03:56',210,'陈月娇',0,0),(298,2390,'流转取消','罗文波同意取消订单','2018-12-04 00:48:08',119,'罗文波',0,0),(299,4247,'流转取消','刘建光请求取消订单','2018-12-04 01:54:58',141,'刘建光',0,0),(300,4247,'流转取消','罗文波同意取消订单','2018-12-04 02:59:22',119,'罗文波',0,0),(301,2212,'流转取消','陈月娇请求取消订单','2018-12-04 03:01:51',210,'陈月娇',0,0),(302,2212,'流转取消','罗文波同意取消订单','2018-12-04 03:02:32',119,'罗文波',0,0),(303,1170,'流转取消','梁倩请求取消订单','2018-12-04 05:51:05',296,'梁倩',0,0),(304,1170,'流转取消','罗文波同意取消订单','2018-12-04 05:59:04',119,'罗文波',0,0),(305,1017,'流转取消','梁倩请求取消订单','2018-12-05 03:55:01',296,'梁倩',0,0),(306,1017,'流转取消','罗文波同意取消订单','2018-12-05 04:22:32',119,'罗文波',0,0),(307,2663,'流转取消','梁倩请求取消订单','2018-12-06 01:23:18',296,'梁倩',0,0),(308,2663,'流转取消','罗文波同意取消订单','2018-12-06 01:30:41',119,'罗文波',0,0),(309,2663,'流转取消','刘建光请求取消订单','2018-12-06 01:31:37',141,'刘建光',0,0),(310,2663,'流转取消','罗文波同意取消订单','2018-12-06 01:31:56',119,'罗文波',0,0),(311,1204,'流转取消','梁倩请求取消订单','2018-12-06 06:11:32',296,'梁倩',0,0),(312,1204,'流转取消','陈勇极请求取消订单','2018-12-06 06:15:54',139,'陈勇极',0,0),(313,1204,'流转取消','陈勇极请求取消订单','2018-12-06 06:15:55',139,'陈勇极',0,0),(314,1204,'流转取消','罗文波同意取消订单','2018-12-06 06:19:45',119,'罗文波',0,0),(315,1204,'流转取消','罗文波同意取消订单','2018-12-06 06:19:48',119,'罗文波',0,0),(316,3273,'流转取消','刘建光请求取消订单','2018-12-10 03:01:21',141,'刘建光',0,0),(317,3273,'流转取消','罗文波同意取消订单','2018-12-11 00:58:42',119,'罗文波',0,0),(318,1944,'流转取消','刘建光请求取消订单','2018-12-11 02:19:38',141,'刘建光',0,0),(319,1944,'流转取消','罗文波同意取消订单','2018-12-11 02:21:53',119,'罗文波',0,0),(320,5299,'流转取消','陈小银请求取消订单','2018-12-11 03:12:24',106,'陈小银',0,0),(321,5299,'流转取消','罗文波同意取消订单','2018-12-11 03:17:11',119,'罗文波',0,0),(322,3990,'流转取消','刘建光请求取消订单','2018-12-12 02:17:18',141,'刘建光',0,0),(323,3990,'流转取消','罗文波同意取消订单','2018-12-12 02:19:21',119,'罗文波',0,0),(324,1887,'流转取消','莫诗域请求取消订单','2018-12-12 08:55:11',140,'莫诗域',0,0),(325,1887,'流转取消','罗文波同意取消订单','2018-12-12 09:06:59',119,'罗文波',0,0),(326,1210,'流转取消','陈勇极请求取消订单','2018-12-12 09:07:54',139,'陈勇极',0,0),(327,1210,'流转取消','罗文波同意取消订单','2018-12-12 09:07:57',119,'罗文波',0,0),(328,5233,'流转取消','刘建光请求取消订单','2018-12-13 01:15:01',141,'刘建光',0,0),(329,5233,'流转取消','罗文波同意取消订单','2018-12-13 01:47:15',119,'罗文波',0,0),(330,831,'流转取消','廖小捷请求取消订单','2018-12-13 03:18:41',154,'廖小捷',0,0),(331,831,'流转取消','罗文波同意取消订单','2018-12-13 03:19:45',119,'罗文波',0,0),(332,831,'流转取消','罗文波恢复订单','2018-12-13 03:19:53',119,'罗文波',0,0),(333,828,'流转取消','廖小捷请求取消订单','2018-12-13 03:24:45',154,'廖小捷',0,0),(334,828,'流转取消','罗文波同意取消订单','2018-12-13 03:24:58',119,'罗文波',0,0),(335,3124,'流转取消','王坚请求取消订单','2018-12-13 08:40:55',138,'王坚',0,0),(336,3124,'流转取消','罗文波同意取消订单','2018-12-13 09:05:46',119,'罗文波',0,0),(337,5232,'流转取消','陈勇极请求取消订单','2018-12-14 05:56:45',139,'陈勇极',0,0),(338,5232,'流转取消','陈勇极请求取消订单','2018-12-14 05:56:50',139,'陈勇极',0,0),(339,5232,'流转取消','罗文波同意取消订单','2018-12-14 05:57:40',119,'罗文波',0,0),(340,5232,'流转取消','罗文波同意取消订单','2018-12-14 05:57:43',119,'罗文波',0,0),(341,4874,'流转取消','陈勇极请求取消订单','2018-12-14 05:58:49',139,'陈勇极',0,0),(342,4874,'流转取消','罗文波同意取消订单','2018-12-14 05:59:08',119,'罗文波',0,0),(343,3273,'流转取消','罗文波恢复订单','2018-12-14 06:11:42',119,'罗文波',0,0),(344,5161,'流转取消','陈静玲请求取消订单','2018-12-18 08:37:32',381,'陈静玲',0,0),(345,5166,'流转取消','刘建光请求取消订单','2018-12-19 00:58:02',141,'刘建光',0,0),(346,5166,'流转取消','罗文波同意取消订单','2018-12-19 01:16:06',119,'罗文波',0,0),(347,5161,'流转取消','罗文波同意取消订单','2018-12-19 01:16:37',119,'罗文波',0,0),(348,5184,'注销业务','李杰 确认 待审核','2018-12-30 05:50:44',239,'李杰',40108,0),(349,5184,'注销业务','李杰 确认 待审核','2018-12-30 05:50:48',239,'李杰',40108,0),(350,5184,'注销业务','李杰 确认完成 待审核','2018-12-30 05:53:31',239,'李杰',40108,0),(351,5184,'注销业务','李杰 确认完成 待审核','2018-12-30 06:39:02',239,'李杰',40108,0),(352,5184,'注销业务','李杰 确认完成 执照银行','2018-12-30 06:41:10',239,'李杰',40108,0),(353,5184,'注销业务','李杰 取消李杰确认 清算登报','2018-12-30 06:45:18',239,'李杰',40108,0),(354,5184,'注销业务','李杰 确认完成 国地税(待审核)','2018-12-30 06:47:05',239,'李杰',40108,0),(355,5184,'注销业务','李杰 取消李杰确认 清算登报','2018-12-30 06:47:41',239,'李杰',40108,0),(356,5184,'注销业务','李杰 取消(李杰)确认 执照银行','2018-12-30 06:48:12',239,'李杰',40108,0),(357,5184,'注销业务','李杰 取消(李杰)确认 国地税','2018-12-30 07:00:24',239,'李杰',40108,0),(358,5184,'注销业务','李杰 确认完成 清算登报(待审核)','2018-12-30 07:01:01',239,'李杰',40108,0),(359,5184,'注销业务','李杰 确认完成 执照银行(待审核)','2018-12-30 07:09:41',239,'李杰',40108,0),(360,5184,'注销业务','李杰 确认(李杰)办结 清算登报','2018-12-30 07:10:28',239,'李杰',40108,0),(361,5184,'注销业务','李杰 确认完成 国地税(待审核)','2018-12-30 07:11:01',239,'李杰',40108,0),(362,5184,'注销业务','李杰 取消(李杰)确认 国地税','2018-12-30 07:11:03',239,'李杰',40108,0),(363,5184,'注销业务','李杰 取消(李杰)确认 执照银行','2018-12-30 07:11:05',239,'李杰',40108,0),(364,5184,'注销业务','李杰 取消(李杰)确认 清算登报','2018-12-30 07:11:07',239,'李杰',40108,0),(365,5184,'注销业务','李杰 确认完成 清算登报(待审核)','2018-12-30 07:11:15',239,'李杰',40108,0),(366,5184,'注销业务','李杰 确认(李杰)办结 清算登报','2018-12-30 07:11:18',239,'李杰',40108,0),(367,5184,'注销业务','李杰 确认完成 执照银行(待审核)','2018-12-30 07:11:59',239,'李杰',40108,0),(368,5184,'注销业务','李杰 确认完成 国地税(待审核)','2018-12-30 07:12:02',239,'李杰',40108,0),(369,5184,'注销业务','李杰 确认(李杰)办结 清算登报','2018-12-30 07:12:04',239,'李杰',40108,0),(370,5184,'注销业务','李杰 确认(李杰)办结 执照银行','2018-12-30 07:17:45',239,'李杰',40108,0),(371,5184,'注销业务','李杰 确认(李杰)办结 国地税','2018-12-30 07:17:47',239,'李杰',40108,0),(372,5184,'注销业务','李杰 取消(李杰)确认 国地税','2018-12-30 07:17:53',239,'李杰',40108,0),(373,5184,'注销业务','李杰 确认完成 国地税(待审核)','2018-12-30 07:20:06',239,'李杰',40108,0),(374,5184,'注销业务','何诗明 确认(李杰)办结 国地税','2018-12-30 07:23:36',95,'何诗明',40108,0),(375,5184,'注销业务','何诗明 确认(李杰)办结 国地税','2018-12-30 08:02:38',95,'何诗明',40108,0),(376,5436,'注销业务','李杰 确认完成 清算登报(待审核)','2018-12-30 08:12:35',239,'李杰',42331,0),(377,5436,'注销业务','何诗明 确认(李杰)办结 清算登报','2018-12-30 08:13:32',95,'何诗明',42331,0),(378,5436,'注销业务','李杰 确认完成 执照银行(待审核)','2018-12-30 08:15:09',239,'李杰',42331,0),(379,5436,'注销业务','何诗明 取消(李杰)确认 执照银行','2018-12-30 08:15:21',95,'何诗明',42331,0),(380,5436,'注销业务','李杰 确认完成 执照银行(待审核)','2018-12-30 08:37:21',239,'李杰',42331,0),(381,5436,'注销业务','何诗明 取消(李杰)确认 执照银行','2018-12-30 08:37:56',95,'何诗明',42331,0),(382,5436,'注销业务','李杰 确认完成 国地税(待审核)','2018-12-30 08:40:32',239,'李杰',42331,0),(383,5436,'注销业务','何诗明 取消(李杰)确认 国地税','2018-12-30 09:18:06',95,'何诗明',42331,0),(384,5224,'注销业务','李杰 确认完成 清算登报(待审核)','2018-12-30 09:18:48',239,'李杰',40411,0),(385,5224,'注销业务','何诗明 取消(李杰)确认 清算登报','2018-12-30 09:22:11',95,'何诗明',40411,0),(386,5224,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-02 00:52:57',239,'李杰',40411,0),(387,5224,'注销业务','李杰 确认完成 国地税(待审核)','2019-01-02 01:05:10',239,'李杰',40411,0),(388,5224,'注销业务','何诗明 取消(李杰)确认 国地税','2019-01-02 01:09:26',95,'何诗明',40411,0),(389,5436,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-02 08:44:22',116,'陈太智',42331,0),(390,5224,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-02 08:45:07',116,'陈太智',40411,0),(391,5224,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-02 08:45:15',116,'陈太智',40411,0),(392,5224,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-02 08:45:24',116,'陈太智',40411,0),(393,5224,'注销业务','陈太智 取消(李杰)确认 国地税','2019-01-02 08:50:26',116,'陈太智',40411,0),(394,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:50:42',116,'陈太智',40411,0),(395,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:50:49',116,'陈太智',40411,0),(396,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:51:18',116,'陈太智',40411,0),(397,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:51:21',116,'陈太智',40411,0),(398,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:51:24',116,'陈太智',40411,0),(399,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:51:56',116,'陈太智',40411,0),(400,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:52:03',116,'陈太智',40411,0),(401,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:52:09',116,'陈太智',40411,0),(402,5224,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-02 08:56:50',116,'陈太智',40411,0),(403,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:56:55',116,'陈太智',40411,0),(404,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:57:00',116,'陈太智',40411,0),(405,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:58:27',116,'陈太智',40411,0),(406,5224,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:58:37',116,'陈太智',40411,0),(407,5436,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-02 08:59:11',116,'陈太智',42331,0),(408,5119,'注销业务','李杰 确认完成 清算登报(待审核)','2019-01-03 05:57:06',239,'李杰',39399,0),(409,5119,'注销业务','陈太智 确认(李杰)办结 清算登报','2019-01-03 06:33:40',116,'陈太智',39399,0),(410,5119,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-03 06:34:25',239,'李杰',39399,0),(411,5119,'注销业务','陈太智 取消(李杰)确认 执照银行','2019-01-03 06:34:38',116,'陈太智',39399,0),(412,5119,'注销业务','李杰 确认完成 国地税(待审核)','2019-01-03 06:37:58',239,'李杰',39399,0),(413,5119,'注销业务','陈太智 取消(李杰)确认 国地税','2019-01-03 06:40:15',116,'陈太智',39399,0),(414,5119,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-03 10:00:44',239,'李杰',39399,0),(415,5119,'注销业务','李杰 确认完成 国地税(待审核)','2019-01-03 10:01:21',239,'李杰',39399,0),(416,5119,'注销业务','陈太智 确认(李杰)办结 国地税','2019-01-03 10:02:06',116,'陈太智',39399,0),(417,5119,'注销业务','陈太智 取消(李杰)确认 执照银行','2019-01-03 10:10:07',116,'陈太智',39399,0),(418,5119,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-03 10:10:22',239,'李杰',39399,0),(419,5119,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-03 10:10:32',116,'陈太智',39399,0),(420,5120,'注销业务','李杰 确认完成 清算登报(待审核)','2019-01-04 01:05:09',239,'李杰',39397,0),(421,5120,'注销业务','陈太智 取消(李杰)确认 清算登报','2019-01-04 01:05:34',116,'陈太智',39397,0),(422,5120,'注销业务','李杰 确认完成 清算登报(待审核)','2019-01-04 01:08:14',239,'李杰',39397,0),(423,5120,'注销业务','陈太智 确认(李杰)办结 清算登报','2019-01-04 01:08:25',116,'陈太智',39397,0),(424,5120,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-04 01:55:55',239,'李杰',39397,0),(425,5120,'注销业务','陈太智 取消(李杰)确认 执照银行','2019-01-04 01:56:12',116,'陈太智',39397,0),(426,5120,'注销业务','李杰 确认完成 执照银行(待审核)','2019-01-04 01:56:25',239,'李杰',39397,0),(427,5120,'注销业务','陈太智 确认(李杰)办结 执照银行','2019-01-04 01:56:33',116,'陈太智',39397,0),(428,5574,'业务信息',',客户姓名:张卫1 修改为 张卫','2019-03-15 08:21:23',116,'陈太智',0,0),(429,5574,'业务信息','客户姓名:张卫 修改为 张卫1','2019-03-15 08:22:38',116,'陈太智',0,0),(430,5574,'业务信息','优惠活动:钜惠套餐 修改为 ,签约方式:现场 修改为 远程,合同情况:无合同 修改为 已收合同,业务内容:广州亚建工程设计咨询有限公司 修改为 好的,客户姓名:张卫1 修改为 张卫,联系电话: 修改为 123','2019-03-15 08:23:26',116,'陈太智',0,0),(431,5574,'业务信息','优惠活动: 修改为 钜惠套餐','2019-03-15 08:25:34',116,'陈太智',0,0),(432,5574,'业务信息','企业名称:广州亚建工程设计咨询有限公司6 修改为 广州亚建工程设计咨询有限公司','2019-03-15 08:32:25',116,'陈太智',0,0),(433,1844,'关联订单','1844关联5124','2019-03-15 08:33:51',116,'陈太智',0,0),(434,8506,'业务信息','签约方式:外出签单 修改为 远程','2019-03-18 03:01:41',176,'李洁韩',0,0),(435,0,'修改客户',',优惠活动: 修改为 ,执照期限:2019-03-12 修改为 2019-03-18','2019-03-18 03:25:11',176,'李洁韩',0,5157),(436,0,'修改客户',',优惠活动: 修改为 ,成立日期:None 修改为 2019-03-19,执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:25:21',176,'李洁韩',0,5157),(437,0,'修改客户',',成立日期:2019-03-19 修改为 2019-03-19 00:00:00,执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:33:28',176,'李洁韩',0,5157),(438,0,'修改客户',',执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:33:38',176,'李洁韩',0,5157),(439,0,'修改客户',',执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:33:38',176,'李洁韩',0,5157),(440,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:40:54',176,'李洁韩',0,5157),(441,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:10',176,'李洁韩',0,5157),(442,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:17',176,'李洁韩',0,5157),(443,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:17',176,'李洁韩',0,5157),(444,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:17',176,'李洁韩',0,5157),(445,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:17',176,'李洁韩',0,5157),(446,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:41:18',176,'李洁韩',0,5157),(447,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:42:24',176,'李洁韩',0,5157),(448,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:43:55',176,'李洁韩',0,5157),(449,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:44:08',176,'李洁韩',0,5157),(450,0,'修改客户','执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:44:11',176,'李洁韩',0,5157),(451,0,'修改客户','注册地址: 修改为 广州市海珠123,信用评级: 修改为 A,执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:45:15',176,'李洁韩',0,5157),(452,0,'修改客户','一般纳税人改为是,注册地址:广州市海珠123 修改为 ,执照期限:2019-03-18 修改为 2019-03-18 00:00:00','2019-03-18 03:46:03',176,'李洁韩',0,5157),(453,1844,'业务信息','加急业务:改为是,成交周期(天）0 修改为 1,预计合同定金:0 修改为 1','2019-03-18 06:12:15',116,'陈太智',0,0),(454,0,'修改客户','成立日期:None 修改为 2019-03-05','2019-03-18 08:16:06',176,'李洁韩',0,5150),(455,0,'修改客户','成立日期:2019-03-05 修改为 2019-03-05 00:00:00','2019-03-18 08:16:36',176,'李洁韩',0,5150),(456,0,'修改客户','成立日期:2019-03-05 00:00:00 修改为 2019-03-19','2019-03-18 08:21:56',176,'李洁韩',0,5150),(457,1362,'注销业务','王坚 确认完成 清算登报(待审核)','2019-03-19 01:23:20',138,'王坚',8133,0),(458,0,'修改客户','注册地址:00 修改为 ','2019-03-21 06:59:44',116,'陈太智',0,5156),(459,0,'修改客户','客服会计:feasd 修改为 张会会,地址类型: 修改为 123,执照期限:2019-03-18 00:00:00 修改为 2019-03-26','2019-03-26 02:46:50',116,'陈太智',0,5157),(460,0,'修改客户','执照期限:2019-03-26 00:00:00 修改为 2019-03-26','2019-03-26 02:47:03',116,'陈太智',0,5157),(461,0,'修改客户','客服会计:陈月娇 修改为 卢欣,客户类型:记账, 修改为 记账','2019-03-26 07:13:55',116,'陈太智',0,5151),(462,0,'修改客户','客服会计:卢欣 修改为 周萍','2019-03-26 07:14:43',116,'陈太智',0,5151),(463,0,'修改客户','法人: 修改为 ff','2019-03-27 01:17:42',116,'陈太智',0,3539),(464,0,'修改客户','注册地址:广州市天河广州市天河区岑村沙埔大街323号B-5栋二层0238（仅限办公） 修改为 ,地址类型:天河区开票地址 修改为 天河区开票地址1','2019-03-27 06:20:25',153,'江嘉琳',0,5129),(465,0,'修改客户','地址类型:天河区开票地址1 修改为 天河区开票地址','2019-03-27 06:20:36',153,'江嘉琳',0,5129),(466,0,'修改客户',',注册地址:广州市天河 修改为 广州市越秀','2019-03-29 05:55:50',116,'陈太智',0,5157),(467,0,'修改客户',',标签类型:记账,正常,楼盘,汇算清缴 修改为 记账,停帐,楼盘,汇算清缴,工商年检','2019-03-29 05:57:29',116,'陈太智',0,5157),(468,0,'修改客户',',首要联系电话:123456 修改为 1234567890,执照成立日期:2019-03-28 修改为 2019-03-29','2019-03-29 06:01:31',116,'陈太智',0,5157),(469,0,'修改客户',',执照成立日期:2019-03-29 修改为 None','2019-03-29 06:01:51',116,'陈太智',0,5157),(470,0,'修改客户',',执照成立日期:2019-03-30 修改为 None','2019-03-29 06:02:24',116,'陈太智',0,5157),(471,0,'修改客户',',执照成立日期:None 修改为 2019-03-27','2019-03-29 06:02:30',116,'陈太智',0,5157),(472,0,'修改客户','纳税类型:小规模 修改为 一般纳税人','2019-03-29 06:07:21',116,'陈太智',0,5157),(473,0,'修改客户','开户行: 修改为 2,地址类型: 修改为 4,银行账号: 修改为 3,所属行业: 修改为 1,专管员姓名: 修改为 5','2019-03-29 09:30:05',116,'陈太智',0,5159),(474,0,'修改客户','纳税类型:小规模 修改为 一般纳税人,税务概况: 修改为 12,税种明细: 修改为 34,税控盘类别: 修改为 565','2019-03-29 09:32:31',116,'陈太智',0,5159);
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

-- Dump completed on 2019-03-29 17:39:21
