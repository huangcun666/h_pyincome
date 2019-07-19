-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_his
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
  `banjie_typle` tinyint(4) DEFAULT NULL,
  `give_up_reason` varchar(255) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage_milepost`
--

LOCK TABLES `business_develop_manage_milepost` WRITE;
/*!40000 ALTER TABLE `business_develop_manage_milepost` DISABLE KEYS */;
INSERT INTO `business_develop_manage_milepost` VALUES (10,11,'陈小奋',145,'2019-03-04 16:01:18','冉小凤',107,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(11,12,'陈小奋',145,'2019-03-05 11:07:44','冉小凤',107,'2019-03-05 11:08:45','2019-03-05 11:23:14','2019-03-05 11:23:49','陈太智',116,2,NULL,NULL,NULL),(12,13,'陈小奋',145,'2019-04-16 13:57:07','陈太智',116,'2019-04-16 14:26:45',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(13,14,'陈小奋',145,'2019-04-16 14:06:44','冉小凤',107,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(14,15,'陈太智',116,'2019-04-30 14:54:32','陈太智',116,'2019-04-30 14:54:49',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(15,16,'陈太智',116,'2019-05-06 11:14:10','仝春梅',143,'2019-05-06 11:24:42',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(16,17,'陈太智',116,'2019-05-06 11:16:48','梁羽祺',435,'2019-05-06 11:17:15',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(17,18,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(18,19,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(19,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(20,21,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL);
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

-- Dump completed on 2019-07-19 17:07:33
