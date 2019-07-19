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
-- Table structure for table `business_develop_manage`
--

DROP TABLE IF EXISTS `business_develop_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business_from_id` int(11) NOT NULL,
  `business_from_name` varchar(45) DEFAULT NULL,
  `customer_name` varchar(45) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `project_request` varchar(255) DEFAULT NULL,
  `source_keyword` varchar(45) DEFAULT NULL,
  `source_way_name` varchar(45) DEFAULT NULL,
  `source_way_id` int(11) DEFAULT '0',
  `source_place_name` varchar(45) DEFAULT NULL,
  `source_place_id` int(11) DEFAULT '0',
  `source_port_name` varchar(45) DEFAULT NULL,
  `source_port_id` int(11) DEFAULT '0',
  `remark` varchar(255) DEFAULT NULL,
  `referrer` varchar(45) DEFAULT NULL,
  `be_referrer_company` varchar(45) DEFAULT NULL,
  `be_referrer_name` varchar(45) DEFAULT NULL,
  `be_referrer_phone` varchar(45) DEFAULT NULL,
  `guid` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `customer_tag` varchar(255) DEFAULT NULL,
  `friend_introduce` tinyint(4) DEFAULT '0',
  `project_id` int(11) DEFAULT NULL,
  `feedback_type_id` int(11) DEFAULT NULL,
  `feedback_type_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage`
--

LOCK TABLES `business_develop_manage` WRITE;
/*!40000 ALTER TABLE `business_develop_manage` DISABLE KEYS */;
INSERT INTO `business_develop_manage` VALUES (11,295,'反馈商机','1','广州发业科技有限公司','1','1','','',0,'',0,'',0,'','1','','1','1','8634a67f-f514-40e7-ad6d-902ef75a2a89','2019-03-04 15:48:54',116,'陈太智',NULL,0,NULL,2,'内部客户办理新公司业务'),(12,294,'推广商机','a','','a','a','a','在线咨询',61,'百度',64,'PC端',281,'','','','','','b9b83992-73cd-4112-87f3-3524071af3cd','2019-03-04 16:24:29',145,'陈小奋','36_咨询注册_咨询（前端）',0,NULL,NULL,NULL),(13,294,'推广商机','cs','c','d','da','da','在线咨询',61,'百度',64,'PC端',281,'','','','','','4e9016ec-a382-4acb-a433-b581f1b47ae7','2019-04-16 13:56:18',145,'陈小奋','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）,44_公司起名_咨询（前端）,87_中质量B2类_质量（业务）,88_低质量C1类_质量（业务）,90_同行_质量（业务）,91_无效业务咨询_质量（业务）,92_没咨询过我司_质量（业务）,58_方案未确定_跟进（业务）,64_意向变弱_跟进（业务）,74_需求商标_需求（业务）,75_需求个体户_需求（业务）,76_需求买卖公司_需求（业务）,77_需求香港公司_需求（业务）,83_需求入户_需求（业务）,84_需求装修_需求（业务）',0,NULL,NULL,NULL),(14,294,'推广商机','dasd','dsad','dasd','dasda','sdas','在线咨询',61,'百度',64,'PC端',281,'','','','','','7e4fc0d7-e946-4249-b414-c1db54927c41','2019-04-16 14:06:01',145,'陈小奋','38_咨询变更_咨询（前端）,39_咨询注销_咨询（前端）',0,NULL,NULL,NULL),(15,295,'反馈商机','广州发业财务咨询有限公司广州分公司','','','','','',0,'',0,'',0,'','','','','','1b64332c-faca-449a-9446-5fc4fd696f00','2019-04-28 14:14:37',116,'陈太智',NULL,1,NULL,1,'内部客户办理自身业务'),(16,295,'反馈商机','121','广州市丽眼饰衣服装有限公司','1111','11','','',0,'',0,'',0,'','111','','','','b6f3e3ac-c314-446c-a9dc-a80c4b56de7f','2019-05-06 11:13:34',116,'陈太智',NULL,0,NULL,1,'内部客户办理原公司业务'),(17,295,'反馈商机','湖广会馆','广州途裕捷投资咨询有限公司','544','5454','','',0,'',0,'',0,'','54','','','','0a8cfbe5-5b0c-4e17-974b-45f54ad03501','2019-05-06 11:16:21',435,'梁羽祺',NULL,0,NULL,1,'内部客户办理原公司业务'),(18,294,'推广商机','','','','变更地址','','在线咨询',61,'百度',64,'PC端',281,'','','','','','be2b62c4-3e96-4eec-b743-d15a7f039cf0','2019-05-06 11:52:19',146,'吴秀珠',NULL,0,NULL,0,''),(19,295,'反馈商机','','广州市丽眼饰衣服装有限公司','','','','',0,'',0,'',0,'','','','','','8b9b7ef4-50db-4199-b3a9-60465d5b37eb','2019-05-07 13:36:30',116,'陈太智',NULL,0,NULL,4,'经理、员工介绍客户办理'),(20,295,'反馈商机','','广州市丽眼饰','','','','',0,'',0,'',0,'','','','','','77aa601a-3f05-4632-bc40-05f1c1a77f0f','2019-05-07 13:37:09',116,'陈太智',NULL,0,NULL,4,'经理、员工介绍客户办理'),(21,295,'反馈商机','','广州市丽眼饰衣服装有限公司','','','','',0,'',0,'',0,'','','','','','3eab2856-f7f3-45c1-933c-b92897cac7e7','2019-05-07 13:37:47',116,'陈太智',NULL,0,NULL,2,'内部客户办理非原公司业务');
/*!40000 ALTER TABLE `business_develop_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:33
