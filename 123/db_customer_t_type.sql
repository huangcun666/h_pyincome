-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_customer
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_type`
--

LOCK TABLES `t_type` WRITE;
/*!40000 ALTER TABLE `t_type` DISABLE KEYS */;
INSERT INTO `t_type` VALUES (1,'A','信用评级',NULL),(2,'B','信用评级',NULL),(3,'M','信用评级',NULL),(4,'C','信用评级',NULL),(5,'D','信用评级',NULL),(6,'国税','网站类型',NULL),(7,'地税','网站类型',NULL),(8,'实名','网站类型',NULL),(9,'其他','网站类型',NULL),(16,'优质','客户等级',NULL),(17,'待评','客户等级',NULL),(19,'记账','客户类型',0),(20,'楼盘','客户类型',0),(21,'客服会计','角色',0),(22,'账务主管','角色',0),(23,'会计一部','会计一部',0),(24,'会计二部','会计二部',0),(25,'会计三部','会计三部',0),(26,'会计四部','会计四部',0),(27,'会计五部','会计五部',0),(28,'广州市','地市',0),(29,'天河','区域',0),(30,'越秀','区域',0),(31,'海珠','区域',0),(32,'荔湾','区域',0),(33,'番禺','区域',0),(34,'南沙','区域',0),(35,'增城','区域',0),(36,'黄埔','区域',0),(37,'白云','区域',0),(39,'萝岗','区域',0),(40,'解约','客户类型',0),(41,'注销','客户类型',0),(42,'入户','客户类型',0),(43,'停账','客户类型',0),(44,'汇算清缴','客户类型',0),(45,'工商年检','客户类型',0),(46,'花都','区域',0),(47,'年付','付费方式',0),(48,'半年付','付费方式',0),(49,'季付','付费方式',0),(50,'月付','付费方式',0);
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

-- Dump completed on 2018-11-02 16:22:42
