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
-- Table structure for table `t_customer_account`
--

DROP TABLE IF EXISTS `t_customer_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(255) DEFAULT NULL,
  `psw` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `created_by` varchar(255) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `updated_by` varchar(255) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `type_id` int(11) NOT NULL DEFAULT '0',
  `type_id_name` varchar(255) DEFAULT NULL,
  `customer_id` int(11) NOT NULL,
  `created_by_uid` int(11) DEFAULT NULL,
  `updated_by_uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_account`
--

LOCK TABLES `t_customer_account` WRITE;
/*!40000 ALTER TABLE `t_customer_account` DISABLE KEYS */;
INSERT INTO `t_customer_account` VALUES (4,'dfs','fdsfd','2018-05-11 07:16:26','陈太智','2018-05-11 07:16:26','陈太智','sfddf',7,'地税',28,116,116),(5,'dfs','fdsfd','2018-05-11 07:16:28','陈太智','2018-05-11 07:16:28','陈太智','sfddf',7,'地税',28,116,116),(6,'dfs','fdsfd','2018-05-11 07:16:28','陈太智','2018-05-11 07:16:28','陈太智','sfddf',7,'地税',28,116,116),(7,'asd','asdsad','2018-05-11 07:16:41','陈太智','2018-05-11 07:16:41','陈太智','dsaasd',8,'实名',28,116,116),(8,'fds','sdf','2018-05-11 07:17:39','陈太智','2018-05-11 07:17:39','陈太智','',8,'实名',28,116,116),(9,'fds','sdf','2018-05-11 07:34:42','陈太智','2018-05-11 07:34:42','陈太智','sadads',8,'实名',28,116,116),(10,'fds11111','sdf','2018-05-11 07:34:52','陈太智','2018-05-11 07:34:52','陈太智','',8,'实名',28,116,116),(11,'选择','选择','2018-05-11 07:36:05','陈太智','2018-05-11 07:36:05','陈太智','',8,'实名',28,116,116);
/*!40000 ALTER TABLE `t_customer_account` ENABLE KEYS */;
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
