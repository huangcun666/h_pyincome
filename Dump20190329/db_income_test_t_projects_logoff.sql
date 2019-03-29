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
-- Table structure for table `t_projects_logoff`
--

DROP TABLE IF EXISTS `t_projects_logoff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_logoff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) NOT NULL,
  `project_id` int(11) DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  `finish_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `leader_uid` int(11) NOT NULL DEFAULT '0',
  `leader_uid_name` varchar(255) DEFAULT NULL,
  `leader_at` datetime DEFAULT NULL,
  `state_id` int(11) DEFAULT '0',
  `state_id_name` varchar(255) DEFAULT NULL,
  `state_id_remark` varchar(2000) DEFAULT NULL,
  `type_id` int(11) NOT NULL DEFAULT '0',
  `type_id_name` varchar(255) DEFAULT NULL,
  `last_reject_remark` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41347 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_logoff`
--

LOCK TABLES `t_projects_logoff` WRITE;
/*!40000 ALTER TABLE `t_projects_logoff` DISABLE KEYS */;
INSERT INTO `t_projects_logoff` VALUES (41330,40108,5184,239,'李杰','2018-12-30 15:11:15',NULL,239,'李杰','2018-12-30 15:12:04',2,'已审核',NULL,1,'清算登报',NULL),(41331,40108,5184,239,'李杰','2018-12-30 15:11:59',NULL,239,'李杰','2018-12-30 15:17:45',2,'已审核',NULL,2,'执照银行',NULL),(41333,40108,5184,239,'李杰','2018-12-30 15:20:06',NULL,95,'何诗明','2018-12-30 16:02:38',2,'已审核',NULL,3,'国地税',NULL),(41334,42331,5436,239,'李杰','2018-12-30 16:12:35',NULL,95,'何诗明','2018-12-30 16:13:32',2,'已审核',NULL,1,'清算登报',NULL),(41336,42331,5436,239,'李杰','2018-12-30 16:37:21',NULL,116,'陈太智','2019-01-02 16:59:11',2,'已审核',NULL,2,'执照银行',NULL),(41337,42331,5436,239,'李杰','2018-12-30 16:40:32',NULL,116,'陈太智','2019-01-02 16:44:22',2,'已审核',NULL,3,'国地税',NULL),(41338,40411,5224,239,'李杰','2018-12-30 17:18:48',NULL,95,'何诗明','2018-12-30 17:22:11',3,'驳回',NULL,1,'清算登报',NULL),(41339,40411,5224,239,'李杰','2019-01-02 08:52:57',NULL,116,'陈太智','2019-01-02 16:58:37',2,'已审核',NULL,2,'执照银行',NULL),(41340,40411,5224,239,'李杰','2019-01-02 09:05:10',NULL,116,'陈太智','2019-01-02 16:56:50',2,'已审核',NULL,3,'国地税',NULL),(41341,39399,5119,239,'李杰','2019-01-03 13:57:06',NULL,116,'陈太智','2019-01-03 14:33:40',2,'已审核',NULL,1,'清算登报',NULL),(41342,39399,5119,239,'李杰','2019-01-03 18:10:22',NULL,116,'陈太智','2019-01-03 18:10:32',2,'已审核',NULL,2,'执照银行','ddd'),(41343,39399,5119,239,'李杰','2019-01-03 18:01:21',NULL,116,'陈太智','2019-01-03 18:02:06',2,'已审核',NULL,3,'国地税','错误了'),(41344,39397,5120,239,'李杰','2019-01-04 09:08:14',NULL,116,'陈太智','2019-01-04 09:08:25',2,'已审核',NULL,1,'清算登报','cxxxxxx'),(41345,39397,5120,239,'李杰','2019-01-04 09:56:25',NULL,116,'陈太智','2019-01-04 09:56:33',2,'已审核',NULL,2,'执照银行','cccccc'),(41346,8133,1362,138,'王坚','2019-03-19 09:23:20',NULL,0,NULL,NULL,1,'待审核',NULL,1,'清算登报',NULL);
/*!40000 ALTER TABLE `t_projects_logoff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:27
