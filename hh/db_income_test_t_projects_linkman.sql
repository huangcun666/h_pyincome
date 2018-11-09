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
-- Table structure for table `t_projects_linkman`
--

DROP TABLE IF EXISTS `t_projects_linkman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_linkman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `tel` varchar(1000) DEFAULT NULL,
  `gender` tinyint(2) DEFAULT NULL,
  `remark` varchar(2000) DEFAULT NULL,
  `uid_name` varchar(200) DEFAULT NULL,
  `uid` int(11) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `guid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_linkman`
--

LOCK TABLES `t_projects_linkman` WRITE;
/*!40000 ALTER TABLE `t_projects_linkman` DISABLE KEYS */;
INSERT INTO `t_projects_linkman` VALUES (1,'我的天','10086',1,'沃德天那么帅','庄培润',97,'2018-05-23 14:58:42',NULL,413,NULL),(2,'曾志华','13711738169',1,'','朱伟峰',131,'2018-05-27 09:45:55',NULL,897,NULL),(3,'何梓权','13316074507',1,'','朱伟峰',131,'2018-05-27 09:47:26',NULL,898,NULL),(4,'杨曦雯','15013031905',0,'','朱伟峰',131,'2018-05-30 01:41:20',NULL,987,NULL),(5,'邹连英','13644307888',0,'张松超转让公司给邹连英注册','陈小银',106,'2018-06-12 07:21:56',NULL,863,NULL),(6,'123','123456',1,'111','庄培润',97,'2018-06-15 01:46:30',NULL,1231,NULL),(7,'赖嘉华·','13316273760',1,'','朱伟峰',131,'2018-06-26 02:46:11',NULL,1353,NULL),(8,'李婉丽','13829708673',0,'','陈小银',106,'2018-07-03 08:18:15',NULL,1475,NULL),(9,'曹世华','18588829496',0,'这个电话才是曹世华本人的','陈小银',106,'2018-07-11 02:13:16',NULL,1444,NULL),(10,'玫小姐','15971597666',0,'','陈小银',106,'2018-07-16 05:45:59',NULL,1660,NULL),(11,'王先生','13923080397',1,'','庄培润',97,'2018-07-23 10:39:23',NULL,1798,NULL),(12,'钟小姐','13760821491',1,'','庄培润',97,'2018-07-25 09:05:52',NULL,1840,NULL),(13,'钟小姐','13760821491',1,'','庄培润',97,'2018-07-25 09:11:44',NULL,1841,NULL),(14,'钟小姐','13760821491',1,'','庄培润',97,'2018-07-25 09:14:24',NULL,1842,NULL),(16,'李彦庭','17728188926',1,'','陈太智',116,'2018-08-01 02:47:53',NULL,294,NULL),(17,'第三方','打发打发',1,'打发打发','何家辉',123,'2018-08-01 06:54:41',NULL,1508,NULL),(18,'陈','13662529917',0,'这个是她老板娘','冯恒冠',94,'2018-08-02 02:30:04',NULL,821,NULL),(19,'陈','13662529917',0,'这个是她们老板娘的电话','李静',151,'2018-08-02 02:30:46','2018-08-08 01:20:25',820,NULL),(20,'刘小姐','18126877780',1,'','庄培润',97,'2018-08-06 09:27:06',NULL,2166,NULL),(21,'彭辉','13690167260',1,'','冯恒冠',94,'2018-08-09 01:55:05',NULL,819,NULL),(22,'刘家璇','18302009056',1,'','莫诗域',140,'2018-08-09 02:11:17',NULL,576,NULL),(23,'肖小姐','13751288275',0,'','陈勇极',139,'2018-08-10 02:43:50',NULL,686,NULL),(24,'柳剑','13560465665',1,'','陈勇极',139,'2018-08-10 07:00:56',NULL,2118,NULL),(25,'刘帅洋','15915955991',1,'','庄培润',97,'2018-08-13 05:50:42',NULL,2263,NULL),(26,'莫先生','18620011937',1,'','陈小银',106,'2018-08-15 07:58:36',NULL,2296,NULL),(27,'宾利霞','13622213943',0,'法人','黄小芬',182,'2018-08-21 07:49:45',NULL,2194,NULL),(28,'徐晓荣','13922422221',1,'雷素娟老公的电话，只要联系人','冯恒冠',94,'2018-08-23 01:42:44',NULL,2446,NULL),(29,'212','212',1,'','陈太智',116,'2018-08-23 11:11:22',NULL,2466,NULL);
/*!40000 ALTER TABLE `t_projects_linkman` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:22
