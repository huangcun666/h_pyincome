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
-- Table structure for table `t_projects_transition`
--

DROP TABLE IF EXISTS `t_projects_transition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_transition` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `remark` varchar(2505) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `guid` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `tran_by` varchar(255) DEFAULT NULL,
  `rec_by` varchar(255) DEFAULT NULL,
  `tran_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(255) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_transition`
--

LOCK TABLES `t_projects_transition` WRITE;
/*!40000 ALTER TABLE `t_projects_transition` DISABLE KEYS */;
INSERT INTO `t_projects_transition` VALUES (5,'232',NULL,NULL,'2018-05-24 02:50:00','2','4','2018-05-01 00:00:00',97,'庄培润',413),(13,'',NULL,NULL,'2018-05-24 03:43:29','','','2018-05-25 00:00:00',97,'庄培润',413),(15,'','/static/customer/415/b8387db8-3e6f-4763-a185-396ba6904e83_415.png',NULL,'2018-05-24 03:50:57','23','24','2018-05-02 00:00:00',97,'庄培润',415),(17,'',NULL,NULL,'2018-05-24 03:54:46','13','3','2018-05-17 00:00:00',97,'庄培润',415),(18,'',NULL,NULL,'2018-05-24 05:55:46','3','3','2018-05-23 00:00:00',97,'庄培润',415),(19,'',NULL,NULL,'2018-05-24 05:57:49','32','32','2018-05-15 00:00:00',97,'庄培润',415),(20,'111','/static/customer/418/a095853e-c082-4d3c-99b4-c8fece6c4a1e_418.jpg',NULL,'2018-05-24 08:08:43','11','111','2018-05-24 16:26:01',95,'何诗明',418),(21,'1111','/static/customer/412/ccc2ee6d-f6d3-40ab-a251-7eb9d17aac3c_412.jpg',NULL,'2018-05-24 08:23:29','1','1','2018-05-01 00:00:00',95,'何诗明',412),(22,'','/static/customer/412/fbbbd0b5-da20-415e-b68a-3615e0b5de70_412.png',NULL,'2018-05-25 09:15:29','12','323','2018-05-08 00:00:00',95,'何诗明',412);
/*!40000 ALTER TABLE `t_projects_transition` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:28
