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
-- Table structure for table `business_develop_manage_msg`
--

DROP TABLE IF EXISTS `business_develop_manage_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_manage_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `message` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  `tag_type` varchar(255) DEFAULT NULL,
  `btype_id` int(11) NOT NULL DEFAULT '1',
  `company_name` varchar(255) DEFAULT NULL,
  `company_regid` varchar(255) DEFAULT NULL,
  `rel_id` int(11) NOT NULL DEFAULT '0',
  `ext_id` int(11) NOT NULL DEFAULT '0',
  `file_list` varchar(4000) DEFAULT NULL,
  `project_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3715 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_manage_msg`
--

LOCK TABLES `business_develop_manage_msg` WRITE;
/*!40000 ALTER TABLE `business_develop_manage_msg` DISABLE KEYS */;
INSERT INTO `business_develop_manage_msg` VALUES (3703,116,'陈太智','设置跟进人为庄培润','2019-02-28 13:59:07',NULL,2,'操作记录',2,NULL,NULL,0,0,NULL,0),(3704,97,'庄培润','庄培润已接单','2019-02-28 14:06:57',NULL,2,'操作记录',2,NULL,NULL,0,0,NULL,0),(3705,97,'庄培润','庄培润确认办结','2019-02-28 14:11:02',NULL,2,'操作记录',2,NULL,NULL,0,0,NULL,0),(3706,116,'陈太智','陈太智审核通过','2019-02-28 14:30:56',NULL,2,'操作记录',2,NULL,NULL,0,0,NULL,0),(3707,97,'庄培润','庄培润已接单','2019-02-28 15:54:48',NULL,5,'操作记录',2,NULL,NULL,0,0,NULL,0),(3708,116,'陈太智','36_咨询注册_咨询（前端）,36_咨询注册_咨询（前端）','2019-03-04 17:30:18',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3709,116,'陈太智','37_咨询记账_咨询（前端）,36_咨询注册_咨询（前端）','2019-03-04 17:31:43',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3710,116,'陈太智','37_咨询记账_咨询（前端）,38_咨询变更_咨询（前端）,36_咨询注册_咨询（前端）,37_咨询记账_咨询（前端）','2019-03-04 17:32:42',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3711,116,'陈太智','36_咨询注册_咨询（前端）','2019-03-04 17:33:55',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3712,116,'陈太智','36_咨询注册_咨询（前端）,38_咨询变更_咨询（前端）,93_办理自有地址_成交（业务）','2019-03-04 17:34:08',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3713,116,'陈太智','36_咨询注册_咨询（前端）,38_咨询变更_咨询（前端）,93_办理自有地址_成交（业务）,28_直拨电话_渠道（前端）,55_到访后可放弃_跟进（业务）','2019-03-04 17:38:45',NULL,5,'操作标签',1,NULL,NULL,0,0,NULL,0),(3714,116,'陈太智','86_中质量B1类_质量（业务）','2019-03-04 17:44:03',NULL,4,'操作标签',1,NULL,NULL,0,0,NULL,0);
/*!40000 ALTER TABLE `business_develop_manage_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:15
