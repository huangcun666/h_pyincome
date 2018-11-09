-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 192.168.2.169    Database: db_building
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
-- Table structure for table `t_user`
--

DROP TABLE IF EXISTS `t_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL DEFAULT '',
  `pswd` varchar(255) NOT NULL DEFAULT '',
  `email` varchar(255) NOT NULL DEFAULT '',
  `phone` varchar(255) NOT NULL DEFAULT '',
  `is_lock` tinyint(1) NOT NULL DEFAULT '0',
  `role` int(11) DEFAULT NULL,
  `reg_time` datetime NOT NULL,
  `remark` varchar(4000) DEFAULT NULL,
  `is_first` int(11) NOT NULL DEFAULT '0',
  `is_admin` tinyint(11) NOT NULL DEFAULT '0',
  `guid` varchar(255) NOT NULL DEFAULT '',
  `is_child_uid` int(11) NOT NULL DEFAULT '0',
  `order_int` int(11) NOT NULL DEFAULT '0',
  `is_cq` int(11) NOT NULL DEFAULT '0',
  `is_manager` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_user`
--

LOCK TABLES `t_user` WRITE;
/*!40000 ALTER TABLE `t_user` DISABLE KEYS */;
INSERT INTO `t_user` VALUES (1,'domizzi','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,0,'b7d87b2a-28c4-11e8-89fc-00163e028ada',0,0,0,0),(5,'天河北','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87e4a-28c4-11e8-89fc-00163e028ada',0,0,0,0),(6,'尚城','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87ea5-28c4-11e8-89fc-00163e028ada',0,0,0,0),(7,'米酷','930ada2b9f4f5aaddd8096deae230b28','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87ed8-28c4-11e8-89fc-00163e028ada',0,0,0,0),(8,'百信广场','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87f08-28c4-11e8-89fc-00163e028ada',0,0,0,0),(9,'城市之光','9d279e579ef3173824c12802bdf15efd','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87f38-28c4-11e8-89fc-00163e028ada1dsadasdsa',0,0,0,0),(10,'海上传奇','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87f6a-28c4-11e8-89fc-00163e028ada',0,0,0,0),(11,'万科黄埔中心','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87f98-28c4-11e8-89fc-00163e028ada',0,0,0,0),(12,'陈小银','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,0,'b7d87fc8-28c4-11e8-89fc-00163e028ada',0,0,1,0),(13,'冯恒敏','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,1,'b7d88208-28c4-11e8-89fc-00163e028adasadasda',0,0,0,0),(14,'李江友','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,1,'b7d8827d-28c4-11e8-89fc-00163e028ada',0,0,0,0),(15,'钟晓鸣','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,1,'b7d8827d-28c4-11e8-89fc-00163e028adbs',0,0,0,0),(16,'米酷01','b41786a2b6c87709c4634c8dbf767f9d','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87ed8-28c4-11e8-89fc-00163e028ada',7,0,0,0),(17,'米酷02','9ed6cf33ee9a60c88bf45d1fe0f1242e','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87ed8-28c4-11e8-89fc-00163e028ada',7,0,0,0),(18,'世博汇','6d47b6cdf7b1aa1904d66642d868e0e7','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'db7d87e4a-28c4-11e8-89fc-asdaasdasdasd',0,0,0,0),(19,'其他','9f9c1f4f76f1719a8d32f6c1dd5f84a3','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87e4a-28c4-11e8-89fc-00163e028ada',0,1000,0,0),(20,'远洋天骄','e8fb700487c0ea4edb99e427632a40b5','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'b7d87e4a-28c4-11e8-89fc-00163e028ada',0,0,0,0),(21,'钟明霞','1b8a9966fadd8a5ddd1cc4a7e65fae65','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,0,'b7d87fc8-28c4-11e8-89fc-00163e028adadasdasdasd',0,0,1,0),(22,'钟东梅','141602a1850aa8b4ebe56843c036132d','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,0,'b7d87fc8-28c4-11e8-89fc-00163e028ada',0,0,1,0),(23,'罗文波','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,1,'b7d88208-28c4-11e8-89fc-00163e028ada',0,0,0,0),(24,'陈太智','200820e3227815ed1756a6b531e7e0d2','214124','12312312',0,1,'2017-09-09 00:00:00',NULL,0,1,'b7d88208-28c4-11e8-89fc-00163e028ada',0,0,0,0),(25,'佳兆业未来城','a8c410d123c1c9cae0f6bb0e551d80d4','214124','12312312',0,2,'2017-09-09 00:00:00',NULL,0,0,'fddfsfdsfs-28c4-11e8-89fc-00163e028adafdsfsdfdsfdsd',0,0,0,0);
/*!40000 ALTER TABLE `t_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-09 17:32:44