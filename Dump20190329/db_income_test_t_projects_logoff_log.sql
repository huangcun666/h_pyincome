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
INSERT INTO `t_projects_logoff_log` VALUES (40411,5224,239,3,116,'试试撒',41340,'2019-01-02 16:50:26',3,'陈太智','李杰'),(39399,5119,239,2,116,'嘻嘻嘻',41342,'2019-01-03 14:34:38',2,'陈太智','李杰'),(39399,5119,239,3,116,'错误了',41343,'2019-01-03 14:39:38',3,'陈太智','李杰'),(39399,5119,239,3,116,'错误了',41343,'2019-01-03 14:40:01',3,'陈太智','李杰'),(39399,5119,239,3,116,'错误了',41343,'2019-01-03 14:40:14',3,'陈太智','李杰'),(39399,5119,239,2,116,'ddd',41342,'2019-01-03 18:10:07',2,'陈太智','李杰'),(39397,5120,239,1,116,'cxxxxxx',41344,'2019-01-04 09:05:34',1,'陈太智','李杰'),(39397,5120,239,2,116,'cccccc',41345,'2019-01-04 09:56:12',2,'陈太智','李杰');
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

-- Dump completed on 2019-03-29 17:39:14
