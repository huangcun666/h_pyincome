-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
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
-- Table structure for table `t_plan`
--

DROP TABLE IF EXISTS `t_plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_plan` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `plan_type_id_name` varchar(255) DEFAULT NULL,
  `plan_type_id` int(11) DEFAULT NULL,
  `plan_body` varchar(1011) NOT NULL DEFAULT '0',
  `created_at` datetime NOT NULL,
  `reminder_at` datetime NOT NULL,
  `rtype` int(11) NOT NULL DEFAULT '0',
  `rel_id` int(11) NOT NULL DEFAULT '0',
  `is_read` tinyint(4) NOT NULL DEFAULT '0',
  `is_hide` int(11) NOT NULL DEFAULT '0',
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(100) DEFAULT NULL,
  `is_read_at` datetime DEFAULT NULL,
  `plan_title` varchar(255) DEFAULT NULL,
  `rel_url` varchar(1000) DEFAULT NULL,
  `rtype_name` varchar(255) DEFAULT NULL,
  `business_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_plan`
--

LOCK TABLES `t_plan` WRITE;
/*!40000 ALTER TABLE `t_plan` DISABLE KEYS */;
INSERT INTO `t_plan` VALUES (30,'微信',28,'aaa','2018-08-21 07:13:56','2018-08-21 00:00:00',1,43746,1,0,97,'庄培润','2018-08-21 14:50:28','广州器化医疗设备有限公司','/company?tag=show&guid=93c75468-9ebd-11e8-b047-6045cb9a7117&id=43746','传统商机',NULL),(31,'电话',1,'阿斯顿萨达','2018-08-21 09:49:12','2018-08-02 00:00:00',1,17432,0,0,97,'庄培润',NULL,'广州市八棵杨电子商务有限公司','/company?tag=show&guid=934b3f86-9ebd-11e8-b047-6045cb9a7117&id=17432','传统商机',NULL),(32,'短信',3,'广州伟通网络科技有限公司','2018-08-21 10:16:21','2018-08-15 18:50:00',1,9516,0,0,97,'庄培润',NULL,'广州伟通网络科技有限公司','/company?tag=show&guid=93306f04-9ebd-11e8-b047-6045cb9a7117&id=9516','传统商机',NULL),(33,'电话',1,'1222','2018-08-21 10:24:36','2018-08-22 00:00:00',1,45335,1,0,116,'陈太智','2018-08-21 14:20:54','广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(34,'微信',2,'广州于电科技有限公司','2018-08-21 15:42:50','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(35,'微信',2,'广州于电科技有限公司','2018-08-21 15:42:51','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(36,'微信',2,'广州于电科技有限公司','2018-08-21 15:42:52','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(37,'微信',2,'广州于电科技有限公司','2018-08-21 15:42:52','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(38,'微信',2,'广州于电科技有限公司','2018-08-21 15:42:52','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(39,'微信',2,'广州于电科技有限公司','2018-08-21 15:56:42','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(40,'微信',2,'广州于电科技有限公司','2018-08-21 15:57:53','2018-08-15 10:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(41,'QQ',4,'黄启飞','2018-08-21 16:19:44','2018-08-15 02:30:00',1,45335,0,0,116,'陈太智',NULL,'广州于电科技有限公司','/company?tag=show&guid=35627bb0-a12b-11e8-b047-6045cb9a7117&id=45335','传统商机',NULL),(42,'QQ',4,'梁路娟','2018-08-21 16:47:22','2018-08-08 10:50:00',1,16637,1,0,116,'陈太智','2018-08-21 16:54:59','广州鑫宇化工科技有限公司','/company?tag=show&guid=9348a506-9ebd-11e8-b047-6045cb9a7117&id=16637','传统商机',NULL),(43,'电话',1,'','2019-05-06 18:26:17','2019-05-06 18:20:00',1,0,0,0,116,'陈太智',NULL,'c','/company?tag=show_business&guid=4e9016ec-a382-4acb-a433-b581f1b47ae7&id=13','传统商机',13),(44,'电话',1,'fgdds','2019-05-06 18:26:31','2019-05-06 18:25:00',1,0,0,0,116,'陈太智',NULL,'c','/company?tag=show_business&guid=4e9016ec-a382-4acb-a433-b581f1b47ae7&id=13','传统商机',13),(45,'电话',1,'dasdsafsdfsdf','2019-05-06 18:27:10','2019-05-06 05:25:00',1,0,0,0,116,'陈太智',NULL,'c','/company?tag=show_business&guid=4e9016ec-a382-4acb-a433-b581f1b47ae7&id=13','传统商机',13),(46,'电话',1,'','2019-05-09 09:12:20','2019-05-09 09:15:00',1,0,0,0,116,'陈太智',NULL,'广州市丽眼饰衣服装有限公司','/company?tag=show_business&guid=3eab2856-f7f3-45c1-933c-b92897cac7e7&id=21','传统商机',21);
/*!40000 ALTER TABLE `t_plan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:30
