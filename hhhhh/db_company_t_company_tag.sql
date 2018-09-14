-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
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
-- Table structure for table `t_company_tag`
--

DROP TABLE IF EXISTS `t_company_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_company_tag` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `tag_name` varchar(255) DEFAULT NULL,
  `tag_category` varchar(255) DEFAULT NULL,
  `order_int` int(11) NOT NULL DEFAULT '0',
  `is_hide` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_company_tag`
--

LOCK TABLES `t_company_tag` WRITE;
/*!40000 ALTER TABLE `t_company_tag` DISABLE KEYS */;
INSERT INTO `t_company_tag` VALUES (1,'空号','状态',0,0),(2,'需求注册','需求',0,0),(3,'需求记账','需求',0,0),(4,'变更','需求',0,0),(5,'注销','需求',0,0),(6,'需求商标','需求',0,0),(7,'需求个体户','需求',0,0),(8,'需求买卖公司','需求',0,0),(9,'需求香港公司','需求',0,0),(10,'需求外资','需求',0,0),(11,'需求食品证','需求',0,0),(12,'餐饮许可证','需求',0,0),(13,'进出口许可证','需求',0,0),(14,'其他许可证件','需求',0,0),(15,'需求入户','需求',0,0),(16,'需求装修','需求',0,0),(17,'需求装修\n','需求',0,0),(18,'高质量A类','质量',0,0),(19,'中质量B1类','质量',0,0),(20,'中质量B2类','质量',0,0),(21,'低质量C1类','质量',0,0),(22,'低质量C2类','质量',0,0),(23,'同行','质量',0,0),(24,'无效业务咨询','质量',0,0),(25,'没咨询过我司','质量',0,0),(26,'待定','质量',0,0);
/*!40000 ALTER TABLE `t_company_tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-14 11:34:35
