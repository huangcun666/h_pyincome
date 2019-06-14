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
-- Table structure for table `t_trade_milepost_his`
--

DROP TABLE IF EXISTS `t_trade_milepost_his`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_trade_milepost_his` (
  `his_id` int(11) NOT NULL AUTO_INCREMENT,
  `his_order` int(11) NOT NULL DEFAULT '1',
  `his_name` varchar(255) DEFAULT NULL,
  `his_at` datetime DEFAULT NULL,
  `his_uid` int(11) DEFAULT NULL,
  `his_uid_name` varchar(255) DEFAULT NULL,
  `is_valid` tinyint(4) NOT NULL DEFAULT '0',
  `state_id` int(11) NOT NULL DEFAULT '0',
  `state_id_name` varchar(255) DEFAULT NULL,
  `state_id_remark` varchar(255) DEFAULT NULL,
  `trade_id` int(11) NOT NULL DEFAULT '0',
  `mile_id` int(11) NOT NULL DEFAULT '0',
  `his_remark` varchar(255) DEFAULT NULL,
  `state_id_at` datetime DEFAULT NULL,
  `state_uid` int(11) NOT NULL DEFAULT '0',
  `state_uid_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`his_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_trade_milepost_his`
--

LOCK TABLES `t_trade_milepost_his` WRITE;
/*!40000 ALTER TABLE `t_trade_milepost_his` DISABLE KEYS */;
INSERT INTO `t_trade_milepost_his` VALUES (1,1,'部分驳回','2019-06-11 18:12:54',116,'陈太智',0,0,NULL,NULL,18,78,NULL,NULL,0,NULL),(2,1,'部分驳回','2019-06-12 10:52:04',116,'陈太智',0,2,'部分驳回',NULL,19,85,'大大大',NULL,0,NULL),(3,2,'部分驳回','2019-06-12 12:01:21',116,'陈太智',0,2,'部分驳回',NULL,19,85,'',NULL,0,NULL),(4,3,'部分驳回','2019-06-12 13:39:19',116,'陈太智',0,1,'初审',NULL,19,85,'',NULL,0,NULL),(5,4,'部分驳回','2019-06-12 13:49:33',116,'陈太智',0,1,'初审',NULL,19,85,'',NULL,0,NULL),(6,1,'部分驳回','2019-06-12 13:51:54',116,'陈太智',0,2,'部分驳回',NULL,21,99,'',NULL,0,NULL),(7,2,'部分驳回','2019-06-12 13:52:37',116,'陈太智',0,1,'初审',NULL,21,99,'',NULL,0,NULL),(8,1,'部分驳回','2019-06-12 13:55:26',116,'陈太智',0,3,'全部驳回',NULL,22,106,'sdfsdfds','2019-06-12 13:55:45',0,NULL),(9,2,'全部驳回','2019-06-12 13:55:45',116,'陈太智',0,2,'部分驳回',NULL,22,106,'ssadfgdsf','2019-06-12 13:59:24',116,'陈太智'),(10,3,'部分驳回','2019-06-12 13:59:02',116,'陈太智',0,0,NULL,NULL,22,106,'',NULL,0,NULL),(11,4,'部分驳回','2019-06-12 13:59:10',116,'陈太智',0,0,NULL,NULL,22,106,'',NULL,0,NULL),(12,5,'部分驳回','2019-06-12 13:59:24',116,'陈太智',0,0,NULL,NULL,22,106,'',NULL,0,NULL),(13,1,'部分驳回','2019-06-12 13:59:48',116,'陈太智',0,2,'部分驳回',NULL,23,113,'fdssdf','2019-06-12 13:59:55',116,'陈太智'),(14,2,'部分驳回','2019-06-12 13:59:55',116,'陈太智',0,1,'初审',NULL,23,113,'dsdsd','2019-06-12 14:00:50',116,'陈太智'),(15,1,'部分驳回','2019-06-12 14:24:44',116,'陈太智',0,3,'全部驳回',NULL,24,120,'','2019-06-12 14:26:25',116,'陈太智'),(16,2,'全部驳回','2019-06-12 14:26:25',116,'陈太智',0,1,'初审',NULL,24,120,'','2019-06-12 14:27:10',116,'陈太智'),(17,1,'被异议','2019-06-12 14:40:14',116,'陈太智',0,2,'被异议',NULL,23,114,'ff','2019-06-12 14:43:42',116,'陈太智'),(18,2,'被异议','2019-06-12 14:43:42',116,'陈太智',0,1,'通过',NULL,23,114,'dddd','2019-06-12 14:46:09',116,'陈太智'),(19,1,'部分驳回','2019-06-12 15:37:17',116,'陈太智',0,1,'初审',NULL,26,134,'dd','2019-06-12 17:18:25',116,'陈太智'),(20,2,'初审','2019-06-12 17:18:25',116,'陈太智',0,2,'部分驳回',NULL,26,134,'ww','2019-06-12 17:18:48',116,'陈太智'),(21,3,'部分驳回','2019-06-12 17:18:48',116,'陈太智',0,1,'初审',NULL,26,134,'','2019-06-12 17:19:05',116,'陈太智'),(22,4,'初审','2019-06-12 17:19:05',116,'陈太智',0,1,'初审',NULL,26,134,'','2019-06-12 17:19:16',116,'陈太智'),(23,5,'初审','2019-06-12 17:19:16',116,'陈太智',0,1,'初审',NULL,26,134,'','2019-06-12 17:20:16',116,'陈太智'),(24,6,'初审','2019-06-12 17:20:16',116,'陈太智',0,1,'初审',NULL,26,134,'','2019-06-12 17:21:25',116,'陈太智'),(25,1,'被异议','2019-06-12 17:24:50',116,'陈太智',0,1,'通过',NULL,26,135,'','2019-06-12 17:25:21',116,'陈太智'),(26,1,'部分驳回','2019-06-13 14:46:30',116,'陈太智',0,0,NULL,NULL,31,169,'aaasaas',NULL,0,NULL),(27,2,'全部驳回','2019-06-13 14:48:49',116,'陈太智',0,0,NULL,NULL,31,169,'',NULL,0,NULL),(28,1,'部分驳回','2019-06-13 17:13:00',116,'陈太智',0,1,'初审',NULL,30,162,'fff','2019-06-13 17:18:05',116,'陈太智'),(29,1,'不受理','2019-06-13 18:55:16',116,'陈太智',0,0,NULL,NULL,32,175,'ww',NULL,0,NULL),(30,1,'部分驳回','2019-06-13 18:58:54',116,'陈太智',0,2,'部分驳回',NULL,33,183,'ss','2019-06-13 19:00:34',116,'陈太智'),(31,2,'部分驳回','2019-06-13 19:00:34',116,'陈太智',0,2,'部分驳回',NULL,33,183,'ddddddd','2019-06-13 19:00:58',116,'陈太智'),(32,3,'部分驳回','2019-06-13 19:00:58',116,'陈太智',0,1,'初审',NULL,33,183,'','2019-06-13 19:01:08',116,'陈太智');
/*!40000 ALTER TABLE `t_trade_milepost_his` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-14  9:06:41
