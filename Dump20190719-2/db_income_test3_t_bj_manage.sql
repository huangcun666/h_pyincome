-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test3
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
-- Table structure for table `t_bj_manage`
--

DROP TABLE IF EXISTS `t_bj_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_bj_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(45) DEFAULT '',
  `project_type` varchar(45) DEFAULT '',
  `invoice_limited` varchar(500) DEFAULT NULL,
  `note` varchar(500) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `is_kp_addr` tinyint(4) NOT NULL DEFAULT '1',
  `is_fhq` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_bj_manage`
--

LOCK TABLES `t_bj_manage` WRITE;
/*!40000 ALTER TABLE `t_bj_manage` DISABLE KEYS */;
INSERT INTO `t_bj_manage` VALUES (39,'天河','虚拟地址','不能开发票','天河区龙怡路.经营范围只能选五类，互联网商品批发（许可审批类除外）、互联网商品零售（许可审批类除外）、软件和信息技术服务业、研究和试验发展、科技推广和应用服务业、文艺创作。',118,'2018-07-17 02:40:55','2018-08-11 07:27:46','冯恒敏',0,1),(40,'天河','天河北小规模孵化器开票地址（不可解锁税务）','5万一个月','科技公司为主。瀚景路1号。',118,'2018-07-17 07:06:42','2018-09-11 07:08:47','冯恒敏',1,1),(41,'天河','黄村小规模开票地址(可以解锁工商税务）','每月20万以内','荔苑路18号，黄村北路26号A区、B区，黄村路57号，黄村路自编8号。中山大道989号。共5个地址可以解除工商税务异常。沙浦大街323号产权，元岗锁。',118,'2018-07-18 01:27:44','2018-10-24 05:51:17','冯恒敏',1,1),(42,'天河','珠江新城小规模开票地址','每月30万以内','只接新注册，绑定做账.珠江东路',118,'2018-07-18 01:29:07','2018-09-11 01:37:45','冯恒敏',1,1),(43,'天河','黄村一般纳税人非孵化器地址','一个月50万以内','可做厂房使用荔苑路18号，黄村北路26号A区、B区，黄村路57号，黄村路自编8号。共四个地址可以解除工商税务异常。实际办公8400一年',118,'2018-07-18 01:30:03','2018-09-11 07:09:03','冯恒敏',1,1),(44,'天河','珠江新城一般纳税人开票地址','50万以内每月','绑定记账',118,'2018-07-18 01:30:56',NULL,'冯恒敏',1,1),(45,'天河','小规模珠江新城预包装食品证开票地址','30万以内每月','只能办理预包装',118,'2018-07-18 01:32:22',NULL,'冯恒敏',1,1),(46,'天河','珠江新城一般纳税人预包装食品证开票地址','每月50万以内','',118,'2018-07-18 01:33:14','2018-09-11 01:41:59','冯恒敏',1,1),(47,'越秀','虚拟地址','不能开发票','',118,'2018-07-18 01:35:06','2018-08-09 01:56:13','冯恒敏',0,1),(48,'越秀','小规模孵化器开票地址','10万每个月','',118,'2018-07-18 01:37:17',NULL,'冯恒敏',1,1),(49,'越秀','越秀一般纳税人开票地址','30万每月','',118,'2018-07-18 01:37:57',NULL,'冯恒敏',1,1),(50,'番禺','小规模孵化器开票地址','10万每月','不接变更，科技公司',118,'2018-07-18 01:38:57','2018-08-06 01:46:11','冯恒敏',1,1),(51,'番禺','番禺预包装食品证开票地址','10万每月','预包装食品经营许可证',118,'2018-07-18 01:39:57','2018-08-06 01:44:54','冯恒敏',1,1),(52,'越秀','越秀预包装食品证小规模开票地址','20万','',118,'2018-07-18 01:40:46',NULL,'冯恒敏',1,1),(53,'越秀','一般纳税人预包装食品证开票地址','20万每月','',118,'2018-07-18 01:41:24',NULL,'冯恒敏',1,1),(54,'天河','岑村小规模开票解锁地址','30','保工商税务一年，可以配合工商税务银行查看，可以提供卡位办公',118,'2018-09-11 07:13:46',NULL,'冯恒敏',1,0),(55,'天河','孵化器开票可续费地址','税局审批为准','地址：天河区龙怡路91号。税务异常不能接。除生产加工、参与服务、娱乐行业、网吧、药品、医疗器械、危险化学品、民用爆品、烟花爆竹、放射性物品、旅行社等行业除外。',118,'2018-10-23 07:04:39','2018-10-24 07:26:28','冯恒敏',1,1);
/*!40000 ALTER TABLE `t_bj_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:24
