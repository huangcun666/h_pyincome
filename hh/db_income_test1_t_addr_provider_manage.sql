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
-- Table structure for table `t_addr_provider_manage`
--

DROP TABLE IF EXISTS `t_addr_provider_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_provider_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `remark` varchar(100) DEFAULT '',
  `updated_at` datetime DEFAULT NULL,
  `danbao_matter` varchar(500) DEFAULT '',
  `fp_limit` varchar(45) DEFAULT '',
  `type` varchar(45) DEFAULT NULL,
  `addr_nature` varchar(45) DEFAULT NULL,
  `cost_price` varchar(45) DEFAULT NULL,
  `register_price` varchar(45) DEFAULT NULL,
  `same_area_change_price` varchar(45) DEFAULT NULL,
  `dif_area_change_price` varchar(45) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `business_scope_limit` varchar(255) DEFAULT NULL,
  `accept_material` varchar(255) DEFAULT NULL,
  `addr_type` varchar(45) DEFAULT NULL,
  `proivde_end` varchar(45) DEFAULT NULL,
  `is_lock` tinyint(4) NOT NULL DEFAULT '0',
  `is_renew` tinyint(4) NOT NULL DEFAULT '0',
  `order_at` datetime DEFAULT NULL,
  `order_int` int(11) DEFAULT '100',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_provider_manage`
--

LOCK TABLES `t_addr_provider_manage` WRITE;
/*!40000 ALTER TABLE `t_addr_provider_manage` DISABLE KEYS */;
INSERT INTO `t_addr_provider_manage` VALUES (20,'白云','t','2018-10-26 05:53:39',95,'何诗明','',NULL,'','','66666666','','','','','','','','None',NULL,NULL,2,2,'2018-10-26 05:56:42',93),(21,'番禺','6','2018-10-26 05:56:42',95,'何诗明','',NULL,'','','55555555','','','','','','','','',NULL,NULL,2,2,'2018-10-26 05:56:42',96),(22,'海珠','23','2018-10-26 06:05:14',119,'罗文波','',NULL,'','','3333','3333333','','','','','','','',NULL,NULL,2,2,'2018-10-26 05:56:42',95),(23,'越秀','3','2018-10-26 06:16:35',119,'罗文波','',NULL,'','','1111','1111','11111','11111','','','','','',NULL,NULL,2,2,'2018-10-26 05:56:42',94),(24,'天河','1111','2018-10-26 06:29:39',119,'罗文波','',NULL,'55555555555','01010101','2222','3333333','444444444','555555','6666666','7777777','8888888','99999999','10100101',NULL,NULL,1,2,'2018-10-26 05:56:42',99),(25,'越秀','444','2018-10-26 06:38:43',119,'罗文波','',NULL,'4','','44444444','4','4','4','4','4','4','4','4',NULL,NULL,1,1,'2018-10-26 05:56:42',97),(27,'越秀','123','2018-11-08 09:58:28',116,'陈太智','',NULL,'','','1433223','2','','','','','','','',NULL,NULL,2,2,'2018-10-26 05:56:42',100);
/*!40000 ALTER TABLE `t_addr_provider_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:58
