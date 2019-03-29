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
-- Table structure for table `business_develop_manage_milepost`
--

DROP TABLE IF EXISTS `business_develop_manage_milepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_manage_milepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business_id` int(11) DEFAULT NULL,
  `assigner_name` varchar(45) DEFAULT NULL,
  `assigner_id` int(11) DEFAULT NULL,
  `assigner_at` datetime DEFAULT NULL,
  `jiedan_name` varchar(45) DEFAULT NULL,
  `jiedan_id` int(11) DEFAULT NULL,
  `jiedan_at` datetime DEFAULT NULL,
  `banjie_at` datetime DEFAULT NULL,
  `checked_at` datetime DEFAULT NULL,
  `checked_name` varchar(45) DEFAULT NULL,
  `checked_id` int(11) DEFAULT NULL,
  `checked_status` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage_milepost`
--

LOCK TABLES `business_develop_manage_milepost` WRITE;
/*!40000 ALTER TABLE `business_develop_manage_milepost` DISABLE KEYS */;
INSERT INTO `business_develop_manage_milepost` VALUES (1,1,'陈太智',116,'2019-02-28 13:58:43','庄培润',97,NULL,NULL,NULL,NULL,NULL,0),(2,2,'陈太智',116,'2019-02-28 13:59:07','庄培润',97,'2019-02-28 14:06:57','2019-02-28 14:11:02','2019-02-28 14:30:56','陈太智',116,1),(3,3,'陈太智',116,'2019-02-28 13:58:08','庄培润',97,NULL,NULL,NULL,NULL,NULL,0),(4,4,'陈太智',116,'2019-02-28 13:57:11','庄培润',97,NULL,NULL,NULL,NULL,NULL,0),(5,5,'陈太智',116,'2019-02-28 11:54:22','庄培润',97,'2019-02-28 15:54:48',NULL,NULL,NULL,NULL,0);
/*!40000 ALTER TABLE `business_develop_manage_milepost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:13
