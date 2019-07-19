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
-- Table structure for table `t_addr_cb_manager`
--

DROP TABLE IF EXISTS `t_addr_cb_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_cb_manager` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(45) DEFAULT NULL,
  `company_uid` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `rent_by` varchar(245) DEFAULT NULL,
  `addr_type` varchar(245) DEFAULT NULL,
  `addr_con` varchar(255) DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) NOT NULL,
  `uid_at` datetime DEFAULT NULL,
  `uid_remark` varchar(1000) DEFAULT NULL,
  `rent_start` datetime DEFAULT NULL,
  `rent_end` datetime DEFAULT NULL,
  `addr_manager` varchar(255) DEFAULT NULL,
  `old_addr` varchar(1050) DEFAULT NULL,
  `now_addr` varchar(1050) DEFAULT NULL,
  `customer_tel` varchar(255) DEFAULT NULL,
  `chuna_uid` int(11) NOT NULL DEFAULT '0',
  `chuna_uid_name` varchar(255) DEFAULT NULL,
  `chuna_uid_at` datetime DEFAULT NULL,
  `chuna_remark` varchar(1000) DEFAULT NULL,
  `yinfu_uid` int(11) NOT NULL DEFAULT '0',
  `yinfu_uid_name` varchar(255) DEFAULT NULL,
  `yinfu_uid_at` datetime DEFAULT NULL,
  `yinfu_remark` varchar(1000) DEFAULT NULL,
  `last_uid` int(11) NOT NULL DEFAULT '0',
  `last_uid_name` varchar(255) DEFAULT NULL,
  `last_uid_at` datetime DEFAULT NULL,
  `last_remark` varchar(1000) DEFAULT NULL,
  `addr_arr` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_cb_manager`
--

LOCK TABLES `t_addr_cb_manager` WRITE;
/*!40000 ALTER TABLE `t_addr_cb_manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_addr_cb_manager` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:38
