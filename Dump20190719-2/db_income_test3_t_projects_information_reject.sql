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
-- Table structure for table `t_projects_information_reject`
--

DROP TABLE IF EXISTS `t_projects_information_reject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_projects_information_reject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(10) unsigned DEFAULT NULL,
  `project_guid` varchar(45) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `reject_msg` varchar(1000) DEFAULT NULL,
  `reject_msg_titles` varchar(500) DEFAULT NULL,
  `handler_uid` int(11) DEFAULT NULL,
  `handler_name` varchar(45) DEFAULT NULL,
  `handler_at` datetime DEFAULT NULL,
  `confirm_at` datetime DEFAULT NULL,
  `confirm_status` tinyint(4) DEFAULT NULL,
  `confirm_reject_msg` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id_idx` (`project_id`),
  CONSTRAINT `project_id` FOREIGN KEY (`project_id`) REFERENCES `t_projects` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_projects_information_reject`
--

LOCK TABLES `t_projects_information_reject` WRITE;
/*!40000 ALTER TABLE `t_projects_information_reject` DISABLE KEYS */;
INSERT INTO `t_projects_information_reject` VALUES (1,11024,'1f684a77-ff49-4979-8327-0773fba69a33',98,'吴蔚亮','2019-06-17 00:00:00','的反复哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇哇发的广泛的放',NULL,97,'庄培润','2019-06-17 15:18:11','2019-06-17 15:29:08',1,''),(2,11024,'1f684a77-ff49-4979-8327-0773fba69a33',98,'吴蔚亮','2019-06-17 10:57:56','房斯蒂芬速度放松付三房的斯蒂芬森地方房斯蒂芬速度放松付三房的斯蒂芬森地方',NULL,97,'庄培润','2019-06-17 17:32:58',NULL,2,'人'),(3,11024,'1f684a77-ff49-4979-8327-0773fba69a33',98,'吴蔚亮','2019-06-17 11:04:53','房斯蒂芬斯蒂芬斯蒂芬个二哥二',NULL,97,'庄培润','2019-06-17 16:47:48',NULL,NULL,NULL),(4,11370,'3b09d3bf-a5b0-4bb7-a060-723aff9431eb',98,'吴蔚亮','2019-06-17 15:50:22','韩国人巴尔干我恶',NULL,199,'杨辉',NULL,NULL,NULL,NULL),(5,11024,'1f684a77-ff49-4979-8327-0773fba69a33',98,'吴蔚亮','2019-06-17 17:02:05','sffd1',NULL,97,'庄培润','2019-06-17 17:30:46',NULL,NULL,NULL),(6,11024,'1f684a77-ff49-4979-8327-0773fba69a33',116,'陈太智','2019-06-17 17:36:19','ffff',NULL,97,'庄培润',NULL,NULL,NULL,NULL),(7,11024,'1f684a77-ff49-4979-8327-0773fba69a33',116,'陈太智','2019-06-17 17:36:25','gfdgdg',NULL,97,'庄培润',NULL,NULL,NULL,NULL),(8,11024,'1f684a77-ff49-4979-8327-0773fba69a33',116,'陈太智','2019-06-17 17:37:33','gggg',NULL,97,'庄培润',NULL,NULL,NULL,NULL),(9,11024,'1f684a77-ff49-4979-8327-0773fba69a33',116,'陈太智','2019-06-17 17:39:03','fffff',NULL,97,'庄培润',NULL,NULL,NULL,NULL),(10,11395,'46e4e06b-ad7e-4546-b1b0-bb4dd4c7fcd6',116,'陈太智','2019-06-17 17:40:36','rrrrrr',NULL,121,'赵松筑',NULL,NULL,NULL,NULL),(11,11395,'46e4e06b-ad7e-4546-b1b0-bb4dd4c7fcd6',116,'陈太智','2019-06-19 11:31:22','122',NULL,121,'赵松筑',NULL,NULL,NULL,NULL),(12,11367,'14007f17-26b8-45a3-b89d-ab00d744a564',98,'吴蔚亮','2019-06-19 17:39:55','放松的',NULL,235,'陈可彬',NULL,NULL,NULL,NULL),(13,2564,'3d7938c2-a88d-4fac-b333-c7aecf0c7102',116,'陈太智','2019-06-21 09:33:36','123',NULL,97,'庄培润',NULL,NULL,NULL,NULL),(14,9210,'64eea52b-e9b5-4f4a-8b79-1bbe9bfedbd9',116,'陈太智','2019-06-21 16:17:46','123',NULL,116,'陈太智','2019-07-17 15:21:41',NULL,NULL,NULL),(15,11395,'46e4e06b-ad7e-4546-b1b0-bb4dd4c7fcd6',116,'陈太智','2019-06-21 16:54:26','是否记账:1231,合同情况:我恶法愕万分,','is_finance,new_contract_type_id,',121,'赵松筑','2019-06-24 09:38:55',NULL,NULL,NULL),(16,11395,'46e4e06b-ad7e-4546-b1b0-bb4dd4c7fcd6',98,'吴蔚亮','2019-06-21 17:06:19','内部推荐人:i花好月圆夜,联系方式:得粉碎饭,','recommend_staff,customer_tel,',121,'赵松筑','2019-06-24 09:53:56',NULL,2,'给我改'),(17,11395,'46e4e06b-ad7e-4546-b1b0-bb4dd4c7fcd6',98,'吴蔚亮','2019-06-21 17:29:45','内部推荐人:i花好月圆夜,联系方式:得粉碎饭,签约方式:得粉碎饭,','recommend_staff,customer_tel,sign_type_id,',121,'赵松筑','2019-06-24 09:38:11','2019-06-24 09:48:21',1,''),(18,11336,'f99e71c3-dedb-4010-b601-50288bfc8c17',98,'吴蔚亮','2019-06-21 17:31:07','来源方式:1231321,','talk_type,',121,'赵松筑',NULL,NULL,NULL,NULL),(19,11381,'1ef02c77-f91b-4f3b-9dae-77b5331998c3',98,'吴蔚亮','2019-06-24 10:13:53','业务收入明细:填错了,合同情况:什么情况,','yewu,new_contract_type_id,',121,'赵松筑',NULL,NULL,NULL,NULL),(20,11290,'dc67ce16-ea56-4bec-97d5-5d30fadaf831',98,'吴蔚亮','2019-06-24 10:15:31','业务收入明细:填错了,合同情况:什么情况,','yewu,new_contract_type_id,',121,'赵松筑','2019-06-24 10:19:19','2019-06-24 10:22:56',2,'给我改');
/*!40000 ALTER TABLE `t_projects_information_reject` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-19 17:07:20
