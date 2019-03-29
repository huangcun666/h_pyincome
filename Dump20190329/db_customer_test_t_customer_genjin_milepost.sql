-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test
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
-- Table structure for table `t_customer_genjin_milepost`
--

DROP TABLE IF EXISTS `t_customer_genjin_milepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_genjin_milepost` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `genjin_state_id` int(11) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_genjin_milepost`
--

LOCK TABLES `t_customer_genjin_milepost` WRITE;
/*!40000 ALTER TABLE `t_customer_genjin_milepost` DISABLE KEYS */;
INSERT INTO `t_customer_genjin_milepost` VALUES (1,5102,1,164,'张会会','2019-03-26 14:22:00'),(2,5157,1,116,'陈太智','2019-03-26 14:50:57'),(3,5155,1,116,'陈太智','2019-03-26 14:51:47'),(4,5155,2,116,'陈太智','2019-03-26 14:55:00'),(5,5157,2,116,'陈太智','2019-03-26 16:44:57'),(6,5102,2,164,'张会会','2019-03-26 17:15:50'),(7,5102,3,164,'张会会','2019-03-26 17:18:27'),(8,5129,1,153,'江嘉琳','2019-03-27 17:34:15'),(9,5129,2,153,'江嘉琳','2019-03-27 17:41:33'),(10,5129,3,153,'江嘉琳','2019-03-27 17:41:55'),(12,5129,4,116,'陈太智','2019-03-28 14:02:38'),(13,5129,5,116,'陈太智','2019-03-28 14:02:38'),(14,5129,6,116,'陈太智','2019-03-28 14:02:48'),(15,5129,7,116,'陈太智','2019-03-28 14:05:36'),(16,5156,1,116,'陈太智','2019-03-28 14:11:34'),(17,5156,2,116,'陈太智','2019-03-28 14:11:38'),(18,5156,3,116,'陈太智','2019-03-28 14:11:38'),(19,5156,4,116,'陈太智','2019-03-28 14:11:41'),(20,5156,5,116,'陈太智','2019-03-28 14:11:41'),(21,5156,6,116,'陈太智','2019-03-28 14:11:41'),(22,5156,7,116,'陈太智','2019-03-28 14:11:41'),(23,5154,1,116,'陈太智','2019-03-28 14:31:42'),(24,5154,2,116,'陈太智','2019-03-28 15:33:16');
/*!40000 ALTER TABLE `t_customer_genjin_milepost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:10
