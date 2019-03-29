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
-- Table structure for table `t_customer_genjin_msg`
--

DROP TABLE IF EXISTS `t_customer_genjin_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_genjin_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) NOT NULL,
  `file_path` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `msg` varchar(555) DEFAULT NULL,
  `genjin_type` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_genjin_msg`
--

LOCK TABLES `t_customer_genjin_msg` WRITE;
/*!40000 ALTER TABLE `t_customer_genjin_msg` DISABLE KEYS */;
INSERT INTO `t_customer_genjin_msg` VALUES (1,5154,NULL,'2019-03-28 16:14:36','陈太智',116,'21321',1),(2,5154,'/static/customer/genjin/5154/huancai_yishu.jpg_5154.jpg','2019-03-28 16:17:00','陈太智',116,'1232133',1),(3,5157,'/static/customer/genjin/5157/2019-01-02 09-13-19 的屏幕截图.png_5157.png','2019-03-28 16:34:37','陈太智',116,'66666',1),(4,1163,'/static/customer/genjin/1163/2019-01-02 09-13-19 的屏幕截图.png_1163.png','2019-03-28 16:42:35','陈太智',116,'123',1),(5,5156,NULL,'2019-03-28 16:43:03','陈太智',116,'123213',1),(6,5156,NULL,'2019-03-28 16:44:39','陈太智',116,'21321321321',2),(7,5156,'/static/customer/genjin/5156/huancai_yishu.jpg_5156.jpg','2019-03-28 16:45:11','陈太智',116,'7777777777777777777777777777777777777',3);
/*!40000 ALTER TABLE `t_customer_genjin_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:39:07
