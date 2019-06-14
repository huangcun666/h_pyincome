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
-- Table structure for table `t_cb_addr_manage`
--

DROP TABLE IF EXISTS `t_cb_addr_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_cb_addr_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sale_addr` varchar(255) DEFAULT NULL,
  `arrange_date` datetime DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `legal_peson` varchar(45) DEFAULT NULL,
  `purchaser` varchar(45) DEFAULT NULL,
  `cost_price` decimal(18,2) DEFAULT '0.00',
  `sell_price` decimal(18,2) DEFAULT '0.00',
  `purchaser_pay_money` decimal(18,2) DEFAULT '0.00',
  `purchaser_pay_date` datetime DEFAULT NULL,
  `chuna_check_name` varchar(45) DEFAULT NULL,
  `chuna_check_id` int(11) DEFAULT NULL,
  `chuna_check_date` datetime DEFAULT NULL,
  `supply_js_money` decimal(18,2) DEFAULT '0.00',
  `supply_js_date` datetime DEFAULT NULL,
  `cawu_js_id` int(11) DEFAULT NULL,
  `caiwu_js_name` varchar(45) DEFAULT NULL,
  `caiwu_js_date` datetime DEFAULT NULL,
  `supplier` varchar(45) DEFAULT NULL,
  `addr_xingzhi` varchar(255) DEFAULT NULL,
  `addr_type` varchar(45) DEFAULT NULL,
  `rent_date` datetime DEFAULT NULL,
  `expire_date` datetime DEFAULT NULL,
  `uid` int(11) NOT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `purchaser_qk` int(11) DEFAULT '0',
  `supply_qk` varchar(45) DEFAULT '0',
  `fq_date` datetime DEFAULT NULL,
  `purchaser_caiwu_confirm` datetime DEFAULT NULL,
  `supply_caiwu_confirm` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_cb_addr_manage`
--

LOCK TABLES `t_cb_addr_manage` WRITE;
/*!40000 ALTER TABLE `t_cb_addr_manage` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_cb_addr_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:07:08
