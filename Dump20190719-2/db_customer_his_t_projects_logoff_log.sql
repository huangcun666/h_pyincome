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
-- Table structure for table `t_projects_logoff_log`
--

DROP TABLE IF EXISTS `t_projects_logoff_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_logoff_log` (
  `mid` int(11) NOT NULL DEFAULT '0',
  `project_id` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL DEFAULT '0',
  `type_id` int(11) NOT NULL DEFAULT '0',
  `leader_uid` int(11) NOT NULL DEFAULT '0',
  `reject_remark` varchar(2000) DEFAULT NULL,
  `logoff_id` int(11) NOT NULL DEFAULT '0',
  `reject_at` datetime DEFAULT NULL,
  `btype_id` int(11) NOT NULL DEFAULT '0',
  `leader_uid_name` varchar(255) DEFAULT NULL,
  `uid_name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_logoff_log`
--

LOCK TABLES `t_projects_logoff_log` WRITE;
/*!40000 ALTER TABLE `t_projects_logoff_log` DISABLE KEYS */;
INSERT INTO `t_projects_logoff_log` VALUES (37910,4953,239,1,119,'没有清算回执',13,'2019-01-07 10:03:14',1,'罗文波','李杰'),(47906,3123,210,3,119,'跟进记录不完整',18,'2019-01-08 15:45:19',3,'罗文波','陈月娇'),(47905,5397,210,3,119,'跟进记录不完整',17,'2019-01-08 15:45:28',3,'罗文波','陈月娇'),(39399,5119,239,2,239,'',62,'2019-01-16 14:17:37',2,'李杰','李杰'),(31069,4037,239,2,119,'跟进记录不完整',129,'2019-01-24 09:06:32',2,'罗文波','李杰'),(33228,2048,239,1,119,'非注销清算登报，是点错了',293,'2019-02-28 17:57:27',1,'罗文波','李杰'),(54688,6890,239,2,119,'未注销完营业执照',318,'2019-03-07 09:19:01',2,'罗文波','李杰'),(52597,6608,239,2,119,'未完成执照银行注销。',317,'2019-03-07 09:29:37',2,'罗文波','李杰'),(48303,6125,239,2,239,'',410,'2019-03-19 17:10:45',2,'李杰','李杰'),(65100,5012,154,3,119,'没有国地税办结',407,'2019-03-20 10:32:21',3,'罗文波','廖小捷'),(65092,5120,154,3,119,'没有国地税',401,'2019-03-20 10:36:52',3,'罗文波','廖小捷'),(65109,4057,461,1,119,'点错了，做了什么就点什么！',427,'2019-03-21 14:32:56',1,'罗文波','李沅芳'),(65118,3022,461,1,119,'点错了，做了什么就点什么！',428,'2019-03-21 14:33:11',1,'罗文波','李沅芳'),(65109,4057,461,3,119,'',435,'2019-03-22 09:33:33',3,'罗文波','李沅芳'),(62877,6993,461,2,119,'未办结，点错',493,'2019-03-29 14:02:47',2,'罗文波','李沅芳'),(77252,5656,106,3,119,'点错',628,'2019-04-18 17:33:14',3,'罗文波','陈小银');
/*!40000 ALTER TABLE `t_projects_logoff_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:34
