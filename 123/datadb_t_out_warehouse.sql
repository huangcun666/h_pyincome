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
-- Table structure for table `t_out_warehouse`
--

DROP TABLE IF EXISTS `t_out_warehouse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_out_warehouse` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serial_num` varchar(10) DEFAULT NULL,
  `num` varchar(10) DEFAULT NULL,
  `rev_time` date DEFAULT NULL,
  `dis_time` date DEFAULT NULL,
  `saleman` varchar(20) DEFAULT NULL,
  `telemark` varchar(20) DEFAULT NULL,
  `group_leader` varchar(20) DEFAULT NULL,
  `gen_dan` varchar(20) DEFAULT NULL,
  `source_bus` varchar(100) DEFAULT NULL,
  `customer_name` varchar(20) DEFAULT NULL,
  `company_name` varchar(20) DEFAULT NULL,
  `regist_id` varchar(100) DEFAULT NULL,
  `bus_content` varchar(100) DEFAULT NULL,
  `company_type` varchar(20) DEFAULT NULL,
  `legal_person` varchar(20) DEFAULT NULL,
  `supervisor` varchar(20) DEFAULT NULL,
  `share_holder` varchar(20) DEFAULT NULL,
  `regist_money` varchar(20) DEFAULT NULL,
  `address_type` varchar(20) DEFAULT NULL,
  `progress` varchar(20) DEFAULT NULL,
  `tally` varchar(10) DEFAULT NULL,
  `server_money` varchar(20) DEFAULT NULL,
  `rec_money` varchar(20) DEFAULT NULL,
  `contract_confirm` varchar(10) DEFAULT NULL,
  `baijie_time` date DEFAULT NULL,
  `remarks` varchar(200) DEFAULT NULL,
  `move_time` date DEFAULT NULL,
  `zhizhao_detail` varchar(500) DEFAULT NULL,
  `accept_man` varchar(20) DEFAULT NULL,
  `other_remarks` varchar(20) DEFAULT NULL,
  `out_time` date DEFAULT NULL,
  `date_kaipiao` date DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `retainage` varchar(20) DEFAULT NULL,
  `banjie_cycle` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_out_warehouse`
--

LOCK TABLES `t_out_warehouse` WRITE;
/*!40000 ALTER TABLE `t_out_warehouse` DISABLE KEYS */;
INSERT INTO `t_out_warehouse` VALUES (2,'1','2','2018-04-01','2018-04-02','33','44','55','66','77','88','99','100','101','多人','102','103','104','105','106','107','否','108','323','','2018-04-12','323','2018-04-10','福分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分福分分分分分分分分分分分分分分分分分分分分分分','1232','福地方','2018-04-04','2018-04-12','123213213','323','22'),(3,'11','22','2018-04-03','2018-04-10','33','44','55','66','77','88','99','100','101','多人','102','103','104','105','106','107','否','108','323','','2018-04-12','323','2018-04-10','福分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分分福分分分分分分分分分分分分分分分分分分分分分分','1232','福地方','2018-04-04','2018-04-12','123213213','323','22');
/*!40000 ALTER TABLE `t_out_warehouse` ENABLE KEYS */;
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
