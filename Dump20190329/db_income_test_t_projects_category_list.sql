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
-- Table structure for table `t_projects_category_list`
--

DROP TABLE IF EXISTS `t_projects_category_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_category_list` (
  `project_id` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `order_int` int(11) NOT NULL DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_category_list`
--

LOCK TABLES `t_projects_category_list` WRITE;
/*!40000 ALTER TABLE `t_projects_category_list` DISABLE KEYS */;
INSERT INTO `t_projects_category_list` VALUES (225,141,35,'已交接',0,'2018-05-29 16:04:31'),(319,141,35,'已交接',0,'2018-05-29 16:04:58'),(407,141,35,'已交接',0,'2018-05-29 16:05:14'),(426,152,25,'已交接',0,'2018-05-23 16:30:10'),(472,152,25,'已交接',0,'2018-05-23 16:30:12'),(479,152,25,'已交接',0,'2018-05-23 16:30:26'),(489,154,23,'办理中',0,'2018-05-25 14:07:59'),(518,141,35,'已交接',0,'2018-05-29 16:06:28'),(522,152,24,'已办结',0,'2018-05-23 16:29:57'),(524,152,3,'已交接',0,'2018-05-21 10:16:32'),(537,141,35,'已交接',0,'2018-05-29 16:06:10'),(566,152,25,'已交接',0,'2018-05-23 16:29:19'),(571,152,25,'已交接',0,'2018-05-23 16:29:27'),(572,152,25,'已交接',0,'2018-05-23 16:29:37'),(612,152,25,'已交接',0,'2018-05-29 10:54:43'),(622,152,25,'已交接',0,'2018-05-23 16:30:42'),(626,152,25,'已交接',0,'2018-05-29 10:54:50'),(643,152,23,'办理中',0,'2018-05-23 17:01:57'),(644,152,25,'已交接',0,'2018-05-23 16:28:37'),(648,152,24,'已办结',0,'2018-05-23 16:28:29'),(662,152,1,'办理中',0,'2018-05-18 13:41:33'),(679,152,1,'办理中',0,'2018-05-18 13:41:30'),(681,152,1,'办理中',0,'2018-05-18 13:41:27'),(682,152,1,'办理中',0,'2018-05-18 13:41:23'),(684,152,24,'已办结',0,'2018-05-18 13:41:19'),(694,152,1,'办理中',0,'2018-05-18 13:40:47'),(696,152,25,'已交接',0,'2018-05-18 13:40:44'),(702,152,1,'办理中',0,'2018-05-18 13:40:40'),(710,122,1,'办理中',0,'2018-05-18 10:07:51'),(711,97,1,'办理中',0,'2018-05-17 09:56:29'),(721,152,1,'办理中',0,'2018-05-18 13:40:33'),(727,122,1,'办理中',0,'2018-05-18 10:07:48'),(822,141,33,'办理中',0,'2018-05-29 16:00:39'),(828,154,23,'办理中',0,'2018-05-25 14:07:54'),(831,154,24,'已办结',0,'2018-05-25 14:07:48'),(834,141,33,'办理中',0,'2018-05-29 16:00:34'),(836,141,33,'办理中',0,'2018-05-29 16:00:30'),(840,141,33,'办理中',0,'2018-05-29 16:00:27'),(841,141,33,'办理中',0,'2018-05-29 16:00:25'),(860,141,33,'办理中',0,'2018-05-29 16:00:20'),(915,154,23,'办理中',0,'2018-05-28 13:48:43'),(924,141,33,'办理中',0,'2018-05-29 16:00:17'),(927,141,33,'办理中',0,'2018-05-29 16:00:15'),(933,141,33,'办理中',0,'2018-05-29 16:00:11'),(966,141,33,'办理中',0,'2018-05-29 15:59:45');
/*!40000 ALTER TABLE `t_projects_category_list` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:28
