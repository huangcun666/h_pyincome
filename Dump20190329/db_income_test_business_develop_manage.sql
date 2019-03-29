-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage`
--

LOCK TABLES `business_develop_manage` WRITE;
/*!40000 ALTER TABLE `business_develop_manage` DISABLE KEYS */;
INSERT INTO `business_develop_manage` VALUES (1,2,'推广','张大大','无厘头公司1','123456','123789','123123','电话直拨',62,'360',65,'移动端',282,'12321313','','','','','fe72e102-ae1b-42e3-bb20-519c56e87412','2019-02-27 00:00:00',116,'陈太智',NULL),(2,3,'客户推荐','张大炮','广州市丽眼饰衣服饰有限公司','1231423','感觉v呢的话','','',0,'',0,'',0,'fffffffffffffffffffff','刘强东','死的方法','1','12345674123','fe72e102-ae1b-42e3-bb20-519c56e87413','2019-02-27 00:00:00',116,'陈太智',NULL),(3,81,'内部推荐','123','广州中西联健康网络科技有限公司','123123','3333333','','',0,'',0,'',0,'555555555555','','第三方公司','拂来','123213213','167fa05b-aab4-4542-a0ad-31fe140ea776','2019-02-27 10:47:02',116,'陈太智',NULL),(4,2,'推广','dfs123','fds3','dsf','dsf','fdsf','在线咨询',61,'360',65,'PC端',281,'fffffffffffff','','','','','d548ce72-b237-42bd-90b7-9eb1d040e79b','2019-02-27 13:49:03',116,'陈太智','86_中质量B1类_质量（业务）'),(5,2,'推广','','广州多多邮箱公司','','','','电话直拨',62,'360',65,'移动端',282,'','','','','','0ce85625-4e7e-4132-b216-68e8431f5418','2019-02-27 17:25:05',116,'陈太智','36_咨询注册_咨询（前端）,38_咨询变更_咨询（前端）,93_办理自有地址_成交（业务）,28_直拨电话_渠道（前端）,55_到访后可放弃_跟进（业务）'),(6,2,'推广','111','11','11','121','','在线咨询',61,'百度',64,'PC端',281,'','','','','','bef8e61c-cc24-4555-bf27-6d48e39e74c3','2019-03-02 14:56:53',145,'陈小奋',NULL),(7,2,'推广','sd','dd','dd','dd','dd','在线咨询',61,'百度',64,'PC端',281,'','','','','','d9e269da-82c7-473d-a3c4-088826136a9f','2019-03-02 14:57:32',145,'陈小奋',NULL),(8,2,'推广','dd','dd','dd','dd','dd','在线咨询',61,'百度',64,'PC端',281,'','','','','','6193b76e-c14e-4b75-90f4-2faa54d81e36','2019-03-02 14:58:13',145,'陈小奋',NULL),(9,81,'内部推荐','广州建洁科技开发有限公司','广州建洁科技开发有限公司','广州建洁科技开发有限公司','广州建洁科技开发有限公司','','',0,'',0,'',0,'','广州建洁科技开发有限公司','','','','d973b766-3a7c-4fcf-a230-1066cf6f2e9e','2019-03-02 15:18:01',106,'陈小银',NULL);
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

-- Dump completed on 2019-03-29 17:39:13
