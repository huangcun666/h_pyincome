-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test3
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
-- Table structure for table `t_customer_payment_merege_record`
--

DROP TABLE IF EXISTS `t_customer_payment_merege_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_payment_merege_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL DEFAULT '0',
  `pay_typeid` int(11) NOT NULL DEFAULT '0',
  `pay_typeid_name` varchar(255) DEFAULT NULL,
  `service_month_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `service_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `book_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `acc_end` datetime DEFAULT NULL,
  `acc_book_end` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  `remark` varchar(4000) DEFAULT NULL,
  `fee` decimal(18,2) NOT NULL DEFAULT '0.00',
  `pb_remark` varchar(4000) DEFAULT NULL,
  `al_remark` varchar(4000) DEFAULT NULL,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `income_id` int(11) NOT NULL DEFAULT '0',
  `req_uid` int(11) NOT NULL DEFAULT '0',
  `req_uid_name` varchar(255) DEFAULT NULL,
  `req_at` datetime DEFAULT NULL,
  `payment_confirm_uid` int(11) NOT NULL DEFAULT '0',
  `payment_confirm_at` datetime DEFAULT NULL,
  `payment_confirm_uid_name` varchar(255) DEFAULT NULL,
  `payment_confirm_state` int(11) NOT NULL DEFAULT '0',
  `payment_confirm_remark` varchar(2550) DEFAULT NULL,
  `cp_title_id` int(11) NOT NULL DEFAULT '0',
  `wait_pay_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `req_close` int(11) NOT NULL DEFAULT '0',
  `pfi_confirm_state` int(11) NOT NULL DEFAULT '0',
  `pfi_confirm_uid` int(11) NOT NULL DEFAULT '0',
  `pfi_confirm_uid_name` varchar(255) DEFAULT NULL,
  `pfi_confirm_at` datetime DEFAULT NULL,
  `pfi_confirm_remark` varchar(2550) DEFAULT NULL,
  `pay_handler_at` datetime DEFAULT NULL,
  `updated_uid` int(11) NOT NULL DEFAULT '0',
  `sale_man` varchar(45) DEFAULT NULL,
  `kf_man` varchar(45) DEFAULT NULL,
  `sale_id` int(11) DEFAULT NULL,
  `kf_id` int(11) DEFAULT NULL,
  `faqi_again` tinyint(4) DEFAULT '0',
  `merege_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_payment_merege_record`
--

LOCK TABLES `t_customer_payment_merege_record` WRITE;
/*!40000 ALTER TABLE `t_customer_payment_merege_record` DISABLE KEYS */;
/*!40000 ALTER TABLE `t_customer_payment_merege_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:07:12
