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
-- Table structure for table `t_company_name`
--

DROP TABLE IF EXISTS `t_company_name`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_company_name` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `remark` varchar(4000) DEFAULT NULL,
  `customer_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_company_name`
--

LOCK TABLES `t_company_name` WRITE;
/*!40000 ALTER TABLE `t_company_name` DISABLE KEYS */;
INSERT INTO `t_company_name` VALUES (1,'到沙发范德萨',161,'周萍','2018-05-16 08:05:31','到沙发凤',0),(2,'到沙发范德萨',161,'周萍','2018-05-16 08:07:46','到沙发凤',0),(3,'上达到',161,'周萍','2018-05-16 08:09:28','撒',0),(5,'阿斯顿是',161,'周萍','2018-05-16 08:23:44','士大夫士大夫',1),(6,'到沙发到沙发萨达',161,'周萍','2018-05-16 08:23:38','',1),(7,'范德萨',161,'周萍','2018-05-16 08:23:51','到沙发士大夫萨达',1),(8,'广州市泰紫阁贸易有限公司',95,'何诗明','2018-10-08 06:32:38','',4073),(9,'广州市泰紫阁贸易有限公司1',95,'何诗明','2018-10-08 06:32:55','',4073),(10,'我是新公司',116,'陈太智','2018-10-11 02:44:10','',4094),(11,'广州薇恩展览服务有限公司1',116,'陈太智','2018-10-11 02:44:26','',4094),(12,'广州腾睿控股有限公司',119,'罗文波','2018-10-17 07:37:54','',2277),(13,'广州腾睿控股有限公司1',119,'罗文波','2018-10-17 07:38:11','',2277),(14,'广州腾睿控股有限公司',119,'罗文波','2018-10-17 07:38:27','',2277),(15,'广州腾睿控股有限公司2',119,'罗文波','2018-10-17 07:38:57','',2277),(16,'广州腾睿控股有限公司',119,'罗文波','2018-10-17 07:45:31','',2277),(17,'广州腾睿控股有限公司1',119,'罗文波','2018-10-17 07:45:42','',2277),(18,'广州寰宇电子商务有限公司',97,'庄培润','2018-10-17 07:58:53','',1593),(19,'广州寰宇电子商务有限公司1',97,'庄培润','2018-10-17 07:59:21','',1593),(20,'广州寰宇电子商务有限公司',97,'庄培润','2018-10-17 07:59:39','',1593),(21,'广州寰宇电子商务有限公司1',97,'庄培润','2018-10-17 07:59:47','',1593),(22,'广州寰宇电子商务有限公司',97,'庄培润','2018-10-17 08:00:05','',1593),(23,'广州寰宇电子商务有限公',97,'庄培润','2018-10-17 08:10:25','',1593),(24,'广州寰宇电子商务有限公司',97,'庄培润','2018-10-17 08:10:58','',1593),(25,'广东坤玛机电有限公司',116,'陈太智','2018-10-22 03:36:45','',1881),(26,'广东坤玛机电有限公司1',116,'陈太智','2018-10-22 06:43:31','',1881),(27,'广东坤玛机电有限公司',116,'陈太智','2018-10-22 06:44:56','',1881),(28,'广东坤玛机电有限公司1',116,'陈太智','2018-10-22 06:45:41','',1881),(29,'广州市富钰文化传播有限公司',119,'罗文波','2018-10-22 06:48:58','',3249),(30,'广州厚锟服饰有限公司',116,'陈太智','2018-10-22 06:50:03','',3249),(31,'广东匀见机电科技有限公司',116,'陈太智','2018-10-22 06:53:34','',3599),(32,'广州市富钰文化传播有限公司',119,'罗文波','2018-10-22 07:03:29','',3249),(33,'广州厚锟服饰有限公司',119,'罗文波','2018-10-22 07:04:32','',3249),(34,'广州市冰芯蝶化妆品有限公司',116,'陈太智','2018-10-31 10:02:47','',1419),(35,'广州市冰芯蝶化妆品有限公司1',116,'陈太智','2018-10-31 10:03:03','',1419),(36,'广州骏新贸易有限公司',106,'陈小银','2018-10-31 10:14:42','',2894),(37,'广州市冰芯蝶化妆品有限公司',106,'陈小银','2018-10-31 10:23:06','',1419),(38,'广州市冰芯蝶化妆品有限公司1',106,'陈小银','2018-10-31 10:23:20','',1419),(39,'广州市冰芯蝶化妆品有限公司',106,'陈小银','2018-10-31 10:26:34','',1419),(40,'广州婀娜服饰有限公司',116,'陈太智','2018-10-31 10:27:44','',852);
/*!40000 ALTER TABLE `t_company_name` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:23:02
