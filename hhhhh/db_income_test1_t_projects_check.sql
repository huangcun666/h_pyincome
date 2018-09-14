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
-- Table structure for table `t_projects_check`
--

DROP TABLE IF EXISTS `t_projects_check`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kf_created_at` datetime DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `kf_uid` int(11) DEFAULT NULL,
  `kf_uid_name` varchar(45) DEFAULT NULL,
  `remark` varchar(500) DEFAULT NULL,
  `kf_check_status` tinyint(4) DEFAULT NULL,
  `sh_uid_name` varchar(45) DEFAULT NULL,
  `sh_uid` int(11) DEFAULT NULL,
  `sh_created_at` datetime DEFAULT NULL,
  `sh_remark` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_check`
--

LOCK TABLES `t_projects_check` WRITE;
/*!40000 ALTER TABLE `t_projects_check` DISABLE KEYS */;
INSERT INTO `t_projects_check` VALUES (47,'2018-09-07 08:28:09',2084,100,'甘雪莲','',0,'陈太智',116,'2018-09-07 09:03:24','0'),(48,'2018-09-07 08:40:41',1476,100,'甘雪莲','123',1,'陈太智',116,'2018-09-07 09:01:18','1'),(49,'2018-09-07 09:06:16',379,100,'甘雪莲','',1,'陈太智',116,'2018-09-11 02:30:26',''),(50,'2018-09-07 09:35:04',849,100,'甘雪莲','',0,'陈太智',116,'2018-09-11 02:26:16','6666');
/*!40000 ALTER TABLE `t_projects_check` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-14 11:34:27
