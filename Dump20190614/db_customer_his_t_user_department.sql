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
-- Table structure for table `t_user_department`
--

DROP TABLE IF EXISTS `t_user_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user_department` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `parent_id` int(11) NOT NULL DEFAULT '0',
  `parent_name` varchar(255) DEFAULT NULL,
  `leader_id` int(11) NOT NULL DEFAULT '0',
  `leader_name` varchar(255) DEFAULT NULL,
  `is_used` int(11) NOT NULL DEFAULT '0',
  `order_int` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user_department`
--

LOCK TABLES `t_user_department` WRITE;
/*!40000 ALTER TABLE `t_user_department` DISABLE KEYS */;
INSERT INTO `t_user_department` VALUES (11,'会计部',0,NULL,0,NULL,0,0),(12,'会计一部',11,'会计部',0,'',0,0),(13,'会计二部',11,'会计部',173,'陈雨薇',0,0),(14,'会计三部',11,'会计部',0,NULL,0,0),(15,'会计四部',11,'会计部',0,NULL,0,0),(16,'会计五部',11,'会计部',0,NULL,0,0),(17,'销售部',0,NULL,0,NULL,0,0),(18,'工商部',0,NULL,0,NULL,0,0),(19,'注销部',0,NULL,0,NULL,0,0),(20,'人事行政部',0,NULL,0,NULL,0,0),(21,'市场技术部',0,NULL,0,NULL,0,0),(22,'总经办',0,NULL,0,NULL,0,0),(23,'注销部',0,NULL,0,NULL,0,0),(24,'财务部',0,NULL,0,NULL,0,0),(25,'外联部',0,NULL,0,NULL,0,0);
/*!40000 ALTER TABLE `t_user_department` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:07:04
