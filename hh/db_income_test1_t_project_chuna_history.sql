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
-- Table structure for table `t_project_chuna_history`
--

DROP TABLE IF EXISTS `t_project_chuna_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_project_chuna_history` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `company` varchar(255) DEFAULT '',
  `customer_name` varchar(255) DEFAULT '',
  `customer_tel` varchar(255) DEFAULT '',
  `project_name` varchar(255) DEFAULT '',
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_project_chuna_history`
--

LOCK TABLES `t_project_chuna_history` WRITE;
/*!40000 ALTER TABLE `t_project_chuna_history` DISABLE KEYS */;
INSERT INTO `t_project_chuna_history` VALUES (8,2538,'333|5444|','底大杠12|底大杠|底大杠2|','12345|123456789|','比比匕薄123456|比比匕薄|',96,'谢妙欣','2018-10-30 10:35:51'),(9,2524,'广州市泰紫阁贸易有限公司|广州市泰紫阁贸易有限公司1||123|空|','1|12|翁一岚A|翁一岚B|','|1234567||','123|123567|1|',96,'谢妙欣','2018-10-30 14:36:16'),(10,2527,'为为为为试试|为为为为试试1|test|','aaaa|aaaa00000|','|','sss|',96,'谢妙欣','2018-10-30 16:13:08'),(11,2581,'广东福之岛贸易有限公司|','X先生|X先生111|','|123123|123123热吻任务二|','2018-12至2019-11(年付)记账费:2700.00元 2018-12至2019-11(年付)账册费:300.00元|',237,'黄柳如','2018-10-30 12:04:26'),(12,2582,'广州市冰芯蝶化妆品有限公司|广州市冰芯蝶化妆品有限公司1|广州市冰芯蝶化妆品有限公司|广州市冰芯蝶化妆品有限公司1|广州市冰芯蝶化妆品有限公司|','冰芯|','|','2018-11至2019-10(年付)记账费:2760.00元 2018-11至2019-10(年付)账册费:300.00元|',116,'陈太智','2018-10-31 10:03:03'),(13,2576,'广州婀娜服饰有限公司|广州婀娜服饰有限公司1|','婀娜|','|','2018-08至2018-07(年付)账册费:300.00元|',116,'陈太智','2018-10-31 10:27:44');
/*!40000 ALTER TABLE `t_project_chuna_history` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:59
