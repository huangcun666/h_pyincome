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
-- Table structure for table `t_projects_addr_milepost`
--

DROP TABLE IF EXISTS `t_projects_addr_milepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_addr_milepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `type_name` varchar(100) DEFAULT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `confirm_at` datetime DEFAULT NULL,
  `addr_provider_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_addr_milepost`
--

LOCK TABLES `t_projects_addr_milepost` WRITE;
/*!40000 ALTER TABLE `t_projects_addr_milepost` DISABLE KEYS */;
INSERT INTO `t_projects_addr_milepost` VALUES (1,NULL,NULL,1785,'2018-07-23 07:14:44',NULL,'待接单',NULL,NULL,1),(2,NULL,NULL,1792,'2018-07-23 09:07:57',NULL,'待接单',NULL,NULL,2),(3,NULL,NULL,1794,'2018-07-24 01:33:41',NULL,'待接单',NULL,NULL,3),(4,NULL,NULL,1805,'2018-07-24 03:59:43',NULL,'待接单',NULL,NULL,4),(5,NULL,NULL,1808,'2018-07-24 04:01:06',NULL,'待接单',NULL,NULL,5),(6,119,'罗文波',2157,'2018-08-06 04:25:40',NULL,'待接单',NULL,'2018-08-06 04:26:13',6),(7,119,'罗文波',2157,'2018-08-06 04:26:13',NULL,'安排中',NULL,NULL,6),(8,95,'何诗明',2578,'2018-10-26 02:35:58',NULL,'待接单',NULL,'2018-10-26 02:36:07',1),(9,95,'何诗明',2578,'2018-10-26 02:36:07',NULL,'安排中',NULL,NULL,1);
/*!40000 ALTER TABLE `t_projects_addr_milepost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:53
