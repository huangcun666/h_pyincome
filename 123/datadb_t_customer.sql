-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: datadb
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
-- Table structure for table `t_customer`
--

DROP TABLE IF EXISTS `t_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `company` varchar(20) DEFAULT NULL,
  `linkman` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `yewu_content` varchar(100) DEFAULT NULL,
  `address_style` varchar(20) DEFAULT NULL,
  `start_hetong` date DEFAULT NULL,
  `end_hetong` date DEFAULT NULL,
  `date_chengli` date DEFAULT NULL,
  `date_zhizhao` date DEFAULT NULL,
  `date_address` date DEFAULT NULL,
  `kf_name` varchar(20) DEFAULT NULL,
  `sale_name` varchar(20) DEFAULT NULL,
  `zhuanshang` varchar(20) DEFAULT NULL,
  `kuaiji` varchar(20) DEFAULT NULL,
  `address_gongying` varchar(20) DEFAULT NULL,
  `gongshang_name` varchar(255) DEFAULT NULL,
  `dishui_name` varchar(255) DEFAULT NULL,
  `guoshui_name` varchar(255) DEFAULT NULL,
  `bank_account` varchar(245) DEFAULT NULL,
  `bank_name` varchar(255) DEFAULT NULL,
  `kuaji_uid` int(11) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer`
--

LOCK TABLES `t_customer` WRITE;
/*!40000 ALTER TABLE `t_customer` DISABLE KEYS */;
INSERT INTO `t_customer` VALUES (3,12,'有限公司','张益达啊啊啊','10086','福地方地方','福地方','2018-04-10','2018-04-04','2018-03-28','2018-04-09','2018-04-18','张益达','张益达','张益达','张益达','张益达',NULL,NULL,NULL,NULL,NULL,0,NULL,NULL),(4,14,'有限公司','张益达','10086','奋斗法','福福福','2018-04-11','2018-04-18','2018-04-11','2018-04-15','2018-04-17','张益达','张益达','张益达','张益达','张益达',NULL,NULL,NULL,NULL,NULL,0,NULL,NULL),(22,15,'多易','老徐','11111','神武','福','2018-04-19','2018-04-30','2018-04-19','2018-05-16','2018-06-20','张伟','张伟','张伟','张伟','张大炮',NULL,NULL,NULL,NULL,NULL,0,NULL,NULL),(25,1111,'111','111','11','11','111',NULL,NULL,NULL,NULL,NULL,'111','11','11','111','11',NULL,NULL,NULL,NULL,NULL,0,NULL,NULL);
/*!40000 ALTER TABLE `t_customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:22:46
