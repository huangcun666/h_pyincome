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
-- Table structure for table `t_customer_other_data`
--

DROP TABLE IF EXISTS `t_customer_other_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_other_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hangye` varchar(255) DEFAULT NULL,
  `zg_name` varchar(45) DEFAULT NULL,
  `zg_tel` varchar(45) DEFAULT NULL,
  `business_scope` varchar(255) DEFAULT NULL,
  `attention` varchar(255) DEFAULT NULL,
  `zg_option` varchar(255) DEFAULT NULL,
  `survey` varchar(255) DEFAULT NULL,
  `shuizhong_detail` varchar(255) DEFAULT NULL,
  `zhengshou_way` varchar(255) DEFAULT NULL,
  `shuikong_type` varchar(255) DEFAULT NULL,
  `fixed_assets` varchar(45) DEFAULT NULL,
  `legal_id_card` varchar(255) DEFAULT NULL,
  `rel_name_collect_account` varchar(255) DEFAULT NULL,
  `rel_name_collect_password` varchar(255) DEFAULT NULL,
  `shuipan_password` varchar(255) DEFAULT NULL,
  `shuipan_command` varchar(255) DEFAULT NULL,
  `per_income_apply_password` varchar(255) DEFAULT NULL,
  `receipt_card_password` varchar(255) DEFAULT NULL,
  `accumulation_fund_password` varchar(255) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `update_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_other_data`
--

LOCK TABLES `t_customer_other_data` WRITE;
/*!40000 ALTER TABLE `t_customer_other_data` DISABLE KEYS */;
INSERT INTO `t_customer_other_data` VALUES (1,'','','','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,4344,'2019-03-25 11:39:32'),(2,'','1','2','3','4','5',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,5157,'2019-03-29 14:58:49'),(3,'1','6','7','112','23','ddf',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,5156,'2019-03-25 11:52:06'),(4,'','','','','','','1','2','3','4','7','1231243245','23','f','sdf','3','32','23','d',4072,'2019-03-25 15:24:05'),(5,'','','','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,5151,'2019-03-26 15:13:29'),(6,'','','','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1163,'2019-03-29 17:27:28'),(7,'','','','','','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1163,'2019-03-29 17:27:29'),(8,'1','5','','','','','12','34','','565','',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,5159,'2019-03-29 17:32:31');
/*!40000 ALTER TABLE `t_customer_other_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:07
