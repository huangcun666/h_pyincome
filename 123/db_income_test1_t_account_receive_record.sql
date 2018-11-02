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
-- Table structure for table `t_account_receive_record`
--

DROP TABLE IF EXISTS `t_account_receive_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_account_receive_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jiesuan_cycle` varchar(45) DEFAULT NULL,
  `year_charge` int(11) DEFAULT NULL,
  `month_charge` int(11) DEFAULT NULL,
  `zhangce_charge` int(11) DEFAULT NULL,
  `account_charge_end_date` datetime DEFAULT NULL,
  `zhangce_charge_end_date` datetime DEFAULT NULL,
  `new_yishou_detail` varchar(500) DEFAULT NULL,
  `yingshou_detail` varchar(500) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `account_id` int(11) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_account_receive_record`
--

LOCK TABLES `t_account_receive_record` WRITE;
/*!40000 ALTER TABLE `t_account_receive_record` DISABLE KEYS */;
INSERT INTO `t_account_receive_record` VALUES (2,'季付',123,11,0,NULL,NULL,'','','2018-08-31 14:09:40',3,NULL,NULL,NULL),(3,'月付',23,3,0,NULL,NULL,'3','3','2018-08-31 16:25:02',3,NULL,NULL,NULL),(4,'半年付',1,2,3,'2018-08-09 00:00:00','2018-08-16 00:00:00','4','5','2018-08-31 17:21:09',3,NULL,'冯恒敏',118),(5,'年付',1,2,3,NULL,NULL,'','','2018-08-31 17:44:15',4,NULL,'冯恒敏',118),(6,'半年付',1,2,3,NULL,NULL,'','','2018-08-31 17:45:24',4,NULL,'冯恒敏',118),(7,'',0,0,0,NULL,NULL,'','','2018-09-03 09:38:15',5,NULL,'庄培润',97),(8,'年付',0,0,0,NULL,NULL,'','','2018-09-03 09:42:12',4,NULL,'庄培润',97),(9,'年付',100,1000,1111,'2018-09-04 00:00:00','2018-09-05 00:00:00','萨达','的撒','2018-09-03 09:51:03',5,NULL,'吴蔚亮',98),(10,'年付',1,1,1,NULL,NULL,'','','2018-09-03 10:14:06',7,NULL,'庄培润',97),(11,'年付',11,11,11,NULL,NULL,'','','2018-09-03 10:14:31',8,NULL,'庄培润',97),(15,'',0,0,0,NULL,NULL,'','','2018-09-05 09:35:51',11,NULL,'陈太智',116),(16,'',0,0,0,NULL,NULL,'','','2018-09-05 09:37:16',12,NULL,'陈太智',116),(17,'年付',1,0,1,'2018-09-01 00:00:00','2018-09-05 00:00:00','不怒','帮你买吧','2018-09-05 09:53:49',12,NULL,'陈太智',116),(18,'年付',111,11,1111,'2018-09-05 00:00:00','2018-09-06 00:00:00','11','111','2018-09-05 10:01:54',12,NULL,'陈太智',116),(19,'年付',3060,230,300,'2018-09-01 00:00:00','2018-09-01 00:00:00','2018.08记账费+2018.08账册费','2018.09-2019.08记账费2760+2018.09-2019.08账册费费300','2018-09-05 10:27:33',7,NULL,'陈太智',116),(20,'年付',0,0,0,NULL,NULL,'2018.09-2019.02记账费1380+2018.09-2019.02账册费费150','2019.03-2019.08记账费1360+2019.03-2019.08账册费费150','2018-09-05 10:31:59',7,'2018-09-05 10:55:37','陈太智',116),(21,'年付',0,0,0,NULL,NULL,'2019.03-2019.08记账费1360+2019.03-2019.08账册费费150','','2018-09-05 10:56:31',7,NULL,'陈太智',116),(22,'',0,0,0,NULL,NULL,'','','2018-09-05 11:45:29',13,NULL,'赵松筑',121),(23,'年付',12,22,33,NULL,NULL,'','','2018-09-05 14:09:19',13,'2018-09-05 14:46:22','赵松筑',121),(24,'月付',144,144,144,'2018-09-06 00:00:00','2018-09-14 00:00:00','1444','144','2018-09-05 14:46:45',13,NULL,'赵松筑',121),(25,'年付',11,111,111,'2018-09-05 00:00:00','2018-09-29 00:00:00','111','11','2018-09-05 15:17:51',13,NULL,'陈太智',116),(26,'',0,0,0,NULL,NULL,'','','2018-09-05 15:26:12',14,NULL,'江嘉琳',153);
/*!40000 ALTER TABLE `t_account_receive_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:22:51
