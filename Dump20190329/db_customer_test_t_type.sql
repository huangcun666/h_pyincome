-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer_test
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
-- Table structure for table `t_type`
--

DROP TABLE IF EXISTS `t_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  `fee` int(4) NOT NULL DEFAULT '0',
  `is_show` int(4) NOT NULL DEFAULT '0',
  `order_int` int(11) NOT NULL DEFAULT '0',
  `parent_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_type`
--

LOCK TABLES `t_type` WRITE;
/*!40000 ALTER TABLE `t_type` DISABLE KEYS */;
INSERT INTO `t_type` VALUES (1,'A','信用评级',NULL,0,0,0,0),(2,'B','信用评级',NULL,0,0,0,0),(3,'M','信用评级',NULL,0,0,0,0),(4,'C','信用评级',NULL,0,0,0,0),(5,'D','信用评级',NULL,0,0,0,0),(6,'国税','网站类型',NULL,0,0,0,0),(7,'地税','网站类型',NULL,0,0,0,0),(8,'实名','网站类型',NULL,0,0,0,0),(9,'其他','网站类型',NULL,0,0,0,0),(16,'优质','客户等级',NULL,0,0,0,0),(17,'待评','客户等级',NULL,0,0,0,0),(19,'记账','客户类型',0,0,1,0,0),(20,'楼盘','客户类型',0,0,1,0,0),(21,'客服会计','角色',0,0,0,0,0),(22,'账务主管','角色',0,0,0,0,0),(23,'会计一部','会计一部',0,0,0,0,0),(24,'会计二部','会计二部',0,0,0,0,0),(25,'会计三部','会计三部',0,0,0,0,0),(26,'会计四部','会计四部',0,0,0,0,0),(27,'会计五部','会计五部',0,0,0,0,0),(28,'广州市','地市',0,0,0,0,0),(29,'天河','区域',0,0,0,0,0),(30,'越秀','区域',0,0,0,0,0),(31,'海珠','区域',0,0,0,0,0),(32,'荔湾','区域',0,0,0,0,0),(33,'番禺','区域',0,0,0,0,0),(34,'南沙','区域',0,0,0,0,0),(35,'增城','区域',0,0,0,0,0),(36,'黄埔','区域',0,0,0,0,0),(37,'白云','区域',0,0,0,0,0),(39,'萝岗','区域',0,0,0,0,0),(40,'解约','客户类型',0,0,1,0,0),(41,'注销','客户类型',0,0,1,0,0),(42,'入户','客户类型',0,0,1,0,0),(43,'停账','客户类型',0,0,1,0,0),(44,'汇算清缴','客户类型',0,0,1,0,0),(45,'工商年检','客户类型',0,0,1,0,0),(46,'花都','区域',0,0,0,0,0),(47,'年付','付费方式',0,12,0,0,0),(48,'半年付','付费方式',0,6,0,0,0),(49,'季付','付费方式',0,3,0,0,0),(50,'月付','付费方式',0,1,0,0,0),(51,'无','付费方式',0,0,0,0,0),(52,'正常','付费方式标记',0,0,0,0,0),(53,'注销中','付费方式标记',0,0,0,0,0),(54,'逾期','付费方式标记',0,0,0,0,0),(55,'停账','付费方式标记',0,0,0,0,0),(56,'归入发业','付费方式标记',0,0,0,0,0),(57,'两月一付','付费方式',0,2,0,0,0),(58,'解约','付费方式标记',0,0,0,0,0),(59,'逾期','客户类型',0,0,1,0,0),(60,'取消','客户类型',0,0,1,0,0),(61,'指导价','汇算流程',1,0,1,1,0),(62,'分配跟进','汇算流程',2,0,1,2,0),(63,'跟进处理','汇算流程',3,0,1,3,0),(64,'分配负责人审核','汇算流程',4,0,1,4,0),(65,'财务核对','汇算流程',5,0,1,5,0),(66,'汇算处理中','汇算流程',6,0,1,6,0),(67,'汇算审核','汇算流程',7,0,1,7,0),(68,'年检办理中','汇算流程',8,0,1,8,0),(69,'年检审核','汇算流程1',9,0,1,9,0),(71,'汇算','2018',9,0,1,1,0),(72,'年检','2018',9,0,2,2,0),(81,'无需处理','汇算流程1',9,0,1,10,0),(82,'年检','订购服务',0,0,0,1,0),(83,'汇算清缴','订购服务',0,0,0,2,0),(84,'发票','订购服务',0,0,0,3,0),(85,'正常','客户类型',0,0,1,1,0),(86,'坏账','客户类型',0,0,1,0,0),(87,'记账','客户标签1',1,0,1,1,0),(88,'非记账','客户标签1',2,0,1,2,0),(89,'正常','客户标签',1,0,1,1,1),(90,'停帐','客户标签',1,0,1,2,1),(91,'逾期','客户标签',1,0,1,3,1),(92,'坏账','客户标签',1,0,1,4,1),(93,'楼盘','客户标签',1,0,0,5,1),(94,'解约','客户标签',1,0,1,6,1),(95,'注销','客户标签',1,0,1,7,1),(96,'取消','客户标签',1,0,1,8,1),(97,'工商年检','客户标签',1,0,0,9,0),(98,'汇算清缴','客户标签',1,0,0,10,0),(99,'非记账','客户标签',1,10,0,11,2);
/*!40000 ALTER TABLE `t_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:08
