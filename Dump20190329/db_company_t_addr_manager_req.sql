-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_company
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
-- Table structure for table `t_addr_manager_req`
--

DROP TABLE IF EXISTS `t_addr_manager_req`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_manager_req` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addr_id` int(11) NOT NULL,
  `req_now_addr` varchar(555) DEFAULT NULL,
  `req_remark` varchar(2000) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `created_uid` int(11) DEFAULT '0',
  `xs_uid` int(11) NOT NULL DEFAULT '0',
  `xs_uid_name` varchar(255) DEFAULT NULL,
  `xs_uid_at` datetime DEFAULT NULL,
  `gw_uid` int(11) NOT NULL DEFAULT '0',
  `gw_uid_name` varchar(255) DEFAULT NULL,
  `gw_uid_at` datetime DEFAULT NULL,
  `req_act_id` int(8) NOT NULL DEFAULT '0',
  `req_act_id_name` varchar(255) DEFAULT NULL,
  `req_act_at` datetime DEFAULT NULL,
  `req_act_uid` int(11) NOT NULL DEFAULT '0',
  `req_act_uid_at` datetime DEFAULT NULL,
  `req_act_uid_name` varchar(255) DEFAULT NULL,
  `follow_uid` int(11) NOT NULL DEFAULT '0',
  `follow_uid_name` varchar(255) DEFAULT NULL,
  `follow_uid_confirm` datetime DEFAULT NULL,
  `ass_uid` int(11) NOT NULL DEFAULT '0',
  `ass_uid_name` varchar(255) NOT NULL DEFAULT '0',
  `ass_uid_at` datetime DEFAULT NULL,
  `ass_remark` varchar(1000) DEFAULT NULL,
  `finish_type_id` int(11) DEFAULT '0',
  `finish_type_name` varchar(45) DEFAULT NULL,
  `finish_uid` int(11) NOT NULL DEFAULT '0',
  `finish_uid_name` varchar(255) NOT NULL DEFAULT '0',
  `finish_uid_at` datetime DEFAULT NULL,
  `finish_remark` varchar(1000) DEFAULT NULL,
  `leader_uid` int(11) NOT NULL DEFAULT '0',
  `leader_uid_name` varchar(255) NOT NULL DEFAULT '0',
  `leader_uid_at` datetime DEFAULT NULL,
  `leader_remark` varchar(1000) DEFAULT NULL,
  `leader_type_id` int(11) DEFAULT '0',
  `leader_type_id_name` varchar(45) DEFAULT NULL,
  `project_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_manager_req`
--

LOCK TABLES `t_addr_manager_req` WRITE;
/*!40000 ALTER TABLE `t_addr_manager_req` DISABLE KEYS */;
INSERT INTO `t_addr_manager_req` VALUES (35,872,'','','2018-12-26 17:59:28','陈太智',116,0,NULL,NULL,0,NULL,NULL,6,'续费审核','2019-01-15 15:52:39',116,'2019-01-15 15:52:39','陈太智',95,'何诗明','2019-01-15 12:36:49',95,'何诗明','2019-01-15 12:36:48','dddd',0,'已续费',95,'何诗明','2019-01-15 12:37:00','aaaa',0,'0',NULL,NULL,0,NULL,0),(36,869,'','','2018-12-26 18:43:03','陈太智',116,0,NULL,NULL,0,NULL,NULL,6,'续费审核','2019-01-15 15:59:28',116,'2019-01-15 15:59:28','陈太智',97,'庄培润','2019-01-15 15:59:09',93,'domizzi','2019-01-14 17:46:42','',0,'已续费',97,'庄培润','2019-01-15 15:59:17','',116,'陈太智',NULL,NULL,1,'通过',234),(38,870,'','','2018-12-27 15:59:10','陈太智',116,0,NULL,NULL,0,NULL,NULL,5,'不续费审核','2019-01-15 14:19:49',116,'2019-01-15 14:19:49','陈太智',93,'domizzi','2018-12-27 15:59:31',116,'陈太智','2018-12-27 15:59:23','',0,'不续费',93,'domizzi','2019-01-15 11:57:22','',116,'陈太智','2019-01-15 14:19:49','',1,'通过',2743),(39,856,'','','2018-12-28 15:55:18','陈太智',116,0,NULL,NULL,0,NULL,NULL,4,'已处理','2019-01-15 15:19:18',93,'2019-01-15 15:19:18','domizzi',93,'domizzi','2019-01-15 15:18:18',116,'陈太智','2019-01-15 09:32:50','',0,'不续费',93,'domizzi','2019-01-15 15:19:18','',0,'0',NULL,NULL,0,NULL,4433),(40,852,'','','2018-12-28 15:55:38','陈太智',116,0,NULL,NULL,0,NULL,NULL,1,'待安排','2018-12-28 15:55:38',116,NULL,'陈太智',0,NULL,NULL,0,'0',NULL,NULL,0,NULL,0,'0',NULL,NULL,0,'0',NULL,NULL,0,NULL,0),(41,852,'','','2018-12-28 15:55:44','陈太智',116,0,NULL,NULL,0,NULL,NULL,1,'待安排','2018-12-28 15:55:44',116,NULL,'陈太智',0,NULL,NULL,0,'0',NULL,NULL,0,NULL,0,'0',NULL,NULL,0,'0',NULL,NULL,0,NULL,0),(50,407,'','','2019-01-15 11:40:34','何诗明',95,0,NULL,NULL,0,NULL,NULL,1,'待安排','2019-01-15 11:40:34',95,NULL,'何诗明',0,NULL,NULL,0,'0',NULL,NULL,0,NULL,0,'0',NULL,NULL,0,'0',NULL,NULL,0,NULL,0);
/*!40000 ALTER TABLE `t_addr_manager_req` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:04
