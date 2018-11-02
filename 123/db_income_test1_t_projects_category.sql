-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income_test1
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
-- Table structure for table `t_projects_category`
--

DROP TABLE IF EXISTS `t_projects_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_category` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `category_name` varchar(255) NOT NULL DEFAULT '',
  `uid` int(11) DEFAULT NULL,
  `is_hide` tinyint(4) NOT NULL DEFAULT '0',
  `parent_id` int(11) NOT NULL DEFAULT '0',
  `order_int` int(11) NOT NULL DEFAULT '0',
  `role` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=185 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_category`
--

LOCK TABLES `t_projects_category` WRITE;
/*!40000 ALTER TABLE `t_projects_category` DISABLE KEYS */;
INSERT INTO `t_projects_category` VALUES (23,'办理中',154,0,0,0,1),(24,'已办结',154,0,0,0,1),(25,'已交接',154,0,0,0,1),(30,'办理中',154,0,0,0,5),(31,'已办结',154,0,0,0,5),(32,'已交接',154,0,0,0,5),(33,'办理中',154,0,0,0,9),(34,'已办结',154,0,0,0,9),(35,'已交接',154,0,0,0,9),(36,'同区变更',141,0,0,0,NULL),(38,'变更',139,0,0,1,NULL),(39,'跨区变更',139,0,0,2,NULL),(40,'食品证',139,0,0,3,NULL),(41,'进出口',139,0,0,4,NULL),(42,'清算备案',139,0,0,7,NULL),(43,'注销国地税已转会计',139,0,0,8,NULL),(44,'注销执照',139,0,0,9,NULL),(45,'待领执照',139,0,0,5,NULL),(46,'没收到变更资料（同区）',140,0,0,1,NULL),(48,'地址续期',140,0,0,7,NULL),(49,'跨区变更受理',141,0,0,0,NULL),(54,'旧',138,0,0,0,NULL),(57,'问题客户',136,0,0,2,NULL),(60,'变更办理中',140,0,0,3,NULL),(61,'预计核名',106,0,0,1,NULL),(62,'领取核名',106,0,0,2,NULL),(63,'地址安排',106,0,0,3,NULL),(64,'执照受理',106,0,0,4,NULL),(65,'领取执照',106,0,0,5,NULL),(66,'刻章安排',106,0,0,6,NULL),(67,'银行开户',106,0,0,7,NULL),(68,'特殊客户',106,0,0,8,NULL),(69,'其他',106,0,0,9,NULL),(70,'食品证',140,0,0,8,NULL),(76,'预计核名',137,0,0,0,NULL),(77,'领取核名',137,0,0,0,NULL),(78,'地址安排',137,0,0,0,NULL),(79,'执照受理',137,0,0,0,NULL),(80,'领取执照',137,0,0,0,NULL),(81,'刻章备案',137,0,0,0,NULL),(82,'银行开户',137,0,0,0,NULL),(85,'注销',138,0,0,0,NULL),(86,'没收到注销资料',140,0,0,2,NULL),(87,'注销',140,0,0,5,NULL),(88,'注销国地税中',140,0,0,6,NULL),(89,'跨区变更',140,0,0,4,NULL),(90,'还没交接',153,0,0,0,NULL),(93,'还没收齐尾款。',153,0,0,0,NULL),(98,'流转工商办理。',153,0,0,0,NULL),(99,'已完成',153,0,0,0,NULL),(105,'解除异常',139,0,0,6,NULL),(107,'注销国地税',138,0,0,0,NULL),(108,'注销执照',138,0,0,0,NULL),(113,'1 清算有资料',239,0,0,1,NULL),(114,'2 未约号有资料',239,0,0,2,NULL),(115,'3 注销国地税',239,0,0,3,NULL),(116,'4 注销执照',239,0,0,4,NULL),(117,'没有上传交接单。',153,0,0,0,NULL),(118,'1.预计核名',269,0,0,1,NULL),(119,'2.领取核名',269,0,0,2,NULL),(120,'3.地址安排',269,0,0,3,NULL),(121,'4.执照受理',269,0,0,4,NULL),(122,'5.领取执照',269,0,0,5,NULL),(124,'6.刻章备案',269,0,0,6,NULL),(125,'8.办结客户',269,0,0,8,NULL),(126,'7.银行开户',269,0,0,7,NULL),(127,'尾款待结算',116,0,0,0,NULL),(128,'快递资料',116,0,0,0,NULL),(129,'进出口权',140,0,0,9,NULL),(130,'9.取消客户',269,0,0,9,NULL),(131,'可以办的',136,0,0,0,NULL),(132,'食品证',141,0,0,0,NULL),(133,'旧注销银行',138,0,0,0,NULL),(134,'进出口',141,0,0,0,NULL),(135,'旧注销国地税',138,0,0,0,NULL),(136,'没收到变更资料（跨区）',140,0,0,0,NULL),(137,'待办',140,0,0,10,NULL),(138,'等资料',268,0,0,0,NULL),(139,'受理中',268,0,0,0,NULL),(140,'待受理',268,0,0,0,NULL),(141,'注销资料不齐',141,0,0,0,NULL),(142,'执照受理中',136,0,0,0,NULL),(143,'变更',138,0,0,0,NULL),(145,'注销银行',139,0,0,10,NULL),(146,'待处理客户',139,0,0,11,NULL),(148,'旧变更',138,0,0,0,NULL),(149,'注销国地税',141,0,0,0,NULL),(150,'注销执照、银行',141,0,0,0,NULL),(151,'公司',239,0,0,5,NULL),(152,'0无资料',239,0,0,0,NULL),(153,'解除异常',141,0,0,0,NULL),(158,'出地址',268,0,0,0,NULL),(159,'已经发起协助',136,0,0,0,NULL),(160,'待定客户',137,0,0,0,NULL),(161,'整理资料',268,0,0,0,NULL),(163,'执照办理中',296,0,0,0,NULL),(164,'可以办理',296,0,0,0,NULL),(165,'已经发起协助的问题客户',296,0,0,0,NULL),(166,'暂时不办理客户',296,0,0,0,NULL),(167,'已发起协助',139,0,0,12,NULL),(168,'在办外接',210,0,0,0,NULL),(173,'在办内接',210,0,0,0,NULL),(174,'停办',210,0,0,0,NULL),(175,'待办内接',210,0,0,0,NULL),(178,'待办外接',210,0,0,0,NULL),(180,'提交受理注销资料成功',210,0,0,0,NULL),(183,'跨区变更',138,0,0,0,NULL),(184,'123',155,0,0,0,NULL);
/*!40000 ALTER TABLE `t_projects_category` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:22:50
