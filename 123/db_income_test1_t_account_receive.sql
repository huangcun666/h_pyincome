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
-- Table structure for table `t_account_receive`
--

DROP TABLE IF EXISTS `t_account_receive`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_account_receive` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `company` varchar(45) DEFAULT NULL,
  `kf_kuaiji` varchar(45) DEFAULT NULL,
  `sale_guwen` varchar(45) DEFAULT NULL,
  `kf_guwen` varchar(45) DEFAULT NULL,
  `jiesuan_cycle` varchar(45) DEFAULT NULL,
  `year_charge` int(11) DEFAULT NULL,
  `month_charge` int(11) DEFAULT NULL,
  `zhangce_charge` int(11) DEFAULT NULL,
  `chengli_date` datetime DEFAULT NULL,
  `account_charge_end_date` datetime DEFAULT NULL,
  `zhangce_charge_end_date` datetime DEFAULT NULL,
  `new_yishou_detail` varchar(500) DEFAULT NULL,
  `yingshou_detail` varchar(500) DEFAULT NULL,
  `last_updated_msg` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `last_updated` datetime DEFAULT NULL,
  `guid` varchar(45) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `is_loupan` tinyint(1) DEFAULT NULL,
  `register_addr_type` varchar(45) DEFAULT NULL,
  `kp_addr_date_start` datetime DEFAULT NULL,
  `kp_addr_date_end` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_account_receive`
--

LOCK TABLES `t_account_receive` WRITE;
/*!40000 ALTER TABLE `t_account_receive` DISABLE KEYS */;
INSERT INTO `t_account_receive` VALUES (3,'大吉大利','刘建光','张金芳','','半年付',1,2,3,'2018-08-09 00:00:00','2018-08-09 00:00:00','2018-08-16 00:00:00','4','5','6666666','2018-08-31 14:09:40','2018-08-31 17:21:45','3e312e97-eacb-49c7-8fd8-b3a3878848d5',NULL,NULL,NULL,NULL,NULL,NULL),(4,'广州发业测试1','财务11','财务11','财务11','年付',0,0,0,'2018-08-01 00:00:00',NULL,NULL,'','','777','2018-08-31 17:44:15','2018-09-03 09:41:39','efee3792-fc83-484c-97c8-bbc44965115f','冯恒敏',118,NULL,NULL,NULL,NULL),(5,'发业测','','','','年付',100,1000,1111,'2018-09-05 00:00:00','2018-09-04 00:00:00','2018-09-05 00:00:00','萨达','的撒','发发','2018-09-03 09:38:15','2018-09-03 09:48:26','c30f9d1c-36eb-4ab4-84ad-72fd9bfa507c','庄培润',97,NULL,NULL,NULL,NULL),(6,'广州发业测试有限公司','','','','年付',1,1,1,'2018-09-06 00:00:00',NULL,NULL,NULL,'',NULL,'2018-09-03 10:12:23',NULL,'a64620eb-c7a7-4ec4-aab4-26ebbcf6837f','庄培润',97,NULL,NULL,NULL,NULL),(7,'广州发业测试有限公司','dsafsd','fds','fdsfd','年付',1,11,11,'2018-09-06 00:00:00',NULL,NULL,'2019.03-2019.08记账费1360+2019.03-2019.08账册费费150','',NULL,'2018-09-03 10:14:06',NULL,'2345b445-bc23-49bf-b828-2d3fc5bfebb2','庄培润',97,1,'dfsfds','2018-09-07 00:00:00','2018-09-07 00:00:00'),(8,'广州发业测试有限公司1','','','','年付',11,11,11,'2018-09-06 00:00:00',NULL,NULL,NULL,'',NULL,'2018-09-03 10:14:31',NULL,'67fe806b-bf67-4bea-bc01-66f16da8ae4e','庄培润',97,NULL,NULL,NULL,NULL),(11,'发业测','张金芳','财务1','财务1','',0,0,0,'2018-09-05 00:00:00',NULL,NULL,'','',NULL,'2018-09-05 09:35:51',NULL,'7bf94182-1748-4114-a87b-73e4e0becbec','陈太智',116,1,NULL,NULL,NULL),(12,'1','财务1','财务1','财务1','年付',111,11,1111,'2018-09-06 00:00:00','2018-09-05 00:00:00','2018-09-06 00:00:00','11','111','水大的','2018-09-05 09:37:16','2018-09-05 09:54:55','50f2d924-5f55-499f-99a0-805614b3ba11','陈太智',116,0,NULL,NULL,NULL),(13,'广州发业测试','1111','1111111111','11111111111','半年付',1112,222111,3333,'2018-09-15 00:00:00',NULL,NULL,'','',NULL,'2018-09-05 11:45:29',NULL,'969d2e0f-1e42-4f70-b294-2262868f1c52','赵松筑',121,1,'123','2018-09-07 00:00:00','2018-09-08 00:00:00'),(14,'广州发业测试有限公司','财务1','','','',0,0,0,'2018-09-06 00:00:00',NULL,NULL,'','',NULL,'2018-09-05 15:26:12',NULL,'d3f1cb8c-d148-46c3-8dda-d4deef47ffb1','江嘉琳',153,1,'',NULL,NULL);
/*!40000 ALTER TABLE `t_account_receive` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:22:57
