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
-- Table structure for table `t_projects_economic_census`
--

DROP TABLE IF EXISTS `t_projects_economic_census`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_economic_census` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jiedan_name` varchar(45) DEFAULT NULL,
  `jiedan_id` int(11) DEFAULT NULL,
  `jiedan_at` datetime DEFAULT NULL,
  `banjie_at` datetime DEFAULT NULL,
  `file_path` varchar(255) DEFAULT '',
  `banjie_remark` varchar(255) DEFAULT NULL,
  `kj_check_at` datetime DEFAULT NULL,
  `kj_check_name` varchar(45) DEFAULT NULL,
  `kj_check_id` int(11) DEFAULT NULL,
  `kj_check_status` tinyint(4) DEFAULT '0',
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_economic_census`
--

LOCK TABLES `t_projects_economic_census` WRITE;
/*!40000 ALTER TABLE `t_projects_economic_census` DISABLE KEYS */;
INSERT INTO `t_projects_economic_census` VALUES (8,'李洁韩',176,'2019-03-15 17:15:03','2019-03-18 15:32:15','/static/economic_census/8506/2019-01-02 09-13-19 的屏幕截图.png|/static/economic_census/8506/2018-12-05 15-01-58 的屏幕截图.png|/static/economic_census/8506/2019-01-02 09-13-19 的屏幕截图.png|','','2019-03-18 15:43:30','陈太智',116,1,8506),(9,'李洁韩',176,'2019-03-15 17:15:51',NULL,'','',NULL,NULL,NULL,0,8496),(10,'李洁韩',176,'2019-03-15 17:16:57',NULL,'','',NULL,NULL,NULL,0,8504),(11,'李洁韩',176,'2019-03-15 17:20:35',NULL,'','',NULL,NULL,NULL,0,8501),(12,'钟华秀',184,'2019-03-20 14:16:10',NULL,'',NULL,NULL,NULL,NULL,0,8509);
/*!40000 ALTER TABLE `t_projects_economic_census` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:23
