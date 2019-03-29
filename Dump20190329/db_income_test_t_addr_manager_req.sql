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
  `ass_remark` varchar(1000) DEFAULT NULL,
  `xs_uid_at` datetime DEFAULT NULL,
  `gw_uid` int(11) NOT NULL DEFAULT '0',
  `gw_uid_name` varchar(255) DEFAULT NULL,
  `gw_uid_at` datetime DEFAULT NULL,
  `req_act_id` int(8) NOT NULL DEFAULT '0',
  `req_act_id_name` varchar(255) DEFAULT NULL,
  `req_act_at` datetime DEFAULT NULL,
  `req_act_uid` int(11) NOT NULL DEFAULT '0',
  `req_act_uid_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_manager_req`
--

LOCK TABLES `t_addr_manager_req` WRITE;
/*!40000 ALTER TABLE `t_addr_manager_req` DISABLE KEYS */;
INSERT INTO `t_addr_manager_req` VALUES (7,70,'广州市南沙区丰泽东路106号（自编1号楼）X1301-B4553（集群注册）(JM)','sadasd','2018-12-20 19:20:41','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,251,'发起收款','2018-12-20 19:20:41',116,'陈太智'),(8,113,'广州市高新技术产业开发区南云三路39号自编八栋研发楼卓业·空间众创空间办公卡位ZYKJ-1F-15（仅限办公用途）','dasdas','2018-12-20 19:20:46','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,251,'发起收款','2018-12-20 19:20:46',116,'陈太智'),(9,175,'55555','da','2018-12-20 19:22:03','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,251,'发起收款','2018-12-20 19:22:03',116,'陈太智'),(10,362,'','','2018-12-21 13:56:28','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,251,'发起收款','2018-12-21 13:56:28',116,'陈太智'),(11,362,'','','2018-12-21 13:57:58','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,6,'发起收款','2018-12-21 13:57:58',116,'陈太智'),(12,366,'','','2018-12-21 13:58:28','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,6,'发起收款','2018-12-21 13:58:28',116,'陈太智'),(13,366,'','','2018-12-21 13:58:36','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,6,'发起收款','2018-12-21 13:58:36',116,'陈太智'),(14,366,'','','2018-12-21 13:58:51','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,6,'发起收款','2018-12-21 13:58:51',116,'陈太智'),(15,366,'','','2018-12-21 13:59:09','陈太智',116,0,NULL,NULL,NULL,0,NULL,NULL,6,'发起收款','2018-12-21 13:59:09',116,'陈太智');
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

-- Dump completed on 2019-03-29 17:39:20
