-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_income2
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
-- Table structure for table `business_develop_tag`
--

DROP TABLE IF EXISTS `business_develop_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `business_develop_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(45) DEFAULT NULL,
  `tag_category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=129 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `business_develop_tag`
--

LOCK TABLES `business_develop_tag` WRITE;
/*!40000 ALTER TABLE `business_develop_tag` DISABLE KEYS */;
INSERT INTO `business_develop_tag` VALUES (1,'在线咨询','渠道 (前端)'),(2,'直拨电话','渠道 (前端)'),(3,'SEO','渠道 (前端)'),(4,'传统渠道商机','渠道 (前端)'),(5,'客户自身业务','渠道 (前端)'),(6,'客户介绍客户','渠道 (前端)'),(7,'销售主动开发','渠道 (前端)'),(8,'员工介绍朋友','渠道 (前端)'),(9,'楼盘客介绍客','渠道 (前端)'),(10,'咨询注册','咨询 (前端)'),(11,'咨询记账','咨询 (前端)'),(12,'咨询变更','咨询 (前端)'),(13,'咨询注销','咨询 (前端)'),(14,'咨询商标','咨询 (前端)'),(15,'咨询个体户','咨询 (前端)'),(16,'咨询买卖公司','咨询 (前端)'),(17,'咨询香港公司','咨询 (前端)'),(18,'公司起名','咨询 (前端)'),(19,'咨询外资','咨询 (前端)'),(20,'咨询食品证','咨询 (前端)'),(21,'咨询进出口权','咨询 (前端)'),(22,'咨询许可证','咨询 (前端)'),(23,'咨询入户','咨询 (前端)'),(24,'咨询装修','咨询 (前端)'),(25,'优质商机','质量 (前端)'),(26,'普通商机','质量 (前端)'),(27,'会计部','反馈部门'),(28,'工商部','反馈部门'),(29,'销售部','反馈部门'),(30,'内部反馈成交','反馈 (业务)'),(31,'已成交','跟进 (业务)'),(32,'到访后考虑中','跟进 (业务)'),(33,'到访后可放弃','跟进 (业务)'),(34,'到访时间已约','跟进 (业务)'),(35,'重点跟进中','跟进 (业务)'),(36,'方案未确定','跟进 (业务)'),(37,'对比价格中','跟进 (业务)'),(38,'股东商量中','跟进 (业务)'),(39,'本月内确定','跟进 (业务)'),(40,'一周内确定','跟进 (业务)'),(41,'三天内确定','跟进 (业务)'),(42,'意向变弱','跟进 (业务)'),(43,'暂时拒绝','跟进 (业务)'),(44,'不接电话','跟进 (业务)'),(45,'后续可跟进','跟进 (业务)'),(46,'资料有误','跟进 (业务)'),(47,'已流失同行','跟进 (业务)'),(48,'需求注册','需求 (业务)'),(49,'需求记账','需求 (业务)'),(50,'需求变更','需求 (业务)'),(51,'需求注销','需求 (业务)'),(52,'需求商标','需求 (业务)'),(53,'需求个体户','需求 (业务)'),(54,'需求买卖公司','需求 (业务)'),(55,'需求香港公司','需求 (业务)'),(56,'需求外资','需求 (业务)'),(57,'需求食品证','需求 (业务)'),(58,'餐饮许可证','需求 (业务)'),(59,'进出口许可证','需求 (业务)'),(60,'其他许可证件','需求 (业务)'),(61,'需求入户','需求 (业务)'),(62,'需求装修','需求 (业务)'),(63,'高质量A类','质量 (业务)'),(64,'高质量B1类','质量 (业务)'),(65,'中质量B2类','质量 (业务)'),(66,'低质量C1类','质量 (业务)'),(67,'低质量C2类','质量 (业务)'),(68,'同行','质量 (业务)'),(69,'无效业务咨询','质量 (业务)'),(70,'没咨询过我司','质量 (业务)'),(71,'办理自有地址','成交 (业务)'),(72,'办理虚拟地址','成交 (业务)'),(73,'办理开票地址','成交 (业务)'),(74,'办纳税人地址','成交 (业务)'),(75,'办理记账','成交 (业务)'),(76,'办理商标','成交 (业务)'),(77,'升一般纳税人','成交 (业务)'),(78,'办理变更','成交 (业务)'),(79,'办理注销','成交 (业务)'),(80,'办理入户','成交 (业务)'),(81,'办理香港公司','成交 (业务)'),(82,'办理食品证','成交 (业务)'),(83,'办理进出口','成交 (业务)'),(84,'办理个体户','成交 (业务)'),(85,'办理转让公司','成交 (业务)'),(86,'办理转让商标','成交 (业务)'),(87,'办理装修','成交 (业务)'),(88,'已签记帐','签账 (业务)'),(89,'待签记账','签账 (业务)'),(90,'确定不签记账','签账 (业务)'),(91,'预计核名','进度 (工商)'),(92,'地址安排','进度 (工商)'),(93,'执照受理','进度 (工商)'),(94,'领取执照','进度 (工商)'),(95,'刻章备案','进度 (工商)'),(96,'办结客户','进度 (工商)'),(97,'待定办理','进度 (工商)'),(98,'变更办理中','进度 (工商)'),(99,'跨区变更中','进度 (工商)'),(100,'变更资料不齐','进度 (工商)'),(101,'变更待领执照','进度 (工商)'),(102,'注销登记备案','进度 (工商)'),(103,'已注销登报','进度 (工商)'),(104,'注销资料不齐','进度 (工商)'),(105,'食品证办理中','进度 (工商)'),(106,'进出口办理中','进度 (工商)'),(107,'食品证已结办','进度 (工商)'),(108,'进出口已结办','进度 (工商)'),(109,'其他','进度 (工商)'),(110,'老总关系客','质量 (会计)'),(111,'A类优质客户','质量 (会计)'),(112,'B类中质量客','质量 (会计)'),(113,'C1类低质量客','质量 (会计)'),(114,'C2类常拖款客','质量 (会计)'),(115,'C3类严重欠款','质量 (会计)'),(116,'自有地址','地址  (会计)'),(117,'虚拟地址','地址  (会计)'),(118,'开票地址','地址  (会计)'),(119,'孵化器地址','地址  (会计)'),(120,'纳税人地址','地址  (会计)'),(121,'南沙地址','地址  (会计)'),(122,'小规模企业','类型 (会计)'),(123,'一般纳税人','类型 (会计)'),(124,'注销中','状态  (会计)'),(125,'已解约','状态  (会计)'),(126,'非记账','状态  (会计)'),(127,'已停帐','状态  (会计)'),(128,'注销完毕','状态  (会计)');
/*!40000 ALTER TABLE `business_develop_tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:33:13