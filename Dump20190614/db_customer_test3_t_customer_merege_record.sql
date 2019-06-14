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
-- Table structure for table `t_customer_merege_record`
--

DROP TABLE IF EXISTS `t_customer_merege_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_merege_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(255) DEFAULT NULL,
  `reg_addr` varchar(1000) DEFAULT NULL,
  `reg_tel` varchar(200) DEFAULT NULL,
  `reg_number` varchar(100) DEFAULT NULL,
  `reg_person` varchar(100) DEFAULT NULL,
  `reg_bank` varchar(200) DEFAULT NULL,
  `reg_bank_account` varchar(200) DEFAULT NULL,
  `addr_type` varchar(200) DEFAULT NULL,
  `addr_expire` datetime DEFAULT NULL,
  `addr_cp` varchar(255) DEFAULT NULL,
  `acc_uid` int(11) DEFAULT NULL,
  `acc_uid_name` varchar(255) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `guid` varchar(45) DEFAULT NULL,
  `remark` varchar(3000) DEFAULT NULL,
  `reg_date` datetime DEFAULT NULL,
  `end_date` datetime DEFAULT NULL,
  `saic` varchar(450) DEFAULT NULL,
  `national_tax` varchar(450) DEFAULT NULL,
  `land_tax` varchar(450) DEFAULT NULL,
  `company_reguid` varchar(255) DEFAULT NULL,
  `industry_name` varchar(255) DEFAULT NULL,
  `is_general` tinyint(4) NOT NULL DEFAULT '0',
  `credit_rating` int(11) DEFAULT NULL,
  `customer_rating` int(11) DEFAULT NULL,
  `credit_rating_name` varchar(255) DEFAULT NULL,
  `customer_rating_name` varchar(45) DEFAULT NULL,
  `updated_at_name` varchar(45) DEFAULT NULL,
  `customer_type` varchar(450) DEFAULT NULL,
  `customer_type_name` varchar(450) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(255) DEFAULT NULL,
  `acc_uid_at` datetime DEFAULT NULL,
  `customer_tag` varchar(1000) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `zone` varchar(255) DEFAULT NULL,
  `is_close` tinyint(4) NOT NULL DEFAULT '0',
  `is_fever` int(11) NOT NULL DEFAULT '0',
  `is_acc_rec` tinyint(4) NOT NULL DEFAULT '0',
  `acc_confirm_at` datetime DEFAULT NULL,
  `acc_confirm_uid` int(11) NOT NULL DEFAULT '0',
  `manager_confirm_uid` int(11) NOT NULL DEFAULT '0',
  `manager_confirm_at` datetime DEFAULT NULL,
  `manager_confirm_name` varchar(255) NOT NULL DEFAULT '0',
  `acc_confirm_uid_name` varchar(255) NOT NULL DEFAULT '0',
  `promo_id` int(11) NOT NULL DEFAULT '0',
  `promo_id_name` varchar(255) DEFAULT NULL,
  `is_wait` tinyint(4) NOT NULL DEFAULT '0',
  `is_wait_at` datetime DEFAULT NULL,
  `is_wait_uid` int(11) NOT NULL DEFAULT '0',
  `wait_from_type` varchar(255) DEFAULT NULL,
  `paytype_id` int(11) NOT NULL DEFAULT '0',
  `paytype_id_name` varchar(255) DEFAULT NULL,
  `fee` int(11) NOT NULL DEFAULT '0',
  `service_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `service_amount_month` decimal(18,2) NOT NULL DEFAULT '0.00',
  `book_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `paytype_status_id` int(11) NOT NULL DEFAULT '0',
  `paytype_status_id_name` varchar(255) DEFAULT '',
  `project_id` int(11) DEFAULT NULL,
  `pay_project_id` int(11) NOT NULL DEFAULT '0',
  `free_book` tinyint(4) NOT NULL DEFAULT '0',
  `last_cuikuan_at` datetime DEFAULT NULL,
  `last_cuikuan_msg` varchar(255) DEFAULT NULL,
  `loupan_name` varchar(45) DEFAULT NULL,
  `loupan_id` int(11) DEFAULT NULL,
  `company_reguid_new` varchar(255) DEFAULT NULL,
  `is_get` int(11) NOT NULL DEFAULT '0',
  `is_get_at` datetime DEFAULT NULL,
  `tyc_name` varchar(255) DEFAULT NULL,
  `sale_last_cuikuan_at` datetime DEFAULT NULL,
  `sale_last_cuikuan_msg` varchar(255) DEFAULT NULL,
  `income_year` int(11) NOT NULL DEFAULT '0',
  `income_amount` decimal(18,2) NOT NULL DEFAULT '0.00',
  `acc_type` varchar(255) DEFAULT '',
  `acc_type_name` varchar(255) DEFAULT '',
  `updated_uid` int(11) DEFAULT NULL,
  `updated_uid_name` varchar(255) DEFAULT '',
  `is_building` tinyint(4) NOT NULL DEFAULT '0',
  `is_clearly` tinyint(4) NOT NULL DEFAULT '0',
  `is_year` tinyint(4) NOT NULL DEFAULT '0',
  `tag_parent_id` int(11) NOT NULL DEFAULT '0',
  `tag_id` int(11) NOT NULL DEFAULT '0',
  `tag_parent_id_name` varchar(255) DEFAULT NULL,
  `tag_id_name` varchar(255) DEFAULT NULL,
  `be_merege_id` int(11) DEFAULT '0',
  `be_merege_company` varchar(45) DEFAULT '',
  `merege_id` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4720 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_merege_record`
--

LOCK TABLES `t_customer_merege_record` WRITE;
/*!40000 ALTER TABLE `t_customer_merege_record` DISABLE KEYS */;
INSERT INTO `t_customer_merege_record` VALUES (4045,'广州澄宇贸易有限公司','','','','','中国工商银行广州越秀桥支行','3602064909200188371','虚拟地址',NULL,'',253,'陈静','2018-08-20 01:21:14','2019-02-13 09:40:16','63e56dd4-8de8-43be-a207-3b2e9fcc8f7c','','2018-08-27 00:00:00',NULL,'广州市天河区工商行政管理局','天河区税务局石牌税务所','','91440101MA5CBBQK6N','',0,0,0,'','',NULL,'19,20,44,45','记账,楼盘,汇算清缴,工商年检',405,'古沛怡','2019-02-13 09:40:16',NULL,'','',0,0,0,'2018-09-07 08:03:58',195,0,NULL,'0','杨婵',0,'',0,NULL,0,NULL,0,'',0,0.00,0.00,0.00,0,'0',NULL,0,0,NULL,NULL,NULL,NULL,'91440101MA5CBBQK6N',5,'2018-12-18 05:51:31','广州澄宇贸易有限公司',NULL,NULL,0,0.00,'','',NULL,'',1,1,1,1,1,'记账','非逾期',0,'',4719),(4719,'广州誉天科技有限公司','','','','','','','',NULL,'',474,'非记账','2018-11-23 18:31:58','2018-11-23 18:31:58','4868069f-3f5f-4c79-9ebe-c369d434e946','',NULL,NULL,'','','','000000000000004719','',0,0,0,'','',NULL,'19,20,44,45','记账,楼盘,汇算清缴,工商年检',98,'吴蔚亮','2018-11-23 18:31:58',NULL,'0','0',0,0,0,NULL,0,0,NULL,'0','0',0,'',0,NULL,0,NULL,47,'年付',12,2600.00,216.67,0.00,52,'正常',0,0,0,NULL,NULL,'世博汇',135,'91440101304755963W',9,'2018-12-19 02:02:31','广州誉天信息科技有限公司',NULL,NULL,0,0.00,'','',NULL,'',1,1,1,1,1,'记账','非逾期',0,'',4719);
/*!40000 ALTER TABLE `t_customer_merege_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:07:14
