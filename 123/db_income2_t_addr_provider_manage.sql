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
-- Table structure for table `t_addr_provider_manage`
--

DROP TABLE IF EXISTS `t_addr_provider_manage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_addr_provider_manage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `area` varchar(45) DEFAULT NULL,
  `addr_type` varchar(45) DEFAULT NULL,
  `provider` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `remark` varchar(100) DEFAULT '',
  `proivde_end` varchar(500) DEFAULT '',
  `updated_at` datetime DEFAULT NULL,
  `danbao_matter` varchar(500) DEFAULT '',
  `fp_limit` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_addr_provider_manage`
--

LOCK TABLES `t_addr_provider_manage` WRITE;
/*!40000 ALTER TABLE `t_addr_provider_manage` DISABLE KEYS */;
INSERT INTO `t_addr_provider_manage` VALUES (17,'天河','小规模孵化器开票','孵客','2018-08-07 08:12:56',118,'冯恒敏','接科技企业为主','',NULL,'付费期内工商税务保正常，出现异常解决不了退回剩余未使用月份费用','每月5万'),(18,'天河','非孵化器开票地址','老邱','2018-08-07 08:23:50',118,'冯恒敏','新注册3500，变更3500，变更加解锁4000。第二年续费3800','',NULL,'付费期内工商税务保正常，出现异常解决不了退回剩余未使用月份费用','没有上下限');
/*!40000 ALTER TABLE `t_addr_provider_manage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:12
