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
-- Table structure for table `business_develop_manage_linkman`
--

DROP TABLE IF EXISTS `business_develop_manage_linkman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_manage_linkman` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link_name` varchar(45) DEFAULT NULL,
  `link_gender` tinyint(4) DEFAULT NULL,
  `link_tel` varchar(45) DEFAULT NULL,
  `link_remark` varchar(255) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `is_first` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage_linkman`
--

LOCK TABLES `business_develop_manage_linkman` WRITE;
/*!40000 ALTER TABLE `business_develop_manage_linkman` DISABLE KEYS */;
INSERT INTO `business_develop_manage_linkman` VALUES (1,'12',1,'ds','',15,'2019-05-09 14:40:00','陈太智',116,1),(2,'李二狗',1,'','',32,'2019-05-15 17:01:40','庄培润',97,0),(3,'第三方',1,'123213','',16,'2019-05-17 14:44:39','仝春梅',143,0),(4,'213',1,'213','',18,'2019-05-17 14:47:23','陈太智',116,0),(5,'张全蛋',1,'123213123','',32,'2019-05-23 10:08:45','庄培润',97,1),(6,'黄的一笔',1,'123','',37,'2019-05-23 10:30:50','陈太智',116,0),(7,'翻翻翻翻',1,'1111111111114444','',37,'2019-05-23 10:30:51','冯恒冠',94,1),(8,'无法无天',1,'123','',37,'2019-05-23 10:30:51','陈太智',116,0),(9,'无法无天',1,'123','',37,'2019-05-23 10:30:52','陈太智',116,0),(10,'无法无天',1,'123','',37,'2019-05-23 10:30:59','陈太智',116,0),(11,'热狗',NULL,'324r324',NULL,43,'2019-05-23 11:15:12','庄培润',97,1),(12,'第三方第三方',1,'12313','',43,'2019-05-23 11:17:01','庄培润',97,0),(13,'财讯困',NULL,'1231313213213',NULL,44,'2019-05-23 11:18:02','庄培润',97,1),(14,'2312',1,'','第三方司法地方第三方分速度第三方分分分分分分分',21,'2019-05-24 16:57:51','陈太智',116,1),(15,'快快快',NULL,'123',NULL,47,'2019-05-28 11:32:50','陈太智',116,1),(16,'21',NULL,'2',NULL,48,'2019-05-28 14:25:48','冯恒冠',94,1),(17,'1',NULL,'2',NULL,49,'2019-05-28 14:52:40','冯恒冠',94,1),(18,'得粉碎斯蒂芬',1,'6666666666666','',29,'2019-05-29 10:44:40','冯恒冠',94,0),(19,'777',1,'dtr344r523','',29,'2019-05-29 10:45:01','冯恒冠',94,0),(20,'漂漂漂漂',1,'1354646','',29,'2019-05-29 11:04:08','冯恒冠',94,1),(21,'龙淑芬',NULL,'123',NULL,50,'2019-06-03 16:58:46','陈太智',116,1),(22,'发达到沙发',NULL,'奋',NULL,51,'2019-06-03 17:09:34','陈太智',116,1),(23,'发达到沙发',NULL,'奋',NULL,52,'2019-06-03 17:10:03','陈太智',116,1),(24,'大法师奋',NULL,'大赛反倒是',NULL,53,'2019-06-03 17:11:31','陈太智',116,1),(25,'大法师奋',NULL,'大赛反倒是',NULL,54,'2019-06-03 17:12:15','陈太智',116,1),(26,'大法师奋',NULL,'大赛反倒是',NULL,55,'2019-06-03 17:12:39','陈太智',116,1),(27,'大法师奋',NULL,'大赛反倒是',NULL,56,'2019-06-03 17:13:00','陈太智',116,1),(28,'123',NULL,'1231',NULL,57,'2019-06-03 17:25:47','陈太智',116,1),(29,'个人个2',NULL,'123124',NULL,58,'2019-06-03 17:37:16','陈太智',116,1),(30,'张无忌',NULL,'1488448',NULL,59,'2019-06-04 09:12:23','陈太智',116,1),(31,'123',1,'2131','',28,'2019-06-13 11:10:47','陈太智',116,0),(32,'公分高',NULL,'1231432142',NULL,60,'2019-06-13 11:12:08','陈太智',116,1),(33,'斯蒂芬',2,'12313214',NULL,61,'2019-06-13 11:46:33','陈太智',116,1),(34,'大锤',1,'12313',NULL,62,'2019-06-13 11:47:17','陈太智',116,1),(35,'dd哦哦',2,'ddd','None',63,'2019-06-13 11:55:48','陈太智',116,1),(36,'一袋米',2,'2132424324',NULL,64,'2019-06-13 14:04:25','陈太智',116,1);
/*!40000 ALTER TABLE `business_develop_manage_linkman` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:06:41
