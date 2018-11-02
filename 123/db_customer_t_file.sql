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
-- Table structure for table `t_file`
--

DROP TABLE IF EXISTS `t_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `guid` varchar(155) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `file_remark` varchar(4000) DEFAULT NULL,
  `file_name` varchar(555) DEFAULT '',
  `created_at` datetime DEFAULT NULL,
  `uid` int(11) NOT NULL DEFAULT '0',
  `uid_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_file`
--

LOCK TABLES `t_file` WRITE;
/*!40000 ALTER TABLE `t_file` DISABLE KEYS */;
INSERT INTO `t_file` VALUES (6,21,'363f3b2f-529e-11e8-a20d-6045cb9a7117','fsd','fsdfsd','/static/customer/21/949666b1-2e35-4f69-95f3-36b46c25ae0b_21.jpg','2018-05-08 09:00:10',116,'陈太智'),(8,2533,'f93709d9-64b3-11e8-b807-6045cb9a7117','xcvx','xcxcv',NULL,'2018-05-31 09:21:17',161,'周萍'),(9,1994,'984454de-8e35-11e8-b047-6045cb9a7117','新玖力—一般纳税人认定','','/static/customer/1994/d0dc6e6c-400b-4ed9-b145-5ddc809bf7ae_1994.jpg','2018-07-23 05:02:27',174,'伍荷敏'),(10,913,'3743fa5d-9c48-11e8-b047-6045cb9a7117','一般纳税人改为小规模纳税人','','/static/customer/913/1d70a485-8653-4f89-baf4-d39412ba1cc9_913.jpg','2018-08-10 02:51:01',192,'马嘉欣'),(12,3168,'ca75e9fb-a055-11e8-b047-6045cb9a7117','鸿瑞2018.08.15日升为一般纳税人','','/static/customer/3168/9eb4ccaa-99d6-4201-aecf-ed339542dd0d_3168.jpg','2018-08-15 06:38:16',174,'伍荷敏'),(15,1,'524405ed-a4ed-11e8-b047-6045cb9a7117','广州市丽眼饰衣服饰有限公司、记账合同、20160801、20180701','','/static/customer/1/广州市丽眼饰衣服饰有限公司、记账合同、20160801、20180701.pdf_1.pdf','2018-08-21 02:53:02',98,'吴蔚亮');
/*!40000 ALTER TABLE `t_file` ENABLE KEYS */;
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
