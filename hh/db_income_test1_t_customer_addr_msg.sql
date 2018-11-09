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
-- Table structure for table `t_customer_addr_msg`
--

DROP TABLE IF EXISTS `t_customer_addr_msg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_customer_addr_msg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `tel` varchar(45) DEFAULT NULL,
  `addr` varchar(45) DEFAULT NULL,
  `company` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT '0',
  `uid_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_customer_addr_msg`
--

LOCK TABLES `t_customer_addr_msg` WRITE;
/*!40000 ALTER TABLE `t_customer_addr_msg` DISABLE KEYS */;
INSERT INTO `t_customer_addr_msg` VALUES (1,'秦卓奕','13800138000','广州市南沙区留新路（留新段）3号（自编2栋）302房',NULL,0,NULL),(2,'王硕','13800138000','广州市天河区棠东东路9号306房',NULL,0,NULL),(3,'秦卓奕','13800138888','广州市南沙区留新路（留新段）3号（自编2栋）302房',NULL,0,NULL),(20,'王神龙','13800138000','广州市天河区石牌西路8号801房自编839房','龙惠（广州）电器设备有限公司',116,'陈太智'),(21,'123','123','123','',116,'陈太智'),(22,'1','1233333','1','',116,'陈太智'),(23,'陈欢欢','13800138000','123','',116,'陈太智'),(24,'1','23','333','',116,'陈太智'),(25,'323','23323','232323','广州市丽眼饰衣服饰有限公司',116,'陈太智'),(26,'123456','123567','123666','广州市晶名贸易有限公司',116,'陈太智'),(27,'1433223','1433223','1433223','',116,'陈太智'),(28,'14444','144444','144444','',116,'陈太智'),(29,'1','1','1','',116,'陈太智'),(30,'4444','4444','4444','',116,'陈太智'),(31,'黄','无','32','',180,'黄晓晴'),(32,'黄','3232','2332','',180,'黄晓晴'),(33,'黄','222222','33333333','',180,'黄晓晴'),(35,'郑东丰','18202026552','123','广州海罗黎电子科技有限公司',116,'陈太智'),(36,'111111','111111','111111111111','广州市晶名贸易有限公司',116,'陈太智'),(37,'5555','55555','55555','广州市晶名贸易有限公司',116,'陈太智'),(38,'66666666','6666666','6666666','23',116,'陈太智'),(39,'陈丽萍','13800138000','11123','广州亨博贸易有限公司',119,'罗文波'),(40,'陈丽萍','13800138000','23233','广州亨博贸易有限公司',119,'罗文波'),(41,'陈丽萍','13800138000','666666666666','广州亨博贸易有限公司',119,'罗文波'),(42,'邵瑛','13800138000','广州市天河区兴民路222号1305房','广州英伦教育咨询服务有限公司',119,'罗文波'),(43,'sss','sss','sss','sss',116,'陈太智'),(44,'婀娜','无','7','广州婀娜服饰有限公司',119,'罗文波'),(45,'2','2','2','2',95,'何诗明'),(46,'xxx','11111','23','广州凡几文化发展有限公司',180,'黄晓晴'),(47,'冰芯','1','11','广州市冰芯蝶化妆品有限公司',116,'陈太智'),(48,'1','2','2','无',164,'张会会');
/*!40000 ALTER TABLE `t_customer_addr_msg` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:55
