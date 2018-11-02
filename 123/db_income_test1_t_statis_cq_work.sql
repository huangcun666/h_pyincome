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
-- Table structure for table `t_statis_cq_work`
--

DROP TABLE IF EXISTS `t_statis_cq_work`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t_statis_cq_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `uid_name` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `busniess_from_id_name` varchar(45) DEFAULT NULL,
  `project_count` int(11) DEFAULT '0',
  `all_count` int(11) DEFAULT '0',
  `updated_at` datetime DEFAULT NULL,
  `busniess_from_id` int(11) NOT NULL DEFAULT '0',
  `btype_name` varchar(255) DEFAULT NULL,
  `btype_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14137 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t_statis_cq_work`
--

LOCK TABLES `t_statis_cq_work` WRITE;
/*!40000 ALTER TABLE `t_statis_cq_work` DISABLE KEYS */;
INSERT INTO `t_statis_cq_work` VALUES (14126,139,'陈勇极','2018-09-19 00:00:00','内部推荐',2,3,NULL,81,'公司注册',155),(14127,139,'陈勇极','2018-09-19 00:00:00','推广',3,7,NULL,2,'公司注册',155),(14128,139,'陈勇极','2018-09-19 00:00:00','内部推荐',1,2,NULL,81,'公司变更',156),(14129,139,'陈勇极','2018-09-19 00:00:00','推广',2,3,NULL,2,'公司变更',156),(14130,139,'陈勇极','2018-09-19 00:00:00','内部推荐',1,1,NULL,81,'解除异常',157),(14131,139,'陈勇极','2018-09-19 00:00:00','推广',1,1,NULL,2,'解除异常',157),(14132,139,'陈勇极','2018-09-19 00:00:00','内部推荐',1,1,NULL,81,'公司注销',158),(14133,139,'陈勇极','2018-09-19 00:00:00','推广',2,2,NULL,2,'公司注销',158),(14134,139,'陈勇极','2018-09-19 00:00:00','推广',1,2,NULL,2,'商标',159),(14135,139,'陈勇极','2018-09-19 00:00:00','推广',1,1,NULL,2,'特殊业务',160),(14136,139,'陈勇极','2018-09-19 00:00:00','内部推荐',1,1,NULL,81,'其他业务',161);
/*!40000 ALTER TABLE `t_statis_cq_work` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-02 16:22:55
