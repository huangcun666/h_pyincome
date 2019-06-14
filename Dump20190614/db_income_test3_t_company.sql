-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test3
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
-- Table structure for table `t_company`
--

DROP TABLE IF EXISTS `t_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_company` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `company_name` varchar(255) NOT NULL DEFAULT '',
  `company_code` varchar(255) NOT NULL DEFAULT '',
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(100) DEFAULT NULL,
  `updated_uid` int(11) DEFAULT NULL,
  `updated_uid_name` varchar(100) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_company`
--

LOCK TABLES `t_company` WRITE;
/*!40000 ALTER TABLE `t_company` DISABLE KEYS */;
INSERT INTO `t_company` VALUES (1,'广州恒丰远耀贸易有限公司','','2018-07-03 01:06:31',116,'8',NULL,NULL,NULL),(2,'广州市景悦科技有限公司','','2018-07-03 01:23:20',106,'9',NULL,NULL,NULL),(3,'广州杰睿硕科技有限公司','91440101MA5AXNX40N','2018-07-03 02:05:41',155,'11',NULL,NULL,NULL),(4,'广州空谷营销策划有限公司','91440106MA59CA8320','2018-07-03 07:59:54',155,'11',NULL,NULL,NULL),(5,'广州拜康生物科技有限公司','','2018-07-04 01:13:09',153,'11',NULL,NULL,NULL),(6,'广州泰因美生物科技有限公司','','2018-07-16 07:17:21',194,'10',NULL,NULL,NULL),(7,'安顺集团建设有限公司广州分公司','','2018-07-17 02:23:14',239,'9',NULL,NULL,NULL),(8,'广州金柏利贸易有限公司','91440101MA5AULC960','2018-07-19 02:30:33',203,'10',NULL,NULL,NULL),(9,'广州蓝之林科技有限公司','91440101MA5B6TNG58','2018-07-22 02:19:06',121,'1',NULL,NULL,NULL),(10,'广州君宁科技有限公司','','2018-07-23 01:33:12',192,'10',NULL,NULL,NULL),(11,'广州浦尔纳电子科技有限公司','91440106MA59C81M8Y','2018-07-23 01:55:10',97,'1',NULL,NULL,NULL),(12,'广州云帮信息科技有限公司','91440101MA5B700H32','2018-07-23 05:37:30',151,'1',NULL,NULL,NULL),(13,'向明理德(广州)资产管理有限公司','','2018-07-25 02:46:13',192,'10',NULL,NULL,NULL),(14,'格律诗(广州)电子商务有限公司','91440101MA5BUNK0XN','2018-08-01 08:26:09',268,'9',NULL,NULL,NULL),(15,'千玺比萨(广州)餐饮管理有限公司','','2018-08-03 03:15:05',338,'9',NULL,NULL,NULL),(16,'广州华科信息技术有限公司','','2018-08-03 08:30:20',191,'10',NULL,NULL,NULL),(17,'广州华科信息科技有限公司','','2018-08-03 08:42:58',191,'10',NULL,NULL,NULL),(18,'广州市生泰装饰工程有限公司','91440101MA5AQH6G2U','2018-08-06 05:51:16',338,'9',NULL,NULL,NULL),(19,'广州市珍房房地产咨询有限公司','914401050721086433','2018-08-08 09:03:46',141,'9',NULL,NULL,NULL),(20,'广州猛伍人力资源管理有限公司','91440104MA59DJYE8F','2018-08-09 09:20:15',239,'9',NULL,NULL,NULL),(21,'é­åç§æï¼å¹¿å·ï¼æéå¬å¸','91440101MA5AYRLK1K','2018-08-10 07:35:16',123,'1',NULL,NULL,NULL),(22,'信和财富投资管理(北京)有限公司广州第十三分公司','91440184MA59BEY76H','2018-08-13 09:39:22',139,'9',NULL,NULL,NULL),(23,'广州龙胜科技有限公司','91440101MA5AX0CE64','2018-08-14 03:04:21',141,'9',NULL,NULL,NULL),(24,'广州市妍真服饰有限公司','91440106331380511F','2018-08-14 06:06:50',138,'9',NULL,NULL,NULL),(25,'广东诚邦企业管理咨询有限公司','91440101MA59FB268R','2018-08-15 03:34:19',140,'9',NULL,NULL,NULL),(26,'广州鑫烨生物科技有限公司','','2018-08-17 03:17:30',141,'9',NULL,NULL,NULL),(27,'广东旺程易购商贸有限公司','91440101MA5C3KH65A','2018-08-20 08:33:24',139,'9',NULL,NULL,NULL),(28,'广州和沐制冷设备有限公司','无','2018-08-21 02:03:36',203,'10',NULL,NULL,NULL),(29,'广州金西科农业发展有限公司','91440101MA5AA7J937','2018-08-27 07:49:43',116,'陈太智',NULL,NULL,NULL),(30,'广州曦默智能环保科技有限公司','91440101MA5AWNDM55','2018-08-29 09:26:11',199,'杨辉',NULL,NULL,NULL),(31,'广州李唐法律咨询服务有限公司','91440101MA5CBF0D4Y','2018-08-30 05:47:39',269,'陶君怡',NULL,NULL,NULL),(32,'广州灏循信息科技服务有限公司','91440101MA59Q1420M','2018-09-03 01:27:03',138,'王坚',NULL,NULL,NULL),(33,'广州小磨信息科技有限公司','91440101MA5CBTK2XC','2018-09-07 08:09:31',268,'李佳欣',NULL,NULL,NULL),(34,'广州锦绣杏林科技有限公司','91440101MA5CC6Q986','2018-09-18 01:32:59',134,'沈楚纯',NULL,NULL,NULL),(35,'御峰陶瓷贸易(广州)有限公司','91440101MA5AYR6R3G','2018-09-20 04:02:35',94,'冯恒冠',NULL,NULL,NULL),(36,'广州市尚尚签服装有限公司','91440101MA5BLPGQ3Y','2018-09-26 06:33:24',180,'黄晓晴',NULL,NULL,NULL),(37,'广州庞业资产管理有限公司','','2018-10-08 02:21:32',194,'彭苏勉',NULL,NULL,NULL),(38,'培立教育咨询(广州)有限公司','','2018-10-23 07:58:17',386,'杨婷',NULL,NULL,NULL),(39,'广州博逸化妆品有限公司','91440101MA5CKWJUXW','2019-01-09 15:03:25',338,'陈莹莹',NULL,NULL,NULL),(40,'广州宝来医疗服务有限公司','','2019-01-16 17:47:45',95,'何诗明',NULL,NULL,NULL),(41,'广州娜慕晗贸易有限公司','','2019-01-17 11:10:28',161,'周萍',NULL,NULL,NULL),(42,'名媛堂文化传播(广州)有限公司','','2019-01-18 13:43:02',381,'陈静玲',NULL,NULL,NULL),(43,'广州市番禺区南村念玉服装加工厂','','2019-01-30 11:15:42',338,'陈莹莹',NULL,NULL,NULL),(44,'广州博雅咨询有限公司','','2019-02-28 11:25:43',386,'杨婷',NULL,NULL,NULL),(45,'广州马卡德贸易有限公司','91440101MA59M69G99','2019-03-11 17:32:02',380,'叶梓英',NULL,NULL,NULL),(46,'宝元堂(广东)生物工程科技有限公司','91440101MA5CKL070E','2019-03-12 09:15:43',161,'周萍',NULL,NULL,NULL),(47,'广州建洁科技开发有限公司','91440101MA5AXG535H','2019-04-01 11:39:24',204,'刘慧敏',NULL,NULL,NULL),(48,'子木源盛(广东)科技有限公司','','2019-04-01 16:37:50',277,'黄巧玲',NULL,NULL,NULL),(49,'广州企信软件科技有限公司','91440101MA59PDU07T','2019-04-18 16:46:16',155,'岑美凤',NULL,NULL,NULL),(50,'广州袋淑箱包有限公司','91440111MA59BQF35M','2019-04-26 09:22:49',97,'庄培润',NULL,NULL,NULL),(51,'广州耐时电池科技有限公司','91440113689312249L','2019-06-12 14:29:27',116,'陈太智',NULL,NULL,NULL);
/*!40000 ALTER TABLE `t_company` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:06:44
