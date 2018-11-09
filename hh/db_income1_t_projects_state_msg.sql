-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income1
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
-- Table structure for table `t_projects_state_msg`
--

DROP TABLE IF EXISTS `t_projects_state_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_state_msg` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `state_id` varchar(255) NOT NULL,
  `state_remark` varchar(2000) DEFAULT NULL,
  `project_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `guid` varchar(255) NOT NULL DEFAULT '',
  `uid` int(11) DEFAULT NULL,
  `state_id_name` varchar(255) NOT NULL DEFAULT '',
  `uid_name` varchar(50) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `type_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_state_msg`
--

LOCK TABLES `t_projects_state_msg` WRITE;
/*!40000 ALTER TABLE `t_projects_state_msg` DISABLE KEYS */;
INSERT INTO `t_projects_state_msg` VALUES (1,'11','11111',418,'2018-04-25 01:32:11','7a01cdea-4828-11e8-bfea-6045cb9a7117',133,'公司注册','黄晓芳','2018-04-25 01:36:01',0),(2,'6','33',418,'2018-04-25 01:35:34','f2cea763-4828-11e8-bfea-6045cb9a7117',133,'领取执照','黄晓芳','2018-04-25 01:36:06',0),(3,'5','',418,'2018-04-25 01:35:38','f57f64d0-4828-11e8-bfea-6045cb9a7117',133,'执照受理','黄晓芳',NULL,0),(4,'11','',414,'2018-04-25 01:46:13','6fb5d972-482a-11e8-bfea-6045cb9a7117',98,'公司注册','吴蔚亮',NULL,0),(5,'5','ddd',418,'2018-04-25 01:49:14','dbb1266c-482a-11e8-bfea-6045cb9a7117',98,'执照受理','吴蔚亮',NULL,0),(6,'10','资料已齐全',415,'2018-04-28 07:11:59','714129c9-4ab3-11e8-bfea-6045cb9a7117',97,'资料审查','庄培润',NULL,0),(7,'10','',379,'2018-04-28 07:42:17','acb2fafb-4ab7-11e8-bfea-6045cb9a7117',97,'资料审查','庄培润',NULL,0),(8,'8','',379,'2018-04-28 07:42:32','b5c2b254-4ab7-11e8-bfea-6045cb9a7117',97,'银行开户','庄培润',NULL,0),(9,'10','',379,'2018-04-28 07:55:59','96ae12c3-4ab9-11e8-bfea-6045cb9a7117',97,'资料审查','庄培润',NULL,0),(10,'8','cc',379,'2018-04-28 07:56:15','a06609b0-4ab9-11e8-bfea-6045cb9a7117',97,'银行开户','庄培润',NULL,0),(11,'10','11',379,'2018-04-28 07:56:38','ae52040f-4ab9-11e8-bfea-6045cb9a7117',97,'资料审查','庄培润',NULL,0),(12,'8','222',379,'2018-04-28 08:01:52','69394b0b-4aba-11e8-bfea-6045cb9a7117',97,'银行开户','庄培润',NULL,2),(13,'1','111',379,'2018-04-28 08:01:57','6c18554e-4aba-11e8-bfea-6045cb9a7117',97,'预计核名','庄培润',NULL,1),(14,'8','分',413,'2018-04-28 10:09:11','3234a27a-4acc-11e8-bfea-6045cb9a7117',97,'银行开户','庄培润','2018-05-14 07:48:38',2),(21,'6','呦吼吼吼',413,'2018-05-14 06:46:56','98002435-5742-11e8-a20d-6045cb9a7117',97,'领取执照','庄培润','2018-05-14 07:47:32',1),(39,'6','张飞',411,'2018-05-14 08:03:48','55379ee4-574d-11e8-a20d-6045cb9a7117',97,'领取执照','庄培润',NULL,1),(43,'9','刘备',411,'2018-05-14 08:11:51','74d5b480-574e-11e8-a20d-6045cb9a7117',97,'核名中','庄培润',NULL,2),(44,'8','关羽',411,'2018-05-14 08:12:37','9083b686-574e-11e8-a20d-6045cb9a7117',97,'银行开户','庄培润',NULL,2),(45,'1','赵云',411,'2018-05-14 08:13:02','9f38b07f-574e-11e8-a20d-6045cb9a7117',97,'预计核名','庄培润','2018-05-14 08:13:23',1),(46,'6','赵云a',411,'2018-05-14 08:19:22','81dfde4d-574f-11e8-a20d-6045cb9a7117',97,'领取执照','庄培润','2018-05-14 08:20:18',1),(47,'10','啊哈',409,'2018-05-15 01:40:27','f1da58f8-57e0-11e8-a20d-6045cb9a7117',97,'资料审查','庄培润',NULL,1),(48,'9','嗯哼',409,'2018-05-15 01:40:43','fb6b8c9c-57e0-11e8-a20d-6045cb9a7117',97,'核名中','庄培润','2018-05-15 01:40:50',2),(50,'10','好啊',418,'2018-05-15 02:32:40','3d3ed77f-57e8-11e8-a20d-6045cb9a7117',154,'资料审查','吴彦祖',NULL,1),(51,'10','eeee',185,'2018-05-15 10:39:44','3a0de208-57e9-11e8-a20d-6045cb9a7117',97,'资料审查','庄培润',NULL,1),(52,'9','666',185,'2018-05-15 10:40:41','5bd9ca4d-57e9-11e8-a20d-6045cb9a7117',97,'核名中','庄培润',NULL,2),(53,'1','666',413,'2018-05-15 14:27:00','f99492d3-5808-11e8-a20d-6045cb9a7117',97,'预计核名','庄培润',NULL,1),(55,'43','分分',415,'2018-05-17 15:59:47','44723699-59a8-11e8-a20d-6045cb9a7117',97,'已收取资料','庄培润','2018-05-21 11:24:39',3),(56,'57','123',415,'2018-05-17 16:00:13','544604ab-59a8-11e8-a20d-6045cb9a7117',97,'受阻','庄培润',NULL,4),(57,'75','111',415,'2018-05-17 16:00:30','5e567d84-59a8-11e8-a20d-6045cb9a7117',97,'商标证书','庄培润',NULL,6),(58,'93','跑',415,'2018-05-17 16:00:40','64674cdb-59a8-11e8-a20d-6045cb9a7117',97,'跑腿','庄培润',NULL,8),(60,'62','家',415,'2018-05-17 16:05:18','0a21f50d-59a9-11e8-a20d-6045cb9a7117',97,'已与客户建立联系','庄培润',NULL,5),(61,'13','我',415,'2018-05-17 16:10:13','b98e8f16-59a9-11e8-a759-6045cb9a7117',97,'受阻','庄培润','2018-05-23 11:52:15',1),(62,'27','rrer',415,'2018-05-17 16:14:08','45d64851-59aa-11e8-a759-6045cb9a7117',97,'资料审查','庄培润','2018-05-17 16:14:13',2),(63,'11','好分',415,'2018-05-21 09:13:20','263effc6-5c94-11e8-a759-6045cb9a7117',97,'资料审查','庄培润','2018-05-21 11:22:03',1),(64,'25','很好',415,'2018-05-21 09:13:36','300581c0-5c94-11e8-a759-6045cb9a7117',97,'税务环节','庄培润','2018-05-21 11:59:10',1),(65,'12','',414,'2018-05-21 10:05:54','7e3c8016-5c9b-11e8-a759-6045cb9a7117',106,'已与客户建立联系','陈小银',NULL,1),(66,'26','',414,'2018-05-21 10:05:59','81603744-5c9b-11e8-a759-6045cb9a7117',106,'其他','陈小银',NULL,1),(67,'24','',414,'2018-05-21 10:06:03','840d0a5d-5c9b-11e8-a759-6045cb9a7117',106,'银行开户','陈小银',NULL,1),(68,'25','',414,'2018-05-21 10:06:08','86961bf0-5c9b-11e8-a759-6045cb9a7117',106,'税务环节','陈小银',NULL,1),(69,'24','',414,'2018-05-21 10:06:13','89768b94-5c9b-11e8-a759-6045cb9a7117',106,'银行开户','陈小银',NULL,1),(70,'26','',414,'2018-05-21 10:06:24','901bb1a4-5c9b-11e8-a759-6045cb9a7117',106,'其他','陈小银',NULL,1),(71,'26','',414,'2018-05-21 10:06:29','936ad6f4-5c9b-11e8-a759-6045cb9a7117',106,'其他','陈小银',NULL,1),(72,'33','11',415,'2018-05-21 10:10:23','1f004093-5c9c-11e8-a759-6045cb9a7117',97,'执照受理','庄培润','2018-05-21 11:13:53',2),(73,'38','11',415,'2018-05-21 10:10:30','22d92645-5c9c-11e8-a759-6045cb9a7117',97,'税务变更中','庄培润',NULL,2),(74,'42','66',415,'2018-05-21 10:11:02','36104263-5c9c-11e8-a759-6045cb9a7117',97,'已与客户建立联系','庄培润',NULL,3),(76,'57','123',415,'2018-05-21 10:11:38','4b398813-5c9c-11e8-a759-6045cb9a7117',97,'受阻','庄培润','2018-05-23 11:56:11',4),(77,'59','777',415,'2018-05-21 10:11:46','505ec077-5c9c-11e8-a759-6045cb9a7117',97,'注销银行','庄培润',NULL,4),(78,'65','e',415,'2018-05-21 10:12:02','5985b769-5c9c-11e8-a759-6045cb9a7117',97,'领取证件','庄培润',NULL,5),(79,'67','er',415,'2018-05-21 10:12:10','5ec09a81-5c9c-11e8-a759-6045cb9a7117',97,'其他','庄培润',NULL,5),(80,'103','dai',415,'2018-05-21 10:12:24','671daba1-5c9c-11e8-a759-6045cb9a7117',97,'代缴罚款','庄培润',NULL,8),(81,'103','呜呜呜',415,'2018-05-21 10:12:33','6be8ebaf-5c9c-11e8-a759-6045cb9a7117',97,'代缴罚款','庄培润','2018-05-21 11:15:11',8),(82,'13','好',415,'2018-05-21 11:23:35','58be8ddf-5ca6-11e8-bddb-6045cb9a7117',97,'受阻','庄培润',NULL,1),(83,'11','恩he',415,'2018-05-21 11:23:52','62d1b4ca-5ca6-11e8-bddb-6045cb9a7117',97,'资料审查','庄培润','2018-05-22 09:19:21',1),(84,'11','资料已齐全',417,'2018-05-21 12:01:22','9fde347f-5cab-11e8-bddb-6045cb9a7117',116,'资料审查','陈太智',NULL,1),(85,'12','已与客户联系',417,'2018-05-21 12:01:46','adcf7165-5cab-11e8-bddb-6045cb9a7117',116,'已与客户建立联系','陈太智',NULL,1),(86,'14','核名通知书已拿到3',417,'2018-05-21 12:02:22','c3583643-5cab-11e8-bddb-6045cb9a7117',116,'预计核名','陈太智','2018-05-21 12:04:40',1),(87,'17','等等客户确认经营范围2',417,'2018-05-21 12:02:42','cf61a09f-5cab-11e8-bddb-6045cb9a7117',116,'勾选经营范围','陈太智','2018-05-21 12:04:34',1),(88,'18','地址已安排1',417,'2018-05-21 12:02:53','d6304d46-5cab-11e8-bddb-6045cb9a7117',116,'地址安排','陈太智','2018-05-21 12:04:29',1),(89,'11','656554',378,'2018-05-21 12:08:02','8e60f4e8-5cac-11e8-bddb-6045cb9a7117',119,'资料审查','罗文波',NULL,1),(90,'12','65465',378,'2018-05-21 12:08:18','97a6efcf-5cac-11e8-bddb-6045cb9a7117',119,'已与客户建立联系','罗文波',NULL,1),(91,'17','',378,'2018-05-21 12:08:34','a16244ff-5cac-11e8-bddb-6045cb9a7117',119,'勾选经营范围','罗文波',NULL,1),(92,'16','156156',378,'2018-05-21 12:08:57','af452c1c-5cac-11e8-bddb-6045cb9a7117',119,'领取核名','罗文波',NULL,1),(93,'17','2',378,'2018-05-21 12:09:08','b58cb07d-5cac-11e8-bddb-6045cb9a7117',119,'勾选经营范围','罗文波',NULL,1),(95,'85','124',411,'2018-05-22 09:52:10','bda31af5-5d62-11e8-bddb-6045cb9a7117',97,'异常','庄培润','2018-05-22 09:52:25',7);
/*!40000 ALTER TABLE `t_projects_state_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:33
