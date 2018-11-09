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
-- Table structure for table `t_projects_milepost`
--

DROP TABLE IF EXISTS `t_projects_milepost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_milepost` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL DEFAULT '0',
  `is_lock` tinyint(1) NOT NULL DEFAULT '0',
  `confirm_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  `guid` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `remark` varchar(2000) DEFAULT NULL,
  `type_name` varchar(255) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `btype_name` varchar(255) DEFAULT NULL,
  `btype_id` int(11) DEFAULT NULL,
  `order_int` int(11) NOT NULL DEFAULT '0',
  `member_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=176 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_milepost`
--

LOCK TABLES `t_projects_milepost` WRITE;
/*!40000 ALTER TABLE `t_projects_milepost` DISABLE KEYS */;
INSERT INTO `t_projects_milepost` VALUES (57,365,0,'2018-05-28 08:55:20',106,'陈小银','75a5663f-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'办结',136,'公司注册',141,2,1244),(58,365,0,'2018-05-28 08:55:25',106,'陈小银','75a56a83-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'交接',137,'公司注册',141,6,1244),(59,365,0,'2018-05-28 08:55:22',106,'陈小银','75a59a1a-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'告知交接',138,'公司注册',141,3,1244),(60,365,0,'2018-05-28 08:55:24',106,'陈小银','75a59c53-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'完成交接',139,'公司注册',141,5,1244),(61,365,0,'2018-05-28 08:55:26',106,'陈小银','75a59d72-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'确认完成交接',140,'公司注册',141,7,1244),(62,365,0,'2018-05-28 08:55:19',106,'陈小银','75a59ed4-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'工商专员接单',149,'公司注册',141,1,1244),(63,365,0,'2018-05-28 08:55:23',106,'陈小银','75a59fbb-6254-11e8-b807-6045cb9a7117','2018-05-28 08:52:32','2018-05-28 08:52:32',NULL,'接受交接',150,'公司注册',141,4,1244),(99,414,0,NULL,137,'钟明霞','caaf750e-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'工商办结',136,'商标',145,2,1250),(100,414,0,NULL,137,'钟明霞','caaf79e4-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'仓管告知交接',138,'商标',145,3,1250),(101,414,0,NULL,137,'钟明霞','caaf7b60-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'完成与客户交接',139,'商标',145,5,1250),(102,414,0,NULL,137,'钟明霞','caaf7c6a-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'确认完成客户交接',140,'商标',145,6,1250),(103,414,0,NULL,137,'钟明霞','caaf8244-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'工商专员接单',149,'商标',145,1,1250),(104,414,0,NULL,137,'钟明霞','caaf838d-6314-11e8-b807-6045cb9a7117','2018-05-29 07:49:18','2018-05-29 07:49:18',NULL,'销售顾问接受交接',150,'商标',145,4,1250),(134,418,0,'2018-05-29 10:07:40',106,'陈小银','0ec15097-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'工商办结',136,'商标',145,2,1255),(135,418,0,'2018-05-29 10:16:29',153,'江嘉琳','0ec16286-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'仓管告知交接',138,'商标',145,4,1255),(136,418,0,'2018-05-29 10:49:13',123,'何家辉','0ec16453-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'完成与客户交接',139,'商标',145,6,1255),(137,418,0,NULL,106,'陈小银','0ec16575-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'确认完成客户交接',140,'商标',145,7,1255),(138,418,0,'2018-05-29 10:07:37',106,'陈小银','0ec16772-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'工商专员接单',149,'商标',145,1,1255),(139,418,0,'2018-05-29 10:20:40',123,'何家辉','0ec1687b-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'销售顾问接受交接',150,'商标',145,5,1255),(140,418,0,'2018-05-29 10:08:12',106,'陈小银','0ec16981-6328-11e8-b807-6045cb9a7117','2018-05-29 10:07:13','2018-05-29 10:07:13',NULL,'工商办结公司信息更新',152,'商标',145,3,1255),(141,418,0,'2018-05-29 10:39:20',106,'陈小银','8ceb9059-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'工商办结',136,'公司注销',144,2,1256),(142,418,0,'2018-05-29 10:49:04',153,'江嘉琳','8ceb935f-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'仓管告知交接',138,'公司注销',144,4,1256),(143,418,0,'2018-05-30 01:06:17',123,'何家辉','8ceb941c-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'完成与客户交接',139,'公司注销',144,6,1256),(144,418,0,NULL,106,'陈小银','8ceb94a7-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'确认完成客户交接',140,'公司注销',144,7,1256),(145,418,0,'2018-05-29 10:30:55',106,'陈小银','8ceb9563-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'工商专员接单',149,'公司注销',144,1,1256),(146,418,0,'2018-05-30 01:07:27',123,'何家辉','8ceb9614-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03','aaaa','销售顾问接受交接',150,'公司注销',144,5,1256),(147,418,0,'2018-05-29 10:47:17',106,'陈小银','8ceb969c-632a-11e8-b807-6045cb9a7117','2018-05-29 10:25:03','2018-05-29 10:25:03',NULL,'工商办结公司信息更新',152,'公司注销',144,3,1256),(148,418,0,'2018-05-29 10:52:26',106,'陈小银','49b885ca-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'工商办结',136,'公司注销',144,2,1257),(149,418,0,'2018-05-29 10:52:50',153,'江嘉琳','49b88971-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'仓管告知交接',138,'公司注销',144,4,1257),(150,418,0,NULL,106,'陈小银','49b88a8e-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'完成与客户交接',139,'公司注销',144,6,1257),(151,418,0,NULL,106,'陈小银','49b88bc7-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'确认完成客户交接',140,'公司注销',144,7,1257),(152,418,0,'2018-05-29 10:52:24',106,'陈小银','49b88cc3-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'工商专员接单',149,'公司注销',144,1,1257),(153,418,0,NULL,106,'陈小银','49b88e14-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'销售顾问接受交接',150,'公司注销',144,5,1257),(154,418,0,'2018-05-29 10:52:31',106,'陈小银','49b88f69-632e-11e8-b807-6045cb9a7117','2018-05-29 10:51:49','2018-05-29 10:51:49',NULL,'工商办结公司信息更新',152,'公司注销',144,3,1257),(155,417,0,'2018-05-30 07:05:14',106,'陈小银','ae5d4ea7-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'工商办结',136,'公司注册',141,2,1258),(156,417,0,'2018-05-30 07:08:36',153,'江嘉琳','ae5d5ffa-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'仓管告知交接',138,'公司注册',141,4,1258),(157,417,0,'2018-05-30 07:10:23',123,'何家辉','ae5d618c-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'完成与客户交接',139,'公司注册',141,6,1258),(158,417,0,NULL,106,'陈小银','ae5d62b8-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'确认完成客户交接',140,'公司注册',141,7,1258),(159,417,0,'2018-05-30 07:05:07',106,'陈小银','ae5d643d-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'工商专员接单',149,'公司注册',141,1,1258),(160,417,0,'2018-05-30 07:09:46',123,'何家辉','ae5d65b3-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'销售顾问接受交接',150,'公司注册',141,5,1258),(161,417,0,'2018-05-30 07:06:04',106,'陈小银','ae5d66bc-63d7-11e8-b807-6045cb9a7117','2018-05-30 07:04:22','2018-05-30 07:04:22',NULL,'工商办结公司信息更新',152,'公司注册',141,3,1258),(162,415,0,'2018-05-30 11:03:20',106,'陈小银','03a853be-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'工商办结',136,'公司注册',141,2,1259),(163,415,0,'2018-05-30 11:32:46',153,'江嘉琳','03a885a9-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'仓管告知交接',138,'公司注册',141,4,1259),(164,415,0,NULL,106,'陈小银','03a88799-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'完成与客户交接',139,'公司注册',141,6,1259),(165,415,0,NULL,106,'陈小银','03a888aa-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'确认完成客户交接',140,'公司注册',141,7,1259),(166,415,0,'2018-05-30 11:03:17',106,'陈小银','03a88a19-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'工商专员接单',149,'公司注册',141,1,1259),(167,415,0,NULL,106,'陈小银','03a88b15-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'销售顾问接受交接',150,'公司注册',141,5,1259),(168,415,0,'2018-05-30 11:05:15',106,'陈小银','03a88c70-63f9-11e8-b807-6045cb9a7117','2018-05-30 11:02:59','2018-05-30 11:02:59',NULL,'工商办结公司信息更新',152,'公司注册',141,3,1259),(169,419,0,'2018-05-31 03:14:14',106,'陈小银','96c3d2ac-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'工商办结',136,'公司注册',141,2,1267),(170,419,0,'2018-05-31 03:16:15',153,'江嘉琳','96c40343-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'仓管告知交接',138,'公司注册',141,4,1267),(171,419,0,NULL,106,'陈小银','96c40544-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'完成与客户交接',139,'公司注册',141,6,1267),(172,419,0,NULL,106,'陈小银','96c4067e-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'确认完成客户交接',140,'公司注册',141,7,1267),(173,419,0,'2018-05-31 03:14:08',106,'陈小银','96c4081d-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'工商专员接单',149,'公司注册',141,1,1267),(174,419,0,NULL,106,'陈小银','96c4093a-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'销售顾问接受交接',150,'公司注册',141,5,1267),(175,419,0,'2018-05-31 03:14:56',106,'陈小银','96c40a61-6480-11e8-b807-6045cb9a7117','2018-05-31 03:13:28','2018-05-31 03:13:28',NULL,'工商办结公司信息更新',152,'公司注册',141,3,1267);
/*!40000 ALTER TABLE `t_projects_milepost` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:34