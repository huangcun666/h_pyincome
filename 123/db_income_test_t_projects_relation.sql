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
-- Table structure for table `t_projects_relation`
--

DROP TABLE IF EXISTS `t_projects_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `relation_ids` varchar(2550) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid_names` varchar(2550) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_relation`
--

LOCK TABLES `t_projects_relation` WRITE;
/*!40000 ALTER TABLE `t_projects_relation` DISABLE KEYS */;
INSERT INTO `t_projects_relation` VALUES (1,'1942,1857,','2018-08-03 02:10:42',NULL),(2,'1914,1913,','2018-08-03 02:13:03',NULL),(3,'1962,261,','2018-08-03 02:32:08',NULL),(4,'2009,1235,','2018-08-03 02:34:05',NULL),(5,'2021,1862,','2018-08-03 02:35:20',NULL),(6,'2120,1882,1861,','2018-08-03 03:12:27',NULL),(7,'1413,811,','2018-08-06 00:40:25',NULL),(8,'321,2019,','2018-08-06 00:56:06',NULL),(9,'2049,2050,','2018-08-06 02:56:30',NULL),(10,'2162,2012,','2018-08-06 07:14:41',NULL),(11,'2057,1944,','2018-08-06 07:46:07',NULL),(12,'2169,1778,','2018-08-07 00:52:12',NULL),(13,'320,2177,','2018-08-07 02:23:51',NULL),(14,'1250,2185,','2018-08-07 05:08:40',NULL),(15,'2188,1955,','2018-08-07 05:43:02',NULL),(17,'1600,1715,','2018-08-08 07:13:07',NULL),(18,'2216,1643,','2018-08-08 08:33:06',NULL),(19,'1545,2217,','2018-08-08 08:41:15',NULL),(20,'2220,1956,','2018-08-09 02:07:44',NULL),(21,'2192,2191,','2018-08-09 03:40:07',NULL),(22,'1114,1414,','2018-08-10 01:42:10',NULL),(23,'519,635,','2018-08-10 06:41:43',NULL),(24,'592,331,','2018-08-10 06:51:40',NULL),(25,'2245,1516,','2018-08-10 06:53:27',NULL),(26,'294,1079,','2018-08-10 06:58:28',NULL),(27,'627,1319,','2018-08-10 07:06:08',NULL),(28,'1561,1464,','2018-08-13 02:39:13',NULL),(29,'2260,1973,','2018-08-13 03:06:00',NULL),(30,'2263,1324,','2018-08-13 05:50:05',NULL),(31,'1191,848,','2018-08-14 06:29:54',NULL),(32,'1726,1845,1844,','2018-08-14 06:56:48',NULL),(33,'2278,1407,','2018-08-14 08:31:25',NULL),(35,'2302,1793,','2018-08-15 03:08:32',NULL),(36,'1941,2304,','2018-08-15 03:44:08',NULL),(37,'2305,2244,','2018-08-15 06:07:09',NULL),(38,'2317,1593,','2018-08-16 02:10:12','吴凤|2317|1593,'),(39,'2320,2310,','2018-08-16 02:41:23','何健锋|2320|2310,'),(40,'2322,636,','2018-08-16 03:55:12','赵松筑|2322|636,'),(41,'2325,2294,','2018-08-16 06:23:44','庄培润|2325|2294,'),(42,'2291,784,','2018-08-16 06:29:28','罗文波|2291|784,'),(43,'2326,1149,','2018-08-16 06:35:03','庄培润|2326|1149,'),(44,'1582,2338,','2018-08-16 10:21:58','庄培润|1582|2338,'),(45,'1798,1915,','2018-08-17 03:25:37','庄培润|1798|1915,'),(46,'2353,2318,','2018-08-17 08:03:15','庄培润|2353|2318,'),(47,'2381,2337,','2018-08-21 01:50:15','庄培润|2381|2337,'),(48,'2398,491,','2018-08-21 09:43:05','庄培润|2398|491,'),(49,'2399,1543,','2018-08-21 09:47:54','庄培润|2399|1543,'),(50,'2400,2080,','2018-08-21 09:53:44','庄培润|2400|2080,'),(51,'2403,1953,','2018-08-22 01:29:41','何健锋|2403|1953,'),(52,'2437,2393,','2018-08-22 11:03:26','何健锋|2437|2393,'),(53,'2444,1980,','2018-08-23 01:31:35','罗文波|2444|1980,'),(54,'2447,1991,','2018-08-23 01:55:24','庄培润|2447|1991,'),(55,'2448,1153,','2018-08-23 02:03:01','庄培润|2448|1153,'),(56,'2081,771,2538,','2018-08-23 02:14:30','罗文波|2081|771,罗文波|771|2538,'),(57,'1148,2449,','2018-08-23 04:04:05','罗文波|1148|2449,'),(58,'2455,2430,','2018-08-23 06:48:33','朱伟峰|2455|2430,'),(59,'2461,1510,','2018-08-23 08:27:08','罗文波|2461|1510,'),(60,'2476,1818,','2018-08-24 07:34:42','何健锋|2476|1818,'),(61,'2478,777,','2018-08-24 08:05:14','罗文波|2478|777,'),(62,'600,2480,','2018-08-24 08:17:06','罗文波|600|2480,'),(63,'2500,1982,','2018-08-27 02:07:21','罗文波|2500|1982,'),(64,'2506,1606,','2018-08-27 09:50:14','吴凤|2506|1606,'),(65,'2222,2206,','2018-08-28 07:10:33','陈太智|2222|2206,'),(66,'1236,1706,','2018-08-29 00:45:42','罗文波|1236|1706,'),(67,'2534,2528,','2018-08-29 00:52:39','赵松筑|2534|2528,'),(68,'2540,819,','2018-08-29 02:42:24','吴凤|2540|819,'),(69,'2542,1898,','2018-08-29 03:56:54','何健锋|2542|1898,'),(70,'2327,1618,','2018-08-29 07:16:10','陈勇极|2327|1618,');
/*!40000 ALTER TABLE `t_projects_relation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:25
